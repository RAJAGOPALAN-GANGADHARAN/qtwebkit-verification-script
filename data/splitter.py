import os

linux = set(open('Linux.txt', 'r').readlines())
mac = set(open('Mac.txt', 'r').readlines())
win = set(open('Windows.txt', 'r').readlines())

##{0,1,2,{0,1},{1,2},{0,2},{0,1,2}}

allcommon = list(linux & mac & win)
allcommon.sort()

with open("Common.txt", 'w') as f:
    print(''.join(allcommon), file=f, end='')
    

olinux = list(linux - (mac | win))
olinux.sort()
with open('OnlyLinux.txt', 'w') as f:
    print(''.join(olinux), file=f, end='')


omac = list(mac - (linux | win))
omac.sort()
with open('OnlyMac.txt', 'w') as f:
    print(''.join(omac), file=f, end='')


owin = list(win - (mac | linux))
owin.sort()
with open('Onlywin.txt', 'w') as f:
    print(''.join(owin), file=f, end='')


twoattime = list(linux & mac - (linux & mac & win))
twoattime.sort()
with open('Mac-Linux.txt', 'w') as f:
    print(''.join(twoattime), file=f, end='')


twoattime = list(linux & win - (linux & mac & win))
twoattime.sort()
with open('Win-Linux.txt', 'w') as f:
    print(''.join(twoattime), file=f, end='')


twoattime = list(win & mac - (linux & mac & win))
twoattime.sort()
with open('Mac-Win.txt', 'w') as f:
    print(''.join(twoattime), file=f, end='')

