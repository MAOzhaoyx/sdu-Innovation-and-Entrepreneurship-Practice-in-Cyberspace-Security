import DES
import SM2
import random

def PGP_encrypt(M):
    deskey=hex(random.randint(1,2**64))[2:]
    cipher=DES.DES(M,deskey)
    print("deskey:",deskey)
    pk=SM2.SM2_encrypt(deskey)
    print("cipher:",cipher)
    print("pk:",pk)
    return cipher,pk
def PGP_decrypt(pk,cipher,klen):
    deskey=SM2.SM2_decrypt(pk,klen)
    M=DES.deDES(cipher,deskey)
    print("deskey:",deskey)
    print("M:",M)

M="202000460052"  #sdu
klen=64
cipher,pk=PGP_encrypt(M)
PGP_decrypt(pk,cipher,klen)



