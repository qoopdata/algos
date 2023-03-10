# Бинарный поиск <=> Binary Search

---

## Описание

Получаем на вход *отсортированный* список элементов и элемент, который нужно найти в этом списке.
Если он найден -> возвращаем позицию этого элемента в списке.
Иначе -> возвращаем `null`.

## Принцип работы

Играем в игру угадай число от 1 до 100. При каждой попытке мы получаем в ответ **"мало"**, **"много"** или **"угадал"**.
Самый простой вариант, начать перебирать все числа по порядку: 1, 2, 3, 4... это займет очень много времени, даже если крайнее число 100, как в нашем случае.
Такой перебор называется *методом полного перебора* или по-простому *bruteforce*. Его сложность можно оценить в `O(N)`, где N - количество перебираемых элементов.
Используя *метод (алгоритм) бинарного поиска*, мы можем сократить наши страдания до **7 попыток** при числах от 1 до 100.
Теперь, мы загадываем не случайное или порядковое число, а мы *начинаем с половины (середины диапазона)* и сразу же исключаем **половину оставшихся чисел**!
Каждый раз, когда мы говорим число, нам нужно делить оставшийся диапазон чисел на половину и говорить именно эту половину.
В конце концов, худшая из возможных ситуаций - *7 попыток угадать*. Сложность уменьшилась до `O(log₂N)`.

## Задания

Дан отсортированный список из 128 имен. Нам нужно найти в нем одно применяя метод бинарного поиска.
Какое количество проверок нам понадобиться чтобы найти это имя в худшем случае?
Ответ: *7 проверок*.
Пояснение: сложность бинарого поиска - `O(log₂N)`, отсюда и найдем ответ, подставив вместо `N` - 128, то есть кол-во имен.
