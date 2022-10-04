def repeat(some_string, number):
    """
    Return some_string repeated number times.

    If n is negative, return the empty string.

    :param some_string: a string, of course
    :param number: an integer, possibly negative
    :precondition: some_string is a string
    :precondition: number is an integer which can be zero or negative
    :postcondition: multiples the string
    :return: a new string composed of some_string multiplied number times

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)

    >>> repeat('no', -2)

    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
