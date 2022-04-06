#  Создать текстовый файл (не программно), сохранить в нём несколько строк,
#  выполнить подсчёт строк и слов в каждой строке.

with open('2_text.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f'Количество строк в файле: {len(lines)}')

    for i, line in enumerate(lines,1):
        line = line.split()
        l = len(line)
        print(f'Количество слов в строкe {i} - {l}')


