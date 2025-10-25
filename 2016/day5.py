# Advent of Code 2016 - Day 5
import hashlib

doorID = "ffykfhsq"
#doorID = "abc"
integer = 0
password = ""

# Part 1
print("Please wait for Part 1 hashing to complete ...")
while len(password) != 8:
    door = doorID + str(integer)
    result = hashlib.md5(door.encode())
    zeros = result.hexdigest()
    if "00000" == zeros[:5]:
        password += str(zeros[5])
    integer += 1

print(f"The password for Part 1 = {password}")

# Part 2
integer = 0
newPassword = ""
collect = [[], [], [], [], [], [], [], []]
toFill = 8
print("Please wait for Part 2 hashing to complete")
while True:
    door = doorID + str(integer)
    result = hashlib.md5(door.encode())
    zeros = result.hexdigest()
    if "00000" == zeros[:5]:
        if zeros[5].isdigit():
            if int(zeros[5]) >= 0 and int(zeros[5]) < 8:
                index = int(zeros[5])
            if len(collect[index]) == 0:
                collect[index] = str(zeros[6])
                toFill -= 1
                if toFill == 0:
                    break
    integer += 1

for item in collect:
    newPassword = newPassword + item[0]

print(f"The password for Part 2 = {newPassword}")
