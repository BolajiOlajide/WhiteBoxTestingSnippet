def multiples(a, b):
    """This function checks if a number is a multiple of another."""
    if type(a) != int or type(b) != int:
        raise Exception('Values must be integers.')
    elif a == 0:
        raise Exception('0 is not valid.')
    elif a == b:
        raise Exception('Numbers should not be the same.')
    else:
        if b > a:
            check = b % a
            if not check:
                return True
            else:
                return False
        else:
            raise Exception("Error! {0} isn't greater than {1}."
                            .format(b, a))
