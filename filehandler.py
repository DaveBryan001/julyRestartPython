# file access modes
# r, r+, w, w+, a, a+

f = open("myfile.txt", "r+")
f.write("\ni have changed the text again")


# f.writelines()
# f.writeline()
# f.read()
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

