import time

# 定义常量
IV = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 
      0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]

#常数Tj
def Tj(i):
    if i<16:
        return 0x79cc4519
    else:
        return 0x7a879d8a
    

def rotate_left(x, n):
  if n<=32:
      return ((x<<n) & 0xffffffff) | (x >> (32-n))
  else:
        return ((x<<n) & 0xffffffff) | (x << (n-32))

def FF(x, y, z, j):
    if 0 <= j <= 15:
        return x ^ y ^ z
    elif 16 <= j <= 63:
        return (x & y) | (x & z) | (y & z)


def GG(x, y, z, j):
    if 0 <= j <= 15:
        return x ^ y ^ z
    elif 16 <= j <= 63:
        return (x & y) | (~x & z)


def P0(X):
    return X ^ rotate_left(X, 9) ^ rotate_left(X, 17)


def P1(X):
    return X ^ rotate_left(X, 15) ^ rotate_left(X, 23)


def CF(V, Bi):
    W = [0] * 68
    W[0:16] = Bi[0:16]

    for i in range(16, 68):
        W[i] = P1(W[i - 16] ^ W[i - 9] ^ rotate_left(W[i - 3], 15)) ^ rotate_left(W[i - 13], 7) ^ W[i - 6]

    W1 = [0] * 64

    for i in range(0, 64):
        W1[i] = W[i] ^ W[i + 4]

    A, B, C, D, E, F, G, H = V

    for i in range(0, 64):
        SS1 = rotate_left(rotate_left(A, 12) + E + rotate_left(Tj(i), i), 7)
        SS2 = SS1 ^ rotate_left(A, 12)
        TT1 = FF(A, B, C, i) + D + SS2 + W1[i]
        TT2 = GG(E, F, G, i) + H + SS1 + W[i]

        D = C
        C = rotate_left(B, 9)
        B = A
        A = TT1
        H = G
        G = rotate_left(F, 19)
        F = E
        E = P0(TT2)

    V[0] ^= A
    V[1] ^= B
    V[2] ^= C
    V[3] ^= D
    V[4] ^= E
    V[5] ^= F
    V[6] ^= G
    V[7] ^= H

    return V


def sm3(message):
    message = bytearray(message, 'utf-8')
    length = len(message)
    groups = (length // 64) + (1 if length % 64 > 56 else 0) + 1

    message += b'\x80'
    message += b'\x00' * ((groups * 64 - 56 - length - 1) % 64)
    message += length.to_bytes(8, byteorder='big')

    V = IV.copy()

    for i in range(groups):
        Bi = message[i * 64: (i + 1) * 64]
        V = CF(V, Bi)

    return V


def hash_message(message):
    result = ''
    hashed = sm3(message)
    for h in hashed:
        result += format(h, '08x')
    return result


def get_execution_time(message):
    start_time = time.time()
    hash_message(message)
    end_time = time.time()
    execution_time = end_time - start_time
    print("代码运行时间：", execution_time, "秒")


# 测试
message = "Hello, World!"
print(hash_message("Hello, World!"))
get_execution_time(message)
