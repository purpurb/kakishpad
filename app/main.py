import time
import simplejson
import keyboard
import pygame
from winsound import PlaySound, SND_PURGE, SND_FILENAME, SND_ASYNC
import subprocess
import os
from termcolor import colored
import colorama

colorama.init()

pygame.mixer.pre_init(devicename="Voicemeeter Input (VB-Audio Voicemeeter VAIO)")
pygame.mixer.init()

def play(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    PlaySound(file_path,SND_ASYNC)

def convert_files():
    sound_files = os.listdir("sounds/")
    ii = 0
    converted = False
    for item in sound_files:
        if item.endswith(".mp3"):
            subprocess.call(['ffmpeg/bin/ffmpeg.exe', '-i', os.getcwd()+"\\sounds\\"+item,
                  os.getcwd()+"\\sounds\\"+item+'.wav'])
            sound_files[ii] = item+".wav"
            converted = True

            os.remove("sounds/"+item)
        ii += 1

    print("converted files: "+str(sound_files))

    if converted:
        for i in range(64):
            print('"',end="")
        print(" ")
        print(colored("INFO: done file conversion to .wav format. Restarting program.","yellow"))
        os.system("python main.py")
        exit()

def add_sound(name,key,flag):
    for i in range(64):
        print('=',end="")
    print(" ")

    keyy = input("please enter key for the "+name+".\nyou can also enter key combination (e.g.: ctrl+v).\n: ").lower()

    with open("sounds.map", "a") as file:
        file.write("\n;\n")
        file.write("name="+name+'\n')
        file.write("key="+keyy+'\n')
        file.write("enabled=true\n")

def parse_soundmap():
    names_list = []
    key_maps = []
    flags = []

    with open("sounds.map", "r") as file:
        for line in file:
            line = line.strip()
            polufabrikat = line.rsplit('=', maxsplit=1)
            
            if polufabrikat[0] == "name":
                names_list.append(polufabrikat[-1])

            if polufabrikat[0] == "key":
                key_maps.append(polufabrikat[-1])

            if polufabrikat[0] == "enabled":
                value = False
                
                if polufabrikat[-1] == "true":
                    value = True
                if polufabrikat[-1] == "false":
                    value = False

                flags.append(value)
        
    return names_list, key_maps, flags

kakishpad_enabled = True

if __name__ == "__main__":
    press_count = 0

    convert_files()
    names_list, key_maps, flags = parse_soundmap()

    files_list = os.listdir("sounds/")

    files_set = set(files_list)
    names_set = set(names_list)

    for item in files_set.difference(names_set):
        add_sound(item,"None","true")

    names_list, key_maps, flags = parse_soundmap()

    print("names_list: "+str(names_list))
    print("key_maps: "+str(key_maps))
    print("flags: "+str(flags))

    for i in range(64):
        print('=',end="")
    print(" ")

    print(colored("welcome to kakishpad v1.2. press ctrl+alt+backspace to enable or disable kakishpad","magenta"))

    while True:
        i = 0
        read_key = keyboard.read_key()

        if read_key:        
            if press_count > 1:
                press_count = 0

            press_count += 1

            if press_count <= 2:
                if keyboard.is_pressed("ctrl+alt+backspace"):
                    if kakishpad_enabled == True:
                        kakishpad_enabled = False
                    else:
                        kakishpad_enabled = True

                if kakishpad_enabled:
                    if read_key == "delete":
                        pygame.mixer.music.stop()
                        PlaySound(None, SND_PURGE)
                        press_count = -1
                    else:
                        for name in names_list:
                            if keyboard.is_pressed(key_maps[i]) and flags[i] == True:
                                play("sounds/"+name)
                                print("play")
                            i += 1
