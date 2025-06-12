from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hasted_text = sha3(text)
    
    print("Chuỗi văn bản đã nhập là:", text.decode('utf-8'))
    print("Giá trị băm SHA3-256 là:", hasted_text.hex())
    
if __name__ == "__main__":
    main()