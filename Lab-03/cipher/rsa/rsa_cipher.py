import os
import rsa

class RSACipher:
    def __init__(self):
        
        key_dir = os.path.join(os.path.dirname(__file__), "keys")
        os.makedirs(key_dir, exist_ok=True)

        self.private_key_path = os.path.join(key_dir, "private.pem")
        self.public_key_path = os.path.join(key_dir, "public.pem")

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(2048)
        with open(self.public_key_path, "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
        with open(self.private_key_path, "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

    def load_keys(self):
        with open(self.private_key_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        with open(self.public_key_path, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        return private_key, public_key

    def encrypt(self, message, key):
        if isinstance(message, str):
            message = message.encode()
        return rsa.encrypt(message, key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode()

    def sign(self, message, private_key):
        return rsa.sign(message.encode(), private_key, "SHA-256")

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode(), signature, public_key)
            return True
        except rsa.VerificationError:
            return False