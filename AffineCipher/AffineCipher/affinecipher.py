from cryptography.fernet import Fernet

def generate_key():
    '''
    Generates a key and saves it.
    '''
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_doc:
        key_doc.write(key)

def load_key():
    '''
    Loads secret.key
    '''
    return open("secret.key", "rb").read()
    
def encrypt_message(message):
    '''
    Encrypts the message
    '''
    key = load_key()
    encrypted_message = message.encode()
    f = Fernet(key)
    encoded_message = f.encrypt(encrypted_message)

    print(encoded_message)

def decrypt_message(encrypted_message):
    '''
    Decrypts an encrypted message
    '''
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

# E = ["E", "e" , "Encrypt", "encrypt"] # Options for encrypt menu
# D = ["D", "d", "Decrypt", "decrypt"] # Options for decrypt menu
# Q = ["Q", "q", "Quit", "quit"] # Options for quit menu

generate_key()

while True:

    menu = input("Press E for Encrypt. Press D for Decrypt. Press Q for quit. ")

    if menu != "E" or "D" or "Q":
        continue
    
    if menu == "E":
        plaintext = input("Enter message to encrypt: ")

            if __name__ == "__main__":
                encrypt_message(plaintext)

    if menu == "D":
        ciphertext = input("Enter message to decrypt: ")
    
            if __name__ == "__main__":
                decrypt_message(ciphertext)

    if menu == "Q":
        break