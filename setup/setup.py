import os

print("kakishpad setup v1.0")
print("this script will install dependecies needed to run kakishpad")

if input("target dependecies:\nsimplejson\nwinaudio\npygame\nkeyboard\ncolorama\ntermcolor\nVB-AUDIO Voicemeeter 1.1.2.2\nContinue? (y/n): ") == "n":
	exit()

print("Notice! Voicemeeter is a program developed by VB-AUDIO. It is a separate program that i did not develop. Also i highly recommend supporting VB-AUDIO team by making a donation to them :)")

if input("Do you have VB-AUDIO Voicemeeter installed? (y/n): ") == "n":
	print("installing VB-AUDIO Voicemeeter")
	os.system("voicemeetersetup.exe -i -h")

os.system("pip install simplejson")
os.system("pip install winaudio")
os.system("pip install pygame-ce")
os.system("pip install keyboard")
os.system("pip install colorama")
os.system("pip install termcolor")

print("Remember to set VB-AUDIO Voicemeeter to launch on startup and set Primary mic source in VB-AUDIO Voicemeeter")
input("Install completed. You may need to restart your computer for VB-AUDIO Voicemeeter to work.")