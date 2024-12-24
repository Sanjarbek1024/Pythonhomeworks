# Question 1

def check(func):
    """This is a decorator function that checks if the denominator is zero"""
    def wrappers(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Denominator can't be zero!"
    return wrappers

@check
def div(a, b):
    """This function divides two numbers"""
    return a / b

print(div(6, 2))
print(div(6, 0))