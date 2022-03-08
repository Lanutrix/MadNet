import keyboard, time
# while 1:
#     try:
#         keyboard.press_and_release("space+shift+К+У+space")
#         break
#     except:
#         print("NO")
        # keyboard.press_and_release("shift+alt")
def output_keyboard(text):
        vvod=[]
        for i in range(len(text)):
                st=0
                ko=0
                if i=="<":
                        st=i
                elif i==">":
                        ko=i
                if st!=0:
                        vvod.append(i)
                if st!=0 and ko!=0:
                        vvod.append(text[st+1:ko-1])
                        st=0
                        ko=0
        keyboard.press_and_release("space")

        keyboard.press_and_release("space")

def keyb(text):
        keyboard.press_and_release("space")
        for i in text:
                if i == i.lower():
                      keyboard.press_and_release(i)
                else:
                      keyboard.press_and_release("shift+"+i)
        keyboard.press_and_release("space")

time.sleep(2)
# keyboard.press_and_release("shift+alt")
keyb("<shift><alt>TouYtP")
# print(ord("a"),ord("A"), ord("z"),ord("Z"))
# print(ord("а"),ord("А"), ord("я"),ord("Я"))