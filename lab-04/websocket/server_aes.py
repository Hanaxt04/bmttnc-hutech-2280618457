import tornado.ioloop
import tornado.web
import tornado.websocket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Khóa AES cố định (16 bytes cho AES-128)
AES_KEY = b'ThisIsA16ByteKey'

class AESWebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        print("New client connected")
        AESWebSocketHandler.clients.add(self)

    def on_close(self):
        print("Client disconnected")
        AESWebSocketHandler.clients.remove(self)

    def on_message(self, message):
        print(f"Received from client: {message}")

        # Mã hóa message bằng AES-CBC
        cipher = AES.new(AES_KEY, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

        # Gửi về client: iv + ciphertext, encode base64 để client dễ nhận dạng
        msg_to_send = base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
        self.write_message(msg_to_send)
        print(f"Sent encrypted message: {msg_to_send}")

def make_app():
    return tornado.web.Application([
        (r"/websocket", AESWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
