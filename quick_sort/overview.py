from typing import List



# реализация быстрой сортировки (quick sort), получаем на вход неотсортированный массив
def quick_sort(arr: List[int]) -> List[int]:

    # если длина массива меньше 2, то сортировать его нет смысла, ибо он и так отсортирован
    if len(arr) < 2:
        return arr

    # любой другой случай дает нам пройтись по этому куску условия
    else:

        # находим опорный элемент (к примеру первый из полученного массива)
        pivot = arr[0]

        # находим левую часть сортировки
        left = [i for i in arr[1:] if i <= pivot]

        # находим правую часть сортировки
        right = [i for i in arr[1:] if i > pivot]

        # возвращаем рекурсию на сортировку в порядке (левая часть - опорная точка - правая часть)
        return quick_sort(left) + [pivot] + quick_sort(right)



if __name__ == "__main__":
    print("Реализация быстрой сортировки (quick sort)!")
    arr = []
    while True:
        num = input("Введите число для добавления в массив: ")
        if num == "stop":
            break
        else:
            arr.append(int(num))
    print(f"Результат: {quick_sort(arr)}")
