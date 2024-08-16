# creates first file
f = open("myfile2.txt", "w+")

lines = ["hello world\n", "i am in california\n",
          "and im cruising"]
# 
f.write("my daily journal\n")
f.writelines(lines)
print(f.read())
f.close()

# creates second file
f2 = open("diary.txt", "w+")
print("here is my diary")

diary= ["dear diary,\n",
        "my heart has been broken by my crush\n",
        "i am sad today!!!!!\n"]

f2.writelines(diary)
print(f2.read())
f2.close()


# creates third file
print("this is my third diary")
f3 = open("diary3.txt", "a+")
f3.write("dear diary\n")
# f3.writelines(["i am healed from my heartbreak\n",
#               "i have gotten a new crush\n"])
f3.writelines(["thank you for listening to my rants"])
print(f3.read())
f3.close()





