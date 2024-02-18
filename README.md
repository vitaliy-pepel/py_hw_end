## Погружение в Python
### Задание:

Напишите код, который получает на вход путь до директории на ПК. 
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога,
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.

### Решение

1. Запускаем файл script.py
2. Вводим путь до директории. Пример:
![Задание](/1.png)

Содержание директории:
![Задание](/2.png)

3. В результате работы программы собераем информацию о содержимом указанной директории и сохраняем ее в файл file_info.txt, а также логирование в файле file_info.log.

Содержание file_info.txt:

![Задание](/3.png)


Содержание file_info.log:

![Задание](/4.png)