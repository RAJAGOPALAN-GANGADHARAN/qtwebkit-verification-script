import sys
from jinja2 import Environment, FileSystemLoader
import argparse
import os

parser = argparse.ArgumentParser(description='Checker for Qtwebkit Binaries')
parser.add_argument("--version",help=r"Version history of the form {major_version}.{minor_version}.{ver_patch}",required=True)
parser.add_argument("--qt",help="Root of Qt installation",required=True)
parser.add_argument("--build",help="Root of build directory",required=True)
parser.add_argument("--os",help="Operating system",required=True,choices=["linux","macos","windows"])
parser.add_argument("--template",help="Name of template file",default="template.txt")

args = parser.parse_args()

file_loader = FileSystemLoader('.') # directory of template file
env = Environment(loader=file_loader)

template = env.get_template(args.template) # load template file

major,minor,patch=args.version.split('.')

check_list = template.render(os=args.os,
    major=major,minor=minor,ver_patch=patch).split('\n')

error_list=[]
for line in check_list:
    if line.rstrip():
        if line.startswith('bin'):
            chk_path = os.path.join(args.build, line)
        else:
            chk_path = os.path.join(args.qt, line)

        if not os.path.isfile(chk_path):
            error_list.append(chk_path)

if len(error_list) == 0:
    print("All verified")
    exit(0)
else:
    print("Errors found files below are missing:")
    for err in error_list:
        print(err)
    exit(1)


#python3 checker.py --version 5.14.1 --qt "C:/Qt/" --build "C:/qtwebkit/build/" --os linux
#py checker.py --version 5.20.0 --qt "C:/Qt/5.14.2/msvc2017_64" --build "C:/qtwebkit/build/" --os windows
