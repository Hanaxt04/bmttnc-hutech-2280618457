import tornado.websocket
import asyncio
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

AES_KEY = b'ThisIsA16ByteKey'  # Phải giống server

class AESWebSocketClient:
    def __init__(self):
        self.connection = None

    async def connect(self):
        self.connection = await tornado.websocket.websocket_connect("ws://localhost:8888/websocket")
        print("Connected to server")

    async def send_message(self, message):
        if self.connection:
            await self.connection.write_message(message)

    async def receive_loop(self):
        while True:
            msg = await self.connection.read_message()
            if msg is None:
                print("Connection closed")
                break

            print(f"\nEncrypted message from server (base64): {msg}")
            try:
                encrypted_data = base64.b64decode(msg)
                iv = encrypted_data[:AES.block_size]
                ct = encrypted_data[AES.block_size:]

                cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
                plaintext = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
                print(f"Decrypted message: {plaintext}")
            except Exception as e:
                print(f"Failed to decrypt message: {e}")
            print("Enter message to send (type 'exit' to quit): ", end='', flush=True)

async def main():
    client = AESWebSocketClient()
    await client.connect()

    # Chạy receive_loop song song với input
    asyncio.create_task(client.receive_loop())

    while True:
        msg = await asyncio.get_event_loop().run_in_executor(None, input, "Enter message to send (type 'exit' to quit): ")
        if msg == "exit":
            break
        await client.send_message(msg)

if __name__ == "__main__":
    asyncio.run(main())
