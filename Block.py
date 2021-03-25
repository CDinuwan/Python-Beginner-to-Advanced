message = "global variable"


def greet():
    message = "Local variable"
    print(message)


greet()
print(message)
