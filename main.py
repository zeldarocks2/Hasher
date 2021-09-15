import hashlib

userInput = input("Path to the file: ")
isoFile = open(userInput, 'rb')
print(hashlib.algorithms_guaranteed)
userInput2 = input("Enter your hash type here: ")
result = hashlib.new(userInput2)

while True:
    readIso = isoFile.read(1024)

    if readIso:
        result.update(readIso)
    else:
        hexHash = result.hexdigest()
        break

print("The hash value of the file is: ")
print(result.hexdigest())