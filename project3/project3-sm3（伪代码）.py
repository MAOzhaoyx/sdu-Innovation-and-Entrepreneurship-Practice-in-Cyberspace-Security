import struct
import time
import hashlib

def sm3_length_extension_attack(message, original_hash):

    # 获取原始消息的长度（以比特为单位）
    original_length = len(message) * 8

    # 构造填充数据
    padding = b'\x80' + b'\x00' * ((56 - (original_length + 1) % 64) % 64)
    length_bits = struct.pack('>Q', original_length)

    # 通过修改状态变量进行长度扩展攻击
    forged_message = message + padding + length_bits
    h = bytearray.fromhex(original_hash)

    # 创建一个新的SM3对象（假装hashlib库中有SM3算法......）
    sm3 = sm3()

    # 设置初始哈希值
    sm3._h = h

    # 更新哈希对象的内部状态
    sm3.update(forged_message)

    # 输出攻击后的哈希值
    forged_hash = sm3.hexdigest()
    print("Forged Hash: ", forged_hash)

# 示例用法
message = b'This is the original message'
original_hash = 'e4d909c290d0fb1ca068ffaddf22cbd0f5b0b2b5'
start_time = time.time()
sm3_length_extension_attack(message, original_hash)
end_time = time.time()
execution_time = end_time - start_time
print("sm3长度扩展攻击时间: ", execution_time, "秒")
