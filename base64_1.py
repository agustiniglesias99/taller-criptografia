from base64 import *
encriptedKey = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decodedKey = bytes.fromhex(encriptedKey)
print(b64encode(decodedKey))