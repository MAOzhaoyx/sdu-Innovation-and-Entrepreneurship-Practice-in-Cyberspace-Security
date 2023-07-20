import time
import hashlib

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