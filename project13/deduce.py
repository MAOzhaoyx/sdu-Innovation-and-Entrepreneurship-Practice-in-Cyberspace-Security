import time

import SM2
from SM3 import SM3
from random import randint

def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1,u2,u3 = 1, 0, a
    v1,v2,v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
def Legendre(a,p):
    return pow(a, (p - 1) // 2, p)


def extract_2(n):
    t=0
    temp=n
    while(1):
       if temp%2 ==0:
           temp=temp//2
           t+=1
       else:
           s=n//(2**t)
           return t,s
def Qres(a,p):  #求解二次剩余
    a=a % p
    if Legendre(a,p):
        t,s=extract_2(p-1)
        i=t-1
        x_i=pow(a,(s+1)//2, p)
        w_i=(findModInverse(a,p)*x_i*x_i) % p
        temp=x_i
        temp2=w_i
        if i==0:
            return x_i
        for j in range(i-1,-1,-1):

            if pow(temp2,(2**j),p)==1:
                x_i_1=temp
                temp2 = (findModInverse(a, p) * x_i_1 * x_i_1) % p
            else:
                while(1):
                    b=randint(1,p)
                    if Legendre(b,p)==-1 or Legendre(b,p)==p-1:
                        break
                asd=(2**(t-i-1)) * s
                la=pow(b,asd ,p)
                x_i_1=(la * temp)  % p
                temp2 = (findModInverse(a, p) * x_i_1 * x_i_1) % p
            temp=x_i_1
        return temp
    else:
        return False

def Precompute(Z_list):  #
    return  SM3(Z_list[0]+Z_list[1]+Z_list[2]+Z_list[3]+Z_list[4]+Z_list[5]+Z_list[6]+Z_list[7])

def Sign(ecc,G,n,M,dA,Z):
    M_=Z+M
    e=SM3(M_)
    k=randint(1,int(n,16))
    kG=SM2.ecc_multiply(hex(k)[2:],G)   #坐标点,列表十六进制形式  椭圆曲线上的运算全为字符串,数据类型需要转化
    #print("kGx",int(kG[0],16))
    #print("kGy",int(kG[1],16))
    r=(int(e,16)+int(kG[0],16))  % int(n,16)
    if r==0 or r+k==int(n,16):
        Sign(ecc, G, n, M, dA, Z)
        return 0
    s=(findModInverse(1+int(dA,16),int(n,16)) * (k-r*int(dA,16))) % int(n,16)
    if s==0:
        Sign(ecc, G, n, M, dA, Z)
        return 0
    return [hex(r)[2:],hex(s)[2:]]
def get_pk_from_sign(ecc,n,M,sign,Z):
    r=int(sign[0],16)
    s=sign[1]
    #print("s:",s)
    n1 = int(n, 16)
    e=SM3(Z+M)
    kGx=(r-int(e,16))  % int(n,16)
    #print("kGx",kGx)
    a,b,p=ecc
    a=int(a,16)
    b=int(b,16)
    p=int(p,16)
    #print("p",p)
    temp=(kGx**3+a*kGx+b)  % p
    #print("二次剩余",temp)
    #print("传入的kGy**2",shenmi*shenmi %p)
    kGy=Qres(temp,p)
    print("kGy:",kGy)
    kGx=hex(kGx)[2:]
    kGy=hex(kGy)[2:]
    kG=[kGx,kGy]
    sG=SM2.ecc_multiply(s,G)
    #print("sG",sG)
    temp1=findModInverse(int(s,16)+r,n1)
    #print("temp1",temp1)
    temp2=SM2.ecc_diff_sub(kG,sG)
    #print("temp2", temp2)
    PA=SM2.ecc_multiply(hex(temp1)[2:],temp2)
    return PA


#n是基点G的阶
Gx="421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D"
Gy="0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2"
xA="421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D"
yA="0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2"
k="4C62EEFD6ECFC2B95B92FD6C3D9575148AFA17425546D49018E5388D49DD7B4F"
n="8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7"
a="787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498"
b="63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A"
p="8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3"     #模数60275702009245096385686171515219896416297121499402250955537857683885541941187
dA="1649AB77A00637BD5E2EFE283FBF353534AA7F7CB89463F208DDBC2920BB0DA0"       #58724923310756937240092846960887528428411685443607809329868213582531823290246
ENTLa="1649AB77A00637BD5E2Eaaa83FBF353534AA7F7CB89463F208DDBC2920BB0DA0"
IDa="1649AB7fff0637BD5E2EFE283FBF353534AA7F7CB89463F208DDBC2920BB0DA0"
Zlist=[ENTLa,IDa,a,b,Gx,Gy,xA,yA]
Z=Precompute(Zlist)
ecc=[a,b,p]  #确定一个椭圆曲线
G=[Gx,Gy]   #基点




















