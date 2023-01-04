import base64

path = 'bot\\back-d.exe'

def to_text():
    with open(path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b85encode(binary_file_data)
    with open(path+'.cry', 'wb') as binary_file:
        binary_file_data = binary_file.write(base64_encoded_data)

def to_byte():
    with open(path+'.cry', 'rb') as binary_file:
        binary_file_data = base64.b85decode(binary_file.read())#.encode('utf-8'))

    with open('bot\\back-d.exe', 'wb') as binary_file:
        binary_file_data = binary_file.write(binary_file_data)

to_text()
# to_byte()