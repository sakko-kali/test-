


def square(a):
    return a**2

print(square(5))

def listsum(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(listsum(5,3,4,23,4342,324,214,3))
