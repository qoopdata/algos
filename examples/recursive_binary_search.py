from typing import List



def recursive_binary_search(arr: List[int], finder: int) -> bool:
    try:
        if arr[(len(arr) // 2)] > finder:
            return recursive_binary_search(arr[:(len(arr) // 2)], finder)
        elif arr[(len(arr) // 2)] < finder:
            return recursive_binary_search(arr[(len(arr) // 2):], finder)
        elif arr[(len(arr) // 2)] == finder:
            return True
    except Exception as _ex:
        return False



if __name__ == "__main__":
    print("Найдем, есть ли число в указанном диапазоне чисел!")
    finder = int(input("Укажите число для поиска: "))
    arr = [int(i) for i in input("Укажите числовой диапазон в виде `1-100`: ").split("-")]
    print("Число успешно найдено!") if recursive_binary_search(range(arr[0], arr[1] + 1), finder) else print("Число не найдено!")
