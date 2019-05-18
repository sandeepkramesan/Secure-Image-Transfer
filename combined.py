#combined

#with open(path, encoding="utf8", errors='ignore') as f:

#encrypt

from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
with open('./input.jpg', 'rb') as input_file:
    input_data = input_file.read()
input_file.close()

cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
enc_data = cfb_cipher.encrypt(input_data)

with open('encrypted.enc', 'wb') as enc_file:
    enc_file.write(enc_data)
enc_file.close()

#decrypt

with open('./encrypted.enc', 'rb') as enc_file2:
    enc_data2 = enc_file2.read()
enc_file2.close()

cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
plain_data = cfb_decipher.decrypt(enc_data2)

with open('output.jpg', 'wb') as output_file:
    output_file.write(plain_data)
output_file.close()