import base64, os

path = 'main.py'


def crypt(path):
    try:
        with open(path, 'rb') as t:
            text = t.read()
        
        text1 = text.decode('utf8').split('\r\n\r\n\r\n')[0].replace('\n','')

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
