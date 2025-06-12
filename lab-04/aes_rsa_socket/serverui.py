import threading
import socket
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import queue

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

server_key = RSA.generate(2048)

clients = []
message_queue = queue.Queue()

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def handle_client(client_socket, client_address):
    message_queue.put(f"New connection from {client_address}")
    client_socket.send(server_key.publickey().export_key(format='PEM'))

    client_received_key = RSA.import_key(client_socket.recv(2048))

    aes_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)

    clients.append((client_socket, aes_key))

    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            message_queue.put(f"From {client_address}: {decrypted_message}")

            for client, key in clients:
                if client != client_socket:
                    encrypted = encrypt_message(key, decrypted_message)
                    client.send(encrypted)

            if decrypted_message == "exit":
                break
        except Exception as e:
            message_queue.put(f"Error with {client_address}: {e}")
            break

    clients.remove((client_socket, aes_key))
    client_socket.close()
    message_queue.put(f"Connection from {client_address} closed")

def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()

class ServerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES Encrypted Chat Server")

        self.log_area = ScrolledText(root, state='disabled', width=60, height=30)
        self.log_area.pack(padx=10, pady=10)

        self.update_log()

    def update_log(self):
        while not message_queue.empty():
            msg = message_queue.get()
            self.log_area['state'] = 'normal'
            self.log_area.insert(tk.END, msg + "\n")
            self.log_area['state'] = 'disabled'
            self.log_area.see(tk.END)
        self.root.after(100, self.update_log)

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerUI(root)

    threading.Thread(target=accept_clients, daemon=True).start()

    root.mainloop()
