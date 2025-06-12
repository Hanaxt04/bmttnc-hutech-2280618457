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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_key = RSA.generate(2048)
server_public_key = RSA.import_key(client_socket.recv(2048))
client_socket.send(client_key.publickey().export_key(format='PEM'))
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

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

message_queue = queue.Queue()

def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            message_queue.put(decrypted_message)
            if decrypted_message == "exit":
                break
        except Exception as e:
            message_queue.put(f"Error receiving message: {e}")
            break

threading.Thread(target=receive_messages, daemon=True).start()

class ClientUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES Encrypted Chat Client")

        self.chat_area = ScrolledText(root, state='disabled', width=60, height=30)
        self.chat_area.pack(padx=10, pady=10)

        self.entry_message = tk.Entry(root, width=50)
        self.entry_message.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))
        self.entry_message.bind('<Return>', lambda event: self.send_message())

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=(0,10))

        self.exit_button = tk.Button(root, text="Exit", command=self.close)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=(0,10))

        self.update_chat()

    def update_chat(self):
        while not message_queue.empty():
            msg = message_queue.get()
            self.chat_area['state'] = 'normal'
            self.chat_area.insert(tk.END, f"Server: {msg}\n")
            self.chat_area['state'] = 'disabled'
            self.chat_area.see(tk.END)
        self.root.after(100, self.update_chat)

    def send_message(self):
        msg = self.entry_message.get()
        if msg:
            try:
                encrypted = encrypt_message(aes_key, msg)
                client_socket.send(encrypted)
                self.chat_area['state'] = 'normal'
                self.chat_area.insert(tk.END, f"You: {msg}\n")
                self.chat_area['state'] = 'disabled'
                self.chat_area.see(tk.END)
                self.entry_message.delete(0, tk.END)
                if msg == "exit":
                    self.close()
            except Exception as e:
                self.chat_area['state'] = 'normal'
                self.chat_area.insert(tk.END, f"Error sending message: {e}\n")
                self.chat_area['state'] = 'disabled'
                self.chat_area.see(tk.END)

    def close(self):
        try:
            client_socket.close()
        except:
            pass
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientUI(root)
    root.mainloop()
