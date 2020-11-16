try:
    print(x)
except NameError:
    print("Variable x is not defined")
except Exception as ex:
    print(ex.__cause__)
    print("An exception occurred")

try:
    print("Hello")
except Exception as ex:
    print(ex)
    print("Something went wrong")
else:
    print("Nothing went wrong")
