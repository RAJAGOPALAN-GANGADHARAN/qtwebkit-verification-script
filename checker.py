import sys
from jinja2 import Environment, FileSystemLoader
import argparse

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

output = template.render(os=args.os,qt=args.qt,build=args.build,
    major=major,minor=minor,ver_patch=patch)

with open('out_final.txt','w') as f:
    for x in output:
        print(x,end='',file=f)


#python3 checker.py --version 5.14.1 --qt "C:/Qt/" --build "C:/qtwebkit/build/" --os linux