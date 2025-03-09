import os

filepath = os.getcwd()

fullpath = os.path.join(filepath, "example.txt")

if os.path.exists(fullpath):
    print(f"{fullpath} exists")
else:
    print(f"{fullpath} doesn't exist")

#write to a file
file = open(fullpath, "w")
file.write("Helloooo")
file.close()

#read from a file
file = open(fullpath, "r")
content = file.read()
file.close()
print(content)

#append to file
with open("output.txt", "a") as file:
    file.write("\nHello World")


