import socket

from Crypto.Cipher import AES

client = socket.socket()

def filereq():
	filename = input("\nenter the file name : ")
	client.send(filename.encode())
	enc_data = client.recv(2000)
	key = client.recv(1000)
	iv = client.recv(1000)
	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data)
	with open('output.jpg', 'wb') as output_file:
		output_file.write(plain_data)
	output_file.close()


def main():
	client.connect(('192.168.43.79',3393))
	while True:
		try:
			filereq()
		except KeyboardInterrupt:
			print("\nclosing connection...")
			client.close()
			break

if __name__ == "__main__":
	main()