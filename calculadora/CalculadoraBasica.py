
def calculate():
    number_1 = int(input())
    number_2 = int(input())
    operacao = input()
    if operacao == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operacao == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operacao == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operacao == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')
calculate()
