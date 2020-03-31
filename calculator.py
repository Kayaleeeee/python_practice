def calculator():
    while True:
        operation = int(input(
            'Please select \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Division \n\n Selct number from 1 to 4: '))

        if operation == 1:
            print('You Chose add cal')
            firstNum = int(input('Please input first number to add: '))
            secondNum = int(input('Please input second number to add: '))
            result = firstNum + secondNum
            print('The result is \n %f' % result)

        if operation == 2:
            print('You chose subtraction cal')
            firstNum = int(input('Please input first number: '))
            secondNum = int(input('Please input second number: '))
            result = firstNum - secondNum
            print('The result is \n %f' % result)

        if operation == 3:
            print('You chose multiplication cal')
            firstNum = int(input('Please input first number: '))
            secondNum = int(input('Please input second number: '))
            result = firstNum * secondNum
            print('The result is \n %f' % result)

        if operation == 4:
            print('You chose division cal')
            firstNum = int(input('Please input first number : '))
            secondNum = int(input('Please input second number : '))
            result = firstNum / secondNum
            print('The result is \n %f' % result)

        else:
            print("Please Select number from 1 to 4"
                  )


calculator()
