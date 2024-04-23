import sys
import random

def generate_unique_random_numbers(n):
    unique_numbers = set()
    while len(unique_numbers) < n:
        num = random.randint(-10, 1000)
        unique_numbers.add(num)
    
    return list(unique_numbers)


def question1():
    n = random.randint(1, 1000)
    m = random.randint(1, 1000)
    s = random.choice([1,2,3,5])
    print(n,m,s)
    pass

def question2():
    print(random.randint(-2**63,2**63 - 1))
    pass

def question3():
    print(random.randint(1,1000))
    pass

def question4():
    print(random.randint(1,1000000))
    pass

def question5():
    n = random.randint(1, 1000)
    print(n)
    for _ in range(n):
        print(random.choice([0,1]))
    pass

def question6():
    n = random.randint(1, 1000)
    m = random.randint(1, 1000)
    print(n,m)
    pass

def question7():
    n = random.randint(1, 1000)
    b = random.randint(1, n)
    print(n,b)
    for _ in range(n):
        print(random.randint(-1000,1000), end = ' ')
    print()
    pass

def question8():
    n = random.randint(1, 1000)
    print(n)
    for _ in range(n):
        print(random.randint(-1000,1000), end = ' ')
    print()
    pass
def question9():
    n = random.randint(1, 1000)
    print(n)
    unique_random_numbers = generate_unique_random_numbers(n)
    for num in unique_random_numbers:
        print(num, end=' ')
    print()
    pass


def question10():
    n = random.randint(1, 1000)
    print(n)
    for _ in range(n):
        print(random.randint(-1000,1000), end = ' ')
    print()
    pass


def question11():
    n = random.randint(1, 1000)
    print(n)
    for _ in range(n):
        print(random.choice([0,1]))
    pass

def question12():
    n = random.randint(1, 40585)
    print(n)
    pass

def main():
    functionDict = {1:question1, 2:question2, 3:question3, 4:question4, 5:question5, 6:question6, 7:question7, 8: question8,
                    9:question9, 10:question10, 11 : question11, 12:question12}
    i = int(sys.argv[1])
    # print(i)
    functionDict[i]()

if __name__ == "__main__":
    main()

