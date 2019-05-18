import socket
import os

from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

server = socket.socket()

def filedisp(client,addr):
	filename = client.recv(1000)
	print('filename:',filename.decode())
	print("\n")
	try:
		with open(filename,"rb") as input_file:
			input_data = input_file.read()
			input_file.close()
		cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
		enc_data = cfb_cipher.encrypt(input_data)
	
		with open("encrypted.enc", "wb") as enc_file:
			enc_file.write(enc_data)
			enc_file.close()
key iv

	except IOError:
		client.send(b'file does not exist!')
		print('file does not exist!\n')


def main():
	server.bind(('192.168.43.79',3393))
	server.listen(5)
	client,addr = server.accept()
	while True:
		try:
			filedisp(client,addr)
		except KeyboardInterrupt:
			print("\nclosing connection...")
			server.close()
			break

if __name__ == "__main__":
	main()
