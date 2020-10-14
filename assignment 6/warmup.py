
# functions with arguments
"""
def a(x,y):
    answer = x+y
    print(answer)
    return answer

answer = a(7,2)
print(answer)
"""

"""
def a(q):
    print(q)

def b(q):
    return q

def c(q):
    print(q)
    return q

c(5)
"""

# trace the output
"""
def f1(a):
    print("f1", a)
    f2(a)
    print("f1", a)

def f2(a):
    print("f2", a)
    a = f3(a)      # a is a local variable
    print("f2", a)

def f3(a):
    print("f3", a)
    a += 1
    print("f3", a)
    return a       # return has to have variable waiting to catch it

a = 5
print("main", a)
f1(a)
print("main", a)

# output

main 5
f1 5
f2 5
f3 5
f3 6
f2 6
f1 5
main 5
"""


def square(w):
    for i in range(w):
        print("*" * w)

square(5)
