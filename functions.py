def arrayCheck(l1):
    c=0
    for i in range(0,len(l1)-2):
        if(l1[i]==1 and l1[i+1]==2 and l1[i+2]==3):
            c=1
    if(c==1):
         print("True")
    else:
        print("False")
def string_bits(string):
    my_string=""
    my_string+=string[0]
    for i in range(2,len(string),2):
        my_string+=string[i]
    return my_string
def end_other(st1,st2):
    if(st1.lower()==st2[-3:].lower()):
        print("True")
    elif(st2.lower()==st1[-3:].lower()):
        print("True")
    else:
        print("False")
def double_char(st):
    result=""
    for i in st:
        result+=2*i
    print(result)
def no_teen_sum(a,b,c):
    a=fix_teen(a)
    b=fix_teen(b)
    c=fix_teen(c)
    print(a+b+c)
def fix_teen(n):
    i=0
    if(n>=13 and n<=19):
        if(n==15):
            i=n
        elif(n==16):
            i==n
        else:
            i=0
    else:
        i=n
    return i
def count_evens(l):
    count=0
    for i in l:
        if(i%2==0):
            count+=1
    print(count)
count_evens([2,1,2,3,4])
count_evens([2,2,0])
count_evens([1,3,5])
