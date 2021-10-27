'''Checking palindrome using deque'''
def Palcheck(str):
    l=[]
    for ch in str:
        l.append(ch)
    while (len(l)>1):
        if l.pop(0) == l.pop():
            pal = True
        else:
            pal =  False
    return pal




Palcheck('radar')
