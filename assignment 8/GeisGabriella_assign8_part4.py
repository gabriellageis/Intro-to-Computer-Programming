"""
Gabriella Geis
21 November, 2019
Section 002
Assignment 8 - Problem 4
"""

# 1. "listlen"
def listlen(mylist):
    length = 0
    for i in mylist:
        length += 1
    return length

# 2. "listmax"
def listmax(mylist):
    largest = 0
    if listlen(mylist) == 0:
            return None
    else:
        for i in range(listlen(mylist)):
            if mylist[i] > largest:
                largest = mylist[i]
    return largest

# 3. "listcopy"
def listcopy(mylist):
    copy = [] + mylist
    return copy

# 4. "listappend"
def listappend(mylist, x):
    copy = mylist + [x]
    return copy

# 5. "listinsert"
def listinsert(mylist, integer, data):
    copy = []
    for i in range(listlen(mylist)):
        if i == integer:
            copy += [data]
            copy += [mylist[i]]
        else:
            copy += [mylist[i]]
    return copy

# 6. "listremove"
def listremove(mylist, data):
    copy = []
    for i in range(listlen(mylist)):
        if mylist[i] != data:
            print(mylist[i])
            copy = listappend(copy, mylist[i])
    return copy

# 7. "listreverse"
def listreverse(mylist):
    copy = []
    for i in range(listlen(mylist)):
        copy = [mylist[i]] + copy
    return copy


