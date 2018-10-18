def jia(a,b):
    return a+b

def jian(a,b):
    return a-b

def cheng(a,b):
    return a*b

def chu(a,b):
    if(b==0):
        print('除数不能为零')
        exit
    return a/b
while True:
    print('请输入你要算的式子')
    num1 = int((input('请输入第一个数字')))
    ch = input('输入符')
    num2 = int((input('请输入第二个数字')))
    if ch == '+':
        print(jia(num1,num2))
    elif ch == '-':
        print(jian(num1,num2))
    elif ch == '*':
        print(cheng(num1,num2))
    elif ch == '/':
        print(chu(num1,num2))
    else :
        print('运算符错误')
