# Menu
print('Test 3')
print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Devide')

# Input
op=float(input('Enter Choice(1-4): '))

if op==1:

    The_First_Number = float(input('The First Number '))
    The_Second_Number = float(input('The Second Number '))
    The_Third_Number = float(input('The Third Number '))
    Solution = The_First_Number+The_Second_Number+The_Third_Number
    print("Sum = ", Solution)

if op==2:

    The_First_Number = float(input('The First Number '))
    The_Second_Number = float(input('The Second Number '))
    The_Third_Number = float(input('The Third Number '))
    Solution = The_First_Number - The_Second_Number - The_Third_Number
    print("Difference = ", Solution)

if op==3:

    The_First_Number = float(input('The First Number '))
    The_Second_Number = float(input('The Second Number '))
    The_Third_Number = float(input('The Third Number '))

    if The_Third_Number > 0:
        Solution = The_First_Number * The_Second_Number * The_Third_Number
        print("Product = ", Solution)
    if The_Third_Number == 0:
        Solution = The_First_Number * The_Second_Number
        print("Product = ", Solution)

if op==4:

    The_First_Number = float(input('The First Number '))
    The_Second_Number = float(input('The Second Number '))
    The_Third_Number = float(input('The Third Number '))
    Solution = The_First_Number * The_Second_Number * The_Third_Number
    print("Quotient = ",Solution)
else:
    print('Invalid Input')