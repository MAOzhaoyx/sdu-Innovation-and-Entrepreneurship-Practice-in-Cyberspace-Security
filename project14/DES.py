IP = [58, 50, 42, 34, 26, 18, 10, 2,     #64
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# 逆初始置换表
IPinv = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]
# 扩充置换表
E = [32, 1, 2, 3, 4, 5,
          4, 5, 6, 7, 8, 9,
          8, 9, 10, 11, 12, 13,
          12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21,
          20, 21, 22, 23, 24, 25,
          24, 25, 26, 27, 28, 29,
          28, 29, 30, 31, 32, 1]
# 置换选择1  C0表
C0 = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36]

# 置换选择1  D0表
D0 = [63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4]

# 轮数--左移次数
lefttable = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 置换选择2表
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,   #  48bit
           15, 6, 21, 10, 23, 19, 12, 4,
           26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40,
           51, 45, 33, 48, 44, 49, 39, 56,
           34, 53, 46, 42, 50, 36, 29, 32]



# S盒表
S_table = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# P表
Ptable = [16, 7, 20, 21, 29, 12, 28, 17,
          1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9,
          19, 13, 30, 6, 22, 11, 4, 25]
def P_display(s):     #S盒结束后传进来进行P表置换
    result=''
    for i in range(32):
     result+=s[Ptable[i]-1]
    return result

def E_extend(Ri):  #E表48位   Ri传入明文一半32bit
    result=''
    for i in range(48):
        result+=Ri[E[i]-1]
    return result

def PC_2display(key):  # 28+28  ->48bit
    result = ''
    # print(hex(int(key,2)))
    for i in range(48):
        result += key[PC_2[i] - 1]
    # print(result)
    return result

def IP_display(plaintext):
    result=''
    for i in range(64):
        result+=plaintext[IP[i]-1]
    return result
def IP_i(plaintext):
    result=''
    for i in range(64):
        result+=plaintext[IPinv[i]-1]
    return result

def leftShiftRound(str,k):    #k:左移位数
    length=len(str)
    result_left=str[k:length]+str[0:k]
    return result_left

def rightShiftRound(str,k):    #k:左移位数
    length=len(str)
    result_right=str[length-k:]+str[0:length-k]
    return result_right

def Key_generatr(key,i):  #key:当前密钥(str二进制)  i：当前轮数
    C1=''
    D1=''
    if i==0:
         for y in range(28):
             C1+=key[C0[y]-1]
             D1+=key[D0[y]-1]
         C1 = leftShiftRound(C1, lefttable[i])
         D1 = leftShiftRound(D1, lefttable[i])

    else:
        C1=key[:28]
        D1=key[28:]
       # print(hex(int(C1 + D1, 2)))
        C1=leftShiftRound(C1,lefttable[i])
        D1=leftShiftRound(D1,lefttable[i])

    return C1+D1

def deKey_generatr(key,i):  #key:当前密钥(str二进制)  i：当前轮数
    C1=''
    D1=''
    if i==0:
         for y in range(28):
             C1+=key[C0[y]-1]
             D1+=key[D0[y]-1]
         for z in range(16) :
           C1 = leftShiftRound(C1, lefttable[z])
           D1 = leftShiftRound(D1, lefttable[z])

    else:
        C1=key[:28]
        D1=key[28:]
       # print(hex(int(C1 + D1, 2)))
        C1=rightShiftRound(C1,lefttable[-i])
        D1=rightShiftRound(D1,lefttable[-i])

    return C1+D1

def S_box(zip):  #zip:E扩展后和R异或后进入S盒里压缩（48 bit）
    result=''
    for i in range(8):
        temp=zip[i*6:i*6+6]
        row=int(temp[0]+temp[5],2)         #S盒的行
        column=int(temp[1]+temp[2]+temp[3]+temp[4],2)     #S行的列
        temp=bin(S_table[i][row][column])
        temp = temp[2:]
        if len(temp)<4:
            temp ='0'*(4-len(temp))+temp
        result+=temp
    return result

def F_function(R,k):     #R:传进来的一半密文   k：该轮密钥(56bit)
    #print(k)
    k=PC_2display(k)
    #print('密钥:',hex(int(k,2)))
    plaintext=E_extend(R)    #32bit->48bit密文
    plaintext=int(plaintext,2) ^ int(k,2)      #异或
    plaintext=bin(plaintext)
    plaintext = plaintext[2:]
    if len(plaintext)<48:
        plaintext='0'*(48-len(plaintext)) + plaintext
    return P_display(S_box(plaintext))      #32bit f函数， 接下来要和L异或得到下一个的R

def DES(plaintext,key):
    plaintext=bin(int(plaintext,16))
    plaintext=plaintext[2:]
    if len(plaintext) < 64:
        plaintext='0'*(64-len(plaintext))+plaintext
    key=bin(int(key,16))
    key=key[2:]
    if len(key)<64:
        key='0'*(64-len(key))+key
    plaintext=IP_display(plaintext)
    Ltemp = plaintext[:32]
    Rtemp = plaintext[32:]
    Keytemp=key
    for i in range(16):
        Rttemp=Rtemp
        Keytemp=Key_generatr(Keytemp,i)
        #print(Keytemp)
        Rtemp=bin(int(F_function(Rtemp,Keytemp),2) ^ int(Ltemp,2))
        Ltemp=Rttemp
        Rtemp=Rtemp[2:]
        if len(Rtemp)<32:
            Rtemp='0'*(32-len(Rtemp))+Rtemp
        #print('每轮加密：',hex(int(Ltemp+Rtemp,2)))
    cipher=Rtemp+Ltemp
    return hex(int(IP_i(cipher),2))[2:]

def deDES(plaintext,key):
    plaintext=bin(int(plaintext,16))
    plaintext=plaintext[2:]
    if len(plaintext) < 64:
        plaintext='0'*(64-len(plaintext))+plaintext
    print(key)
    key=bin(int(key,16))
    key=key[2:]
    if len(key)<64:
        key='0'*(64-len(key))+key
    plaintext=IP_display(plaintext)
    Ltemp = plaintext[:32]
    Rtemp = plaintext[32:]
    Keytemp=key
    for i in range(16):
        Rttemp=Rtemp
        Keytemp=deKey_generatr(Keytemp,i)
        #print(Keytemp)
        Rtemp=bin(int(F_function(Rtemp,Keytemp),2) ^ int(Ltemp,2))
        Ltemp=Rttemp
        Rtemp=Rtemp[2:]
        if len(Rtemp)<32:
            Rtemp='0'*(32-len(Rtemp))+Rtemp
        #print('每轮加密：',hex(int(Ltemp+Rtemp,2)))
    cipher=Rtemp+Ltemp
    return hex(int(IP_i(cipher),2))[2:]

