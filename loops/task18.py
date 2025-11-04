# TODO 18 : take integer input and output its binary value

# 8 bit value

num = int(input("ENter the number: "))


if num >= 128:
    num = num - 128
    print("1", end="")
else:
    print("0", end="")
if num >= 64:
    num -= 64
    print("1", end="")
else:
    print("0", end="")
if num >= 32:
    num -= 32
    print("1", end="")
else:
    print("0", end="")
if num >= 16:
    num -= 16
    print("1", end="")
else:
    print("0", end="")
if num >= 8:
    num -= 8
    print("1", end="")
else:
    print("0", end="")
if num >= 4:
    num -= 4
    print("1", end="")
else:
    print("0", end="")
if num >= 2:
    num -= 2
    print("1", end="")
else:
    print("0", end="")
if num >= 1:
    num -= 1
    print("1", end="")
else:
    print("0", end="")

print(" ")