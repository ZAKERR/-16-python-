#������
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


x=input("���������֣�")
y=input("���������֣�")
str1=input("�������������")
x=int(x)
y=int(y)
print(x,str1,y,"����",calculation(x,y,str1))