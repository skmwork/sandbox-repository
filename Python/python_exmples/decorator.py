def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

def decorator_function2(func):
    def wrapper():
        print('Функция-обёртка 2!')
        print('Оборачиваемая функция:  {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки 2')
    return wrapper

@decorator_function2
@decorator_function
def hello_world():
    print('Hello world!')

hello_world()