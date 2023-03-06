from typing import List



def custom_len(arr: List[int]) -> int:
    if not arr:
        return 0
    else:
        return 1 + custom_len(arr[1:])


if __name__ == "__main__":
    print("Узнаем количество элементов массива!")
    arr = []
    while True:
        num = input("Введите элемент: ")
        if num != "stop":
            arr.append(int(num))
        else:
            break
    print(f"Количество элементов в указанном массиве: {custom_len(arr)}")
