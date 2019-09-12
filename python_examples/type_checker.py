import inspect
from functools import wraps


def to_args(f, *args, **kwargs):
    signature_f = inspect.signature(f)
    bind_arguments = signature_f.bind(*args, **kwargs)
    return bind_arguments.arguments.values()


def check(*types):
    def my_decorator(checked_function):

        @wraps(checked_function)
        def g(*args, **kwargs):

            args_val = to_args(checked_function, *args, **kwargs)

            for arg, type_arg in zip(args_val, types):
                if not isinstance(arg, type_arg):
                    raise ValueError(f'{arg} is not instance of type {type_arg}')

            return checked_function(*args, **kwargs)

        return g

    return my_decorator


@check(list, int)
def list_multiply(lst, num):
    return type(lst)([x * num for x in lst])


def main():
    assert list_multiply([1, 2, 3], 2) == [2, 4, 6]

    try:
        list_multiply([1, 2, 3], '5')
    except ValueError as err:
        print(err)
    else:
        raise RuntimeError('Шеф, все пропало, всё пропало!')
    finally:
        pass

    try:
        list_multiply((1, 2, 3), '5')
    except ValueError as err:
        print(err)
    else:
        raise RuntimeError('Гипс снимают, клиент уезжает!')
    finally:
        pass

    class MyList(list):
        @staticmethod
        def random_function():
            return 0

    assert list_multiply(MyList([1, 2, 3]), 2) == MyList([2, 4, 6])


if __name__ == '__main__':
    main()
