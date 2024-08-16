# if number is divisible by 5 and greater than 200, skip the number
# if number is greater than 400 break loop

numbers= [10, 15, 275, 21, 355, 85, 100, 780, 66]

for item in numbers:
    if item > 200:
        break
    elif item > 400:
        continue
    
    elif item % 5 == 0:
        print(item)
