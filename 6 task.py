#  Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
#  но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(args):
    # text = input('Введите текст: ')
    return (args.capitalize())

print(int_func('test text'))