import statistics as st

def return_text(text):
    return text


print(return_text("Hello"))

def get_even(numbers):
    even_nos = [num for num in numbers if not num % 2 ]
    return even_nos

print(get_even([2,4,6,7,9,11]))

def mean(sample):
    return sum(sample) / len(sample)

print(mean([10,20,30,40,50]))

def display(text):
    print(text)

display("text")


def add(a,b):
    return a + b

print(add(10,30))

def doStats(data):
    return st.mean(data), st.median(data), st.mode(data)

data = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
print(doStats(data))

mean, median, mode = doStats(data)
print(mean, median, mode)

print(type(doStats(data)))

print(divmod(7,2))

i = 0
def counter():
    global i
    i += 1


counter()
print(i)

def getAbsNo(no):
    if no > 0:
        return no
    elif no < 0:
        return -no
    else:
        return 0

print(getAbsNo(12))
print(getAbsNo(-1))
print(getAbsNo(0))

def is_divisible(a, b):
     if not a % b:
         return True
     return False


print(is_divisible(4, 2))

def isBothAreEqual(a,b):
    return True if a and b else False

print(isBothAreEqual(1,1))
print(isBothAreEqual(1,0))


def deadCode(text):
    return text
    print(text)

print(deadCode("DEAD CODE"))

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit) 

for char in "STRING":
    print(char)