import SM2
from SM3 import SM3
from random import randint
def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b
def findModInverse(a, m):   # a^(-1) mod m
    if gcd(a, m) != 1:
        return None
    u1,u2,u3 = 1, 0, a
    v1,v2,v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
def chr_to_int(chr):
    return int(chr,16)
def sm2_sign(M,n,p):
    d1=randint(1,n)
    d1_=findModInverse(d1,p)
    p1=SM2.ecc_multiply(hex(d1_)[2:],G)
    d2=randint(1,n)
    d2_=findModInverse(d2,p)
    lll=SM2.ecc_multiply(hex(d2_)[2:],p1)
    P=SM2.ecc_diff_sub(lll,G)
    #Z是双方标识符
    e=SM3(Z+M)
    k1=randint(1,n)
    Q1=SM2.ecc_multiply(hex(k1)[2:],G)
    k2=randint(1,n)
    k3=randint(1,n)
    Q2=SM2.ecc_multiply(hex(k2)[2:],G)
    x1,y1=SM2.ecc_diff_add(SM2.ecc_multiply(hex(k3)[2:],Q1),Q2)
    r=chr_to_int(x1) + chr_to_int(e) % n
    s2=d2*k3 %n
    s3=d2*(r+k2) % n
    s=((d1*k1)*s2 + d1 * s3 -r )% n
    if s!=0 and s != n-r:
        return hex(r)[2:],hex(s)[2:]


Gx="421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D"
Gy="0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2"
G=[Gx,Gy]
n="8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7"
p="8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3"     #模数
p=chr_to_int(p)
Z="1649AB77A00637BD5E2Eaaa83FBF353534AA7F7CB89463F208DDBC2920BB0DA0"
n=int(n,16)
M="202000460052"
print(sm2_sign(M, n, p))