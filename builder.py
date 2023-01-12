import base64
import os

path = 'main.py'


def crypt(path):
    try:
        with open(path, 'rb') as t:
            text = t.read()

        text1 = text.decode('utf8').split('\r\n\r\n\r\n')[0].replace('\n', '')
        try:
            exec(text1)
        except Exception as e:
            print(e)
            exit()
        de = base64.b85encode(text)

        code = f"""{text1}
from base64 import b85decode
source = b85decode({de}).decode('utf8')
exec(source)
        """
        with open("cr."+path, 'w') as t2:
            t2.write(code)
        return True
    except Exception as e:
        print(e)
        return False


if crypt('main.py'):
    os.system('auto-py-to-exe.exe --config "build.json"')

    if os.path.exists('output\\cr.main.exe'):
        if os.path.exists('bot\\madnet.exe'):
            os.remove('bot\\madnet.exe')

        os.system('copy "output\\cr.main.exe" "bot\\madnet.exe"')
        if os.path.exists('output\\cr.main.exe'):
            os.remove('output\\cr.main.exe')
else:
    print('Error')