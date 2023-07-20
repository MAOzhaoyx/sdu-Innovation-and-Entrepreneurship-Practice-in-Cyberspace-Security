import SM2
from SM3 import SM3
from random import randint
import time
def Sign(M,d,G,n):
    k=randint(1,n)
    R=SM2.ecc_multiply(hex(k)[2:],G)
    r=R[0]
    e=SM3(M)
    k_=SM2.findModInverse(k,n)
    s=k_*(int(e,16)+int(d,16)*int(r,16)) % n
    return r,hex(s)[2:]
def Verify(e,P,r,s,n,G):
    w=SM2.findModInverse(int(s,16),n)
    ew=hex(int(e,16)*w)[2:]
    rw=hex(int(r,16)*w)[2:]
    r2,s2=SM2.ecc_diff_add(SM2.ecc_multiply(ew,G),SM2.ecc_multiply(rw,P))
    if r2==r:
        print("验证成功")
        return True
def forge(n,G,P):
    u=randint(1,n)
    v=randint(1,n)
    r=SM2.ecc_diff_add(SM2.ecc_multiply(hex(u)[2:],G),SM2.ecc_multiply(hex(v)[2:],P))[0]
    e=int(r,16) * u *SM2.findModInverse(v,n) % n
    s=int(r,16) * SM2.findModInverse(v,n) % n

    return r, hex(s)[2:] ,hex(e)[2:]


Gx="421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D"
Gy="0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2"
n="8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7"
n=int(n,16)
d="1649AB77A00637BD5E2EFE283FBF353534AA7F7CB89463F208DDBC2920BB0DA0"    #私钥
G=[Gx,Gy]
P=SM2.ecc_multiply(d,G)

M="5361746f736869"           #"Satoshi"
M_hash=(SM3(M))
r,s,e=forge(n,G,P)
Verify(e, P, r, s, n, G)



