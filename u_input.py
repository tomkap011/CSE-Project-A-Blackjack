def isint(x):
    isint = True
    try:
        int(x)
    except:
        isint = False
    finally:
        return isint


def boolean(output_true=None, output_false=None, question=None):
    """
    output_true : the option for returning True
    output_false : the option for returning False
    question : The text added before the input
    """
    i = ''
    # if blank setting variables to defaults up defaults
    if output_true is None:
        output_true = 'y'
    if output_false is None:
        output_false = 'n'
    if question is None:
        question = ()
    # printing the requested question if it exists
    else:
        print(question)
    # getting user input and verifying that it is valid
    while i not in [output_true, output_false]:
        i = input(f'({output_true}/{output_false})_?')
    # sorting
    if i == output_true:
        return True
    elif i == output_false:
        return False


def number_only(*question):
    i = ''
    while not i.isdigit():
        i = input(f'{str(*question)}_?')

    return int(i)


def alpha_only(*question):
    i = '1'
    while not i.isalpha():
        i = input(f'{str(*question)}_?')
    return i


def postive_int_only(*question):
    i = ''
    loop = True
    while loop:
        try:
            int(i)
            if int(i) < int(0):
                sodas = 0 / 5
            else:
                break
        except:
            pass
        i = input(f'{str(*question)}_?')
    return int(i)


def yes_or_no(*question):
    i = ()
    while i not in ['y', 'n']:
        i = input(f'{str(*question)}(y/n)_?')
    # sorting
    if i.lower() == 'y':
        return True
    elif i.lower() == 'n':
        return False
