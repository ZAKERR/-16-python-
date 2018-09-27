#计算器
def calculation(x,y,str1):
    if str1=='+':
        return x+y
    elif str1=='-':
        return x-y
    elif str1=='*':
        return x*y
    elif str1=='/' :
        if y==0:
            print("error")
            exit()
        else:
            return x/y


x=input("请输入数字：")
y=input("请输入数字：")
str1=input("请输入操作符：")
x=int(x)
y=int(y)
print(x,str1,y,"等于",calculation(x,y,str1))
