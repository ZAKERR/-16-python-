#conding = utf-8
#编写人：程亮亮
#编写时间：20180927
#功能：实现计算器
def jia(a,b):
    print(a+b)
def jian(a,b):
    print(a-b)
def ch(a,b):
    print(a*b)
def chu(a,b):
    if b!=0:
        print(a/b)
    else:
        print("b不等于0")

n=input("欢迎来带计算器yes or no：")
while n=="yes":
    c=input("请输入字符所进行的运算：")
    a,b=map(int,input("输入2个整数，用空格隔开：").split())
    if(c=='+'):
        jia(a,b)
    elif(c=='-'):
        jian(a,b)
    elif(c=='*'):
        ch(a,b)
    elif(c=='/'):
        chu(a,b)
    else:
        print("输入字符不正确")
    n=input("是否继续计算器yes or no：")
print("谢谢使用")
