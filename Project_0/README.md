# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)

### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений,менее 20 попыток.

**Что практикуем**     
Учимся писать хороший код на python.

### Этапы работы над проектом  
1. Написали функцию которая выдает случайное рандомное число от 1 до 100.
2. Написали функцию которая сама себе загадывает и отгадывает это число.
3. Написали функцию которая проверяет 1000 раз и выводит за сколько попыток в среднем было угадано число.
4. Внесли изменения для того что бы функция находила число в среднем менее чем за 20 попыток.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Функция угадывает число в среднем за 6 попыток.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Задача была выполнена. Функция угадывает число за 6 попыток. весь диапазон чисел делиться на 2 и таким методом получаеться найти загаданое число намного быстрее. 

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами