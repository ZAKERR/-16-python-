soccer = []
x = input('please input a number:')
while True:
    soccer.append(float(x))
    '''if x < 0 and x > 100:
        print('the number is wrong')'''
    flag = input('Do you want to input another number?(yes/no)')
    if flag.lower() not in ('yes','no'):
            print('sorry,you just can input yes or no')
    elif flag.lower() == 'yes':
            x = input('please input a number:')
            soccer.append(float(x))
    elif flag.lower() == 'no':
            break
print(sum(soccer)/len(soccer))
    
    
    
