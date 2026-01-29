x=int(input("Enter a Number: "))


def factorial(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result

print(f"Factorail of {x} is {factorial(x)}")    