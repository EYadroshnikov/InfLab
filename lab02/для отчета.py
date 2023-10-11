while True:
    try:
        prev = int(input("Введите целое число: "))
        break
    except ValueError as ve:
        print(ve)

min_abs_dif = float('inf')

for i in range(9):
    while True:
        try:
            cur = int(input("Введите целое число: "))
            break
        except ValueError as ve:
            print(ve)

    cur_abs_dif = abs(cur - prev)
    if cur_abs_dif < min_abs_dif:
        min_abs_dif = cur_abs_dif

print(f'min: {min_abs_dif}')
