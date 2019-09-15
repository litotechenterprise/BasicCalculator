def cal():
    shutDown = False
    print("Welcome to the simple calculator")
    while shutDown == False:

        
        firstNum =int(input('Enter Your First Number:'))
        secNum = int(input('Enter Second Number:'))

        operation = input("""
        Enter an operation
              + for Addition,
             - for subtraction
             / for division
             * for muliplication
        """)

        if operation == '+':
            print('{} + {}'.format(firstNum,secNum))
            print(firstNum + secNum)
        elif operation == '-':
            print('{} - {}'.format(firstNum,secNum))
            print(firstNum - secNum)
        elif operation == '/':
            print('{} / {}'.format(firstNum,secNum))
            print(firstNum / secNum)
        elif operation == '*':
            print('{} * {}'.format(firstNum,secNum))
            print(firstNum * secNum)
        else: 
            print('Invalided entry')   

        repeat = input('Do you wish to continue? y/n')
        if repeat == 'n':
            print('Goodbye')
            shutDown = True
cal()