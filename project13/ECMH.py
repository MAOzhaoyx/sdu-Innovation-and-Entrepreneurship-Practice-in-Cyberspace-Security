import SM2
from SM3 import SM3
from deduce import Qres


def chr_to_int(chr):
    return int(chr,16)

def ECMH(A,p):
    result=0
    for i in A:
        x=SM3(i)
        #print(x)
        y=Qres(chr_to_int(x),p)
        result=chr_to_int(x)+y % p
    return hex(result)[2:]

A0=["2020004"]
A=["2020004","60052"]
p="8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3"     #模数
p=chr_to_int(p)
print("A0:",ECMH(A0,p))
print("A:",ECMH(A,p))