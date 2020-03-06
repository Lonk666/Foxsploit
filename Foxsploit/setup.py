from os import system
from time import sleep
import urllib
from urllib.request import urlopen

def is_internet():
	try:
		urlopen('https://www.google.com', timeout=1)
		return True
		
	except urllib.error.URLError as Error:
		print(Error)
		return False
		
if is_internet():
	print("Internet is active")
else:
	quit("Internet is disconnected\nPlease turn on you're WiFi")
sleep(0.7)
"""///"""
#Install dependencies
"""///"""
system("clear")
print("Updating")
sleep(0.2)
system("apt-get update")
print("*****************************")
system("clear")
print("Installing python module > colorama")
system("pip3 install colorama")
print("*****************************")
system("clear")
print("Installing python module > pynput")
system("pip3 install pynput")
print("*****************************")
system("clear")
print("Installing python module > urlopen")
system("pip3 install urlopen")
print("*****************************")
system("clear")
print("Installing python module > urlopen")
system("pip3 install bottle")
print("*****************************")
system("clear")
print("[|]")
sleep(0.4)
system("clear")
print("[/]")
sleep(0.4)
system("clear")
print("[-]")
sleep(0.4)
system("clear")
print("[\]")
sleep(0.4)
system("clear")
print("[|]")
sleep(0.4)
system("clear")
print("Done !")
sleep(1)
