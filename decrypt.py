#decrypt

from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

enc_file = open("encrypted.enc")
enc_data = enc_file.read()
enc_file.close()

cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
plain_data = cfb_decipher.decrypt(enc_data)

output_file = open("output.jpg", "w")
output_file.write(plain_data)
output_file.close()