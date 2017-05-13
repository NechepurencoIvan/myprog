from tkinter import *
import rsa
from rsa import *
(key_pub, key_private) = rsa.newkeys(512)


a = int(input())
b = int(input())
c = int(input())

key_pub = PublicKey(8429300119105627611820020154834122336950507623364666829045805313421611595921389330869211032628871733639648291452723589778413393745776595967250234809245341, 65537)
key_private = PrivateKey(8429300119105627611820020154834122336950507623364666829045805313421611595921389330869211032628871733639648291452723589778413393745776595967250234809245341, 65537,a, b,c)

print(key_private)
print(key_pub)

message = b'igrev_sergey@yandex.ru 89537469842!'

# шифруем
crypto = rsa.encrypt(message, key_pub)
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, key_private)
print(message)