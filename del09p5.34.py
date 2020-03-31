""""Matthew Bono I. De las Alas
    DATALOG Lab09
    MAR. 31, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

class CaesarCipher: #class for encryption and decryption
    def __init__(self, shift): # initialization
        encoder = [None] * 26 #array for encryption
        decoder = [None] * 26 #array for decryption
        for k in range(26): #sets the range
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
        self._forward = ''.join(encoder) #will store as string
        self._backward = ''.join(decoder) #fixed

    def encrypt(self, message): # function to return the encrypted string
        return self._transform(message, self._forward)

    def decrypt(self, secret): # function to return decrypted string given an encrypted secret
        return self._transform(secret, self._backward)

    def _transform(self, original, code): # function to transform given code string
        msg = list(original)
        for k in range(len(msg)):
            char = msg[k]

            if (char.isupper()):
                msg += chr((ord(char) + code - 65) % 26 + 65)  # encrypts upper case letters.

            else:
                msg += chr((ord(char) + code - 97) % 26 + 97) # Encrypt's lowercase characters

        return msg

# main program to test the class Caesarcipher
if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "Don Bosco Technical College,DATALGO"
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)