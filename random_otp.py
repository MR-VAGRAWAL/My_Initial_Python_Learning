# Random OTP which starts with zero
import random
while True:
    computer = random.randint(1000,9999999999)
    computer = str(computer)
    for i in range(1 , len(computer)-4):
        if computer[i]=="0":
            print(computer[i:i+4])
            break
    break
else:
    print("This OTP dosenot contain 0")