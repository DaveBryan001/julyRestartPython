def errorHandle(n):
    try:
        value = 10 / 0
        return value
    except ZeroDivisionError:
        print("the number is not divisible by 0\ntry another number")


