from typing import List
from re import match



def looker(arr: List[int], order: bool) -> int:
    
    # инициализируем цикл по списку
    for outer_idx in range(0, len(arr)):

        # инициализируем проверяющую переменную как равную первому элементу списка
        checker = arr[outer_idx]

        # инициализируем цикл по остатку списка
        for inner_idx in range(0, len(arr)):
            
            # если тип сортировки по убыванию то переходим к этому блоку условия
            if order:
                
                # если полученное число из массива больше проверочного числа, то меняем проверочное число на него
                if arr[inner_idx] > checker:
                    checker = arr[inner_idx]

            # если тип сортировки по возрастанию то переходим к этому блоку условия
            else:
                
                # если полученное число из массива меньше проверочного числа, то меняем проверочное число на него
                if arr[inner_idx] < checker:
                    checker = arr[inner_idx]

        # возвращаем минимальное или максимальное значение из полученного списка в зависимости от тип сортировки
        return checker


# реализация сортировки выбором (selection sort), получаем массив и bool в виде `True` - по убыванию и `False` - по возрастанию 
def selection_sort(arr: List[int], order: bool) -> List[int]:

    # инициализируем пустой итоговый список на возвращение
    result = []

    # инициализируем цикл по массиву
    for side in range(0, len(arr)):

        # переносим данные в поисковик максимального/минимального числа из списка
        adder = looker(arr, order)

        # добавляем полученное число в итоговый массив и убираем его из изначального массива
        result.append(adder)
        arr.remove(adder)

    # в итоге возвращаем итоговый массив отсортированный по условию заданному при получении bool значения в нашу функцию
    return result



if __name__ == "__main__":
    print("Отсортируем ваш массив при помощи сортировки выбором (selection sort)!")
    arr = []
    while True:
        adder = input("Введите число или `stop` для остановки введения чисел: ")
        if match(r"^-?\d+$", adder):
            arr.append(int(adder))
        elif adder == "stop":
            break
        else:
            raise Exception("Вы ввели неправильное значение для добавления в массив!")
    sort_type = input("Введите тип сортировки (0 - по убыванию, 1 - по возрастанию): ")
    if sort_type == "0":
        sort_type = True
    elif sort_type == "1":
        sort_type = False
    else:
        raise Exception("Вы ввели неправильное значение для типа сортировки!")

    result = selection_sort(arr, sort_type)
    print(f"Результат: {result}")
    if sorted(result, reverse=sort_type) == result:
        print("Тесты пройдены. Результат верный!")
    else:
        print("Ошибка! Результат неверный!")
