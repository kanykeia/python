# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4_new.txt','w', encoding='UTF-8') as new_file:
    with open('text_4.txt','r', encoding='UTF-8') as file:
        new_file.writelines([line.replace(line.split()[0], num_dict.get(line.split()[0])) for line in file])
print('Перевод записан на файл text_4_new.txt')

