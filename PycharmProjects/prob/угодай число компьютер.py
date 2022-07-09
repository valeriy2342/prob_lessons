import random


def main():
    number = input('Choose any preferable number 1..100.')
    print('Only "=", "<", ">", "exit" commands allowed.')
    print('You choose: {}'.format(number))

    c = random.randint(1, 100)
    print('Computer random number: {}'.format(c))
    count = 0
    last_larger = -1
    last_lower = -1

    while True:
        count += 1
        print()
        # print('last_lower: {}, last_larger: {}'.format(last_lower, last_larger))

        inp = input('Step {}. {} ??: '.format(count, c))
        if inp == 'exit':
            print('Good bye!')
            break
        elif inp == '>':
            last_lower = c
            if last_larger == -1:
                c = c + (100 - c) // 2
            else:
                c = last_larger - (last_larger - last_lower) // 2

        elif inp == '<':
            last_larger = c
            if last_lower == -1:
                c = c // 2
            else:
                c = last_larger - (last_larger - last_lower) // 2

        elif inp == '=':
            print('I Did it for {} steps! Whooooooo!!!'.format(count))
            break
        else:
            print('Only "=", "<", ">", "exit" commands allowed.')


if __name__ == '__main__':
    main()