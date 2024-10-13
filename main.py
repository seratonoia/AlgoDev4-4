def main():
    numbers = []

    num1 = int(input('enter num: '))
    num2 = int(input('enter num:'))
    N = int(input('enter num: '))

    numbers.append(num1)
    numbers.append(num2)

    if N <= 2:
        print('This number sequence must be greater than 2!')
    else:
        for i in range(2, N):
            nextVal = num1 + num2
            numbers.append(nextVal)
            num1 = num2
            num2 = nextVal
    print (numbers)
    return numbers
if __name__ == '__main__':
    main()