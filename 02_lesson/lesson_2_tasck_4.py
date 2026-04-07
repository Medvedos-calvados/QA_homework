def fizz_buzz():
    try:
        n = int(input("Введите число n: "))
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

fizz_buzz()