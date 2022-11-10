import random
otp = random.randint(1000,9999)
print(otp)
for i in range(3,0,-1):
    user = int(input("Enter The Four Digit OTP : "))
    if user == otp:
        print("Congrats, Your OTP is Verified👍")
    else:
        print(f"Wrong OTP,You Have {i-1} chanches left🥺 ")