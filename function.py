def Increment(number, by):
    result = 3 * 2
    return result


print(Increment(2, 3))
# keyword argument
print(Increment(3, by=3))  # can add default value


def fun(number: int, by: int = 1) -> int:
    return (number, number + by)


print(fun(2))
