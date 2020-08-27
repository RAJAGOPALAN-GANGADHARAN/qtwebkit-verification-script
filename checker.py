import sys
from jinja2 import Environment, FileSystemLoader
import argparse
import os

parser = argparse.ArgumentParser(description='Checker for Qtwebkit Binaries')
parser.add_argument("--version",help=r"Version history of the form {major_version}.{minor_version}.{ver_patch}",required=True)
parser.add_argument("--qt",help="Root of Qt installation")
parser.add_argument("--build",help="Root of build directory",required=True)
parser.add_argument("--os",help="Operating system",required=True,choices=["linux","macos","windows"])
parser.add_argument("--template", help="Name of template file", default="template.txt")
parser.add_argument("--build_type", help="Build Type", default="Release", choices=["Release", "Debug"])

args = parser.parse_args()

file_loader = FileSystemLoader('.') # directory of template file
env = Environment(loader=file_loader)

template = env.get_template(args.template) # load template file

major,minor,patch=args.version.split('.')

check_list = template.render(os=args.os,
    major=major,minor=minor,ver_patch=patch).split('\n')

file_count = {"linux": 109, "windows": 118,"windowsRelease":110, "macos": 170}


def verify_linux(check_list):
    error_list = []
    count = 0
    
    qmake = os.popen('qmake -query').read().split('\n')
    qtD = dict()
    with open('data/Linux.txt', 'r') as vf:
        arr = vf.readlines()

    for line in arr:
        if line.rstrip() not in check_list:
            print(line)

    for q in qmake:
        qq = q.split(':')
        if len(qq) == 2:
            qtD[qq[0]] = qq[1]

    for line in check_list:
        if line.rstrip():
            if line.startswith('include/'):
                chk_path = os.path.join(qtD['QT_INSTALL_HEADERS'], line[len('include/'):])
            elif line.startswith('lib/'):
                chk_path = os.path.join(qtD['QT_INSTALL_LIBS'], line[len('lib/'):])
            elif line.startswith('mkspecs/') or line.startswith('qml/'):
                chk_path = os.path.join(qtD['QT_INSTALL_ARCHDATA'], line)
            elif line.startswith('libexec/'):
                chk_path = os.path.join(qtD['QT_INSTALL_LIBEXECS'], line[len('libexec/'):])

            count+=1

            if not os.path.isfile(chk_path):
                error_list.append(chk_path)

    return [error_list, count]
            
def verify_windows_mac(check_list):
    error_list = []
    count = 0
    
    for line in check_list:
        if line.rstrip():
            if line.startswith('bin'):
                chk_path = os.path.join(args.build, line)
            else:
                chk_path = os.path.join(args.qt, line)

            count+=1
            if not os.path.isfile(chk_path):
                error_list.append(chk_path)
    
    return [error_list, count]


if args.os == 'linux':
    res = verify_linux(check_list)
elif args.os == 'windows' or args.os == 'macos':
    res = verify_windows_mac(check_list)

    
print("Verified {0}/{1} files".format(res[1],file_count[args.os+args.build_type]))
if len(res[0])!=0:
    print("Errors found files below are missing:")
    for err in res[0]:
        print(err)
    exit(1)


#python3 checker.py --version 5.212.0 --build /mnt/c/qtwebkit/build --os linux
#
# py checker.py --version 5.20.0 --qt "C:/Qt/5.14.2/msvc2017_64" --build "C:/qtwebkit/build/" --os windows
