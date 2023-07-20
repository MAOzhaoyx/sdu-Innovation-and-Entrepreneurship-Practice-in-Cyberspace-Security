from hashlib import md5,sha256
import os
import time
import binascii
def sha256_length_extension_attack(message, original_hash):
 secrets=os.urandom(15)
 m=b'admin'
 k1=sha256(secrets+m+m).hexdigest()
 print(k1)
 s=binascii.b2a_hex(message)
 key=s.decode('utf-8')
 #str_key = b'This is the original message'
 #hex_key=oath.encode(str_key)
 cipher=original_hash
 #'2ef7bde608ce5404e97d5f042f95f89f1c232871'
 s1=secrets+m+bytes.fromhex(key)
 k2=sha256(s1).hexdigest()
 print(k2)
 if cipher==k2:
    print("成功")

# 示例用法
message = b'This is the original message'
original_hash = '2ef7bde608ce5404e97d5f042f95f89f1c232871'
start_time = time.time()
sha256_length_extension_attack(message, original_hash)
end_time = time.time()
execution_time = end_time - start_time
print("SHA-256长度扩展攻击时间为: ", execution_time, " 秒")



