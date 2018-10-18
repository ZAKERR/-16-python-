print("请选择运算类型")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")
type=int(input())
a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
if type==1:
    print(a,"+",b,"=",(a+b))
elif type==2:
    print(a,"-",b,"=",(a-b))
elif type==3:
    print(a,"*",b,"=",(a * b))
elif tupe==4:
    print(a,"/",b,"=",(a/b))
else:
    print("运算类型错误")
