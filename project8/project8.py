import time
from Crypto.Cipher import AES

password = b'1234567812345678' #秘钥，b就是表示为bytes类型
text = b'abcdefghijklmnhi' #需要加密的内容，bytes类型
aes = AES.new(password,AES.MODE_ECB) #创建一个aes对象
# AES.MODE_ECB 表示模式是ECB模式
t1=time.time()
en_text = aes.encrypt(text) #加密明文
print("密文：",en_text) #加密明文，bytes类型
den_text = aes.decrypt(en_text) # 解密密文
t2=time.time()
print("明文：",den_text)
print("时间：",t2-t1)
