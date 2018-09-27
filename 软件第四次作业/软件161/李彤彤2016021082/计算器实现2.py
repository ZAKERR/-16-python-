choice = int(input('选择运算：\n1、相加\n2、相减\n3、相乘\n4、相除\n请输入您的选择（1/2/3/4）:'))

num1 = int(input('请输入第一个数：'))

num2 = int(input('请输入第二个数：'))

if choice == 1:
    
     print('{} + {} = {}'.format(num1, num2, num1+num2))

elif choice == 2:

    print('{} + {} = {}'.format(num1, num2, num1-num2))

elif choice == 3:

    print('{} * {} = {}'.format(num1, num2, num1*num2))

elif choice == 4:

    print('{} / {} = {}'.format(num1, num2, num1/num2))

else:
    print('非法输入')


