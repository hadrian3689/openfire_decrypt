from hashlib import sha1
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from binascii import unhexlify, hexlify
import sys

def hex2bytes(hex_str):
    return unhexlify(hex_str)

def bytes2hex(byte_data):
    return hexlify(byte_data).decode('utf-8').upper()

def main(argv):
    if len(argv) < 2:
        print("[-] Please specify the hex encoded encrypted password and the passwordKey")
        return

    key_param = sha1(argv[1].encode('utf-8')).digest()
    iv_bytes = hex2bytes(argv[0][:16])
    encrypted_string = hex2bytes(argv[0][16:])

    cipher = Blowfish.new(key_param, Blowfish.MODE_CBC, iv_bytes)
    decrypted = unpad(cipher.decrypt(encrypted_string), Blowfish.block_size)

    decrypted_string = bytes2hex(decrypted)

    print(f"\nDecoded Password: {decrypted.decode('utf-8')}\n\n(Hex Encoded Decrypted Password: {decrypted_string})")

if __name__ == "__main__":
    main(sys.argv[1:])
