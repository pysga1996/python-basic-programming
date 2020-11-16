f1 = open("demo_file2.txt", "a")
f1.write("Now the file has more content!\n")
f1.close()

# open and read the file after the appending:
f1 = open("demo_file2.txt", "r")
print(f1.read())

f2 = open("demo_file3.txt", "w")
f2.write("Woops! I have deleted the content!")
# f2.write("Woops! I have deleted the content!")
f2.close()

# open and read the file after the appending:
f2 = open("demo_file3.txt", "r")
print(f2.read())
