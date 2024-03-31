#using counting variable
num=int(input("Enter  any number"))
fcount=0
if num>1:
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    print('Prime' if fcount==2 else 'Not Prime')
else:
    print('Not Prime')
    
#Method II
num=int(input("Enter  any number"))
if num>1:
    for fa in range(2,num//2+1):
        if num%fa==0:
            print('Not Prime')
            break
    else:
        print('Prime Number')
else:
    print('Not Prime')
    
    
#Methon III
num=int(input("Enter  any number"))
if num>1:
    for fa in range(2,int(num**(0.5))+1):
        if num%fa==0:
            print('Not Prime')
            break
    else:
        print('Prime Number')
else:
    print('Not Prime')
    
    
#Using List comperihenstion
num=int(input("Enter number:"))
if num>1:
    print('Prime' if len([fa for fa in range(2,num//2+1) if num%fa==0])==0 else 'Not Prime')
else:
    print('Not Prime')

#using filter function
num=int(input('Enter any number:'))
if num>1:
    if len(list(filter(lambda fa:num%fa==0,range(1,num+1))))==2:
        print('Prime')
    else:
        print('Not Prime')
else:
    print('Not Prime')

#using recurstion
def fcount(num,fa=1):
    if fa>num:
        return 0
    return (1 if num%fa==0 else 0)+fcount(num,fa+1)
def prime(num):
    return fcount(num)==2
num=int(input('Enter any number:'))
if prime(num):
    print('Prime')
else:
    print('Not Prime')
    
