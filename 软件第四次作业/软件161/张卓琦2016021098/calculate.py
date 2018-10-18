#计算器的实现
def operation(a,b,str):
    if str == '+':
        return a+b
    elif str == '-':
        return a-b
    elif str == '*':
        return a*b
    elif str == '/':
        if b == 0:
            print('error')
            exit()
        return a/b

a = input('please input a number: ')
b = input('please input a number: ')
a = int(a)
b = int(b)
str = input('please input the operation: ')
print(a,b,str,"=",operation(a,b,str))


