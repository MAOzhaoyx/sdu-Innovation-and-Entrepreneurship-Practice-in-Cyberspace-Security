import SM2
from SM3 import SM3
from random import randint
def key_gen(n,p,G):
    d1=randint(1,n)
    d2=randint(1,n)
    d=SM2.findModInverse((d1*d2) % p,p) -1
    P=SM2.ecc_multiply(hex(d)[2:],G)
    return d1,d2,P,d
def two_p_encrypt(P,M,n,G):
    k=randint(1,n)
    k=hex(k)[2:]
    #k="2"
    #print(int(k,16))
    #print("G",G)
    C1=SM2.ecc_multiply(k,G)
    x2=SM2.ecc_multiply(k,P)[0]
    y2=SM2.ecc_multiply(k,P)[1]
    klen=len(M)*4
    t=SM2.KDF(x2+y2,klen,256)
    C2 = SM2.chr_xor(M, t)
    C3 = SM3(x2 + M + y2)
    C1 = C1[0] + C1[1]
    C = C1 + C2 + C3
    return C

def two_p_decrypt(d1,d2,C,p,klen):
    clen=len(C)
    p=SM2.chr_to_int(p)
    C1=C[:128]
    C1=[C1[:64],C1[64:]]
    C2=C[128:clen-64]
    C3=C[-64:]
    T1=SM2.findModInverse(d1,p)
    T1=SM2.ecc_multiply(hex(T1)[2:],C1)
    lll=hex(SM2.findModInverse(d2,p) % p)[2:]
    T2=SM2.ecc_multiply(lll,T1)
    d = SM2.findModInverse((d1 * d2) % p, p) - 1
    x2,y2=SM2.ecc_multiply(hex(d),C1)
    t=SM2.KDF(x2+y2,klen,256)
    M=SM2.chr_xor(C2,t)
    u=SM3(x2+M+y2)
    if u==C3:
        return M

Gx="421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D"
Gy="0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2"
n="8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7"
n=SM2.chr_to_int(n)
p="8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3"
G=[Gx,Gy]

M="202000460052"
klen=len(M)*4
d1,d2,P,d=key_gen(n,SM2.chr_to_int(p),G)
cipher=two_p_encrypt(P,M,n,G)
print("cipher:",cipher)
print("解密明文",two_p_decrypt(d1,d2,cipher,p,klen))













