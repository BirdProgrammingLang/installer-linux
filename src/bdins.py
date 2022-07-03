def unload(hd):
	from os import system
	system(f'tar -xzvf bird.tar.gz -C {hd}')
from os import system
print('Welcome to the linux Bird Installer!')
from pathlib import Path
hd = str(Path(input('Where should Bird be installed: ')).absolute())
def expanduser(a):
	import sys
	return sys.argv[1]
f = open(expanduser('~')+'/bddir.txt','w')
f.write(hd)
f.close()
unload(hd)
f = open(f'{expanduser("~")}/.bashrc','a')
f.write(f'export PATH="{hd}:$PATH"')
f.close()
c = input("Reboot now? Y/N")
if c == "Y":
	system('sudo reboot')
