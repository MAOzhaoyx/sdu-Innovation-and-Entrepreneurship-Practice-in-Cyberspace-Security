import time
import hashlib
import random

def generate_message():
    message = ""
    for i in range(32):
        message += chr(random.randint(0, 255))
    return message

def birthday_attack():
    hash_table = {}
    while True:
        message = generate_message()
        digest = hashlib.md5(message.encode()).hexdigest()
        if digest in hash_table:
            collision_message = hash_table[digest]
            return message, collision_message
        else:
            hash_table[digest] = message

def measure_time(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    print("运行时间：{:.4f}秒".format(end_time - start_time))
    return result

collision_message, message = measure_time(birthday_attack)
print("碰撞消息1:", collision_message)
print("碰撞消息2:", message)


'''以上代码实现了简化的md5生日攻击。它主要通过生成随机的消息，并计算其哈希值，然后将哈希值和消息存储在一个哈希表中。如果发现两个不同的消息具有相同的哈希值（碰撞），则返回这两个消息作为结果。
函数generate_message()用于生成随机的消息，其长度为32字节。每个字符都是从0到255的随机整数转换而来。
函数birthday_attack()实施生日攻击。它使用一个哈希表hash_table来存储已经计算过的哈希值和消息。在每次生成新的消息后，它会计算哈希值，并检查这个哈希值是否已经在哈希表中。如果是，则找到了碰撞，返回当前的消息和与之碰撞的消息；否则，将当前消息和该哈希值存储在哈希表中。
measure_time()函数用于测量代码运行时间。它接受一个函数作为参数，并在函数执行前后记录时间，并输出运行时间。
最后，在主程序中调用measure_time()函数来执行生日攻击，并输出结果。'''