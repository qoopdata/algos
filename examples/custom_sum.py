from typing import List



def summarize(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + summarize(arr[1:])



if __name__ == "__main__":
    arr = [int(input("Введите число: ")) for i in range(0, int(input("Введите количество чисел массива: ")))]
    print(f"Результат: {summarize(arr)}")
