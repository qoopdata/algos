def get_factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)



if __name__ == "__main__":
    num = int(input("Введите число из которого вы хотите получить факториал: "))
    print(f"Результат: `{num}!` = {get_factorial(num)}")
