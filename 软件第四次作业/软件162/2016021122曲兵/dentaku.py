def dentaku():
    suuji1 = float(input('Please enter a number: '))
    opereeta = input('Please enter a operator: ')
    suuji2 = float(input('Please enter another number: '))
    if opereeta == '+':
        print ("result: ",suuji1+suuji2)
    elif opereeta == '-':
        print ("result: ",suuji1-suuji2)
    elif opereeta == '*':
        print ("result: ",suuji1*suuji2)
    elif opereeta == '/':
        if suuji2 == 0:
            print ("The divisor can not be 0.")
        else:
            print ("result: ",suuji1/suuji2)
    else:
        print ("Unknown operator ")
        
dentaku()
