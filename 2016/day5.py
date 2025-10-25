# Advent of Code 2016 - Day 5
import hashlib

doorID = "ffykfhsq"
#doorID = "abc"
integer = 0
password = ""

print("Please wait for hashing to complete ...")
while len(password) != 8:
    door = doorID + str(integer)
    result = hashlib.md5(door.encode())
    zeros = result.hexdigest()
    if "00000" == zeros[:5]:
        password += str(zeros[5])
    integer += 1

print(f"The password for Part 1 = {password}")
