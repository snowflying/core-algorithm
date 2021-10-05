
def fabonacii_number(num):
    n1 = 0
    n2 = 1
    while n1 <= num:
        print(n1)
        n1, n2 = n2, n1+n2


def fabonacci(num):
    n1 = 0
    n2 = 1
    while n1 <= num:
        yield n1
        n1, n2 = n2, n1+n2


# fabonacii_number(10)
# print('-+' * 10)
# fabonacii_number(20)


for item in fabonacci(10):
    print(item)
