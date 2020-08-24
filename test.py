# import os
# for root, dirs, files in os.walk("."):
#     for f in files:
#         print(os.path.relpath(os.path.join(root, f), "."))

with open('data/linuxlist.txt','r') as f:
    linux = set(f.readlines())
    

with open('data/maclist.txt','r') as f:
    mac = set(f.readlines())

with open('data/winlist.txt', 'r') as f:
    windows = set(f.readlines())

common = list(set.intersection(windows, mac, linux))

common.sort()
# print(common,file=open('final.txt','w'))
with open('final.txt', 'w') as f:
    for x in common:
        print(x, file=f, end='')
        
with open('only_linux.txt', 'w') as f:
    winmac = (mac | windows)
    diff = list(linux - winmac)
    diff.sort()
    for x in diff:
        print(x, file=f, end='')
        
with open('only_windows.txt', 'w') as f:
    winmac = (mac | linux)
    diff = list(windows - winmac)
    diff.sort()
    for x in diff:
        print(x, file=f, end='')

with open('only_mac.txt', 'w') as f:
    winmac = (windows | linux)
    diff = list(mac - winmac)
    diff.sort()
    for x in diff:
        print(x, file=f, end='')
    
    
    
    
