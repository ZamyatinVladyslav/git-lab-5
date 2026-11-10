
import os
import math


def main():
    try:
        a = float(os.getenv("A", "1"))
        b = float(os.getenv("B", "0"))
        c = float(os.getenv("C", "0"))
    except ValueError:
        print("Помилка: коефіцієнти повинні бути числами.")
        return

    print(f"\nРівняння: {a}x² + ({b})x + ({c}) = 0")

    if a == 0:
        print("\nПомилка: коефіцієнт a не може дорівнювати нулю.")
        print("Рівняння не є квадратним.")
        return

    # Обчислення дискримінанта
    print("\nКРОК 1. Обчислення дискримінанта")
    print("Формула: D = b² - 4ac")

    d = b ** 2 - 4 * a * c

    print(f"D = ({b})² - 4 * ({a}) * ({c})")
    print(f"D = {d}")

    # Визначення кількості коренів
    print("\nКРОК 2. Визначення кількості коренів")

    if d > 0:
        print("Дискримінант додатний: рівняння має два корені.")

        sqrt_d = math.sqrt(d)

        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        print("\nКРОК 3. Обчислення коренів")
        print("Формула: x = (-b ± √D) / 2a")

        print(f"x1 = (-({b}) + √{d}) / (2 * {a})")
        print(f"x1 = {x1}")

        print(f"x2 = (-({b}) - √{d}) / (2 * {a})")
        print(f"x2 = {x2}")

        print("\nРЕЗУЛЬТАТ:")
        print(f"Перший корінь: x1 = {x1}")
        print(f"Другий корінь: x2 = {x2}")

    elif d == 0:
        print("Дискримінант дорівнює нулю: рівняння має один корінь.")

        x = -b / (2 * a)

        print("\nКРОК 3. Обчислення кореня")
        print("Формула: x = -b / 2a")

        print(f"x = -({b}) / (2 * {a})")
        print(f"x = {x}")

        print("\nРЕЗУЛЬТАТ:")
        print(f"Єдиний корінь: x = {x}")

    else:
        print("\nРЕЗУЛЬТАТ:")
        print("Дійсних коренів немає.")

    print("\n" + "=" * 45)
    print("Розв'язання завершено.")
    print("=" * 45)


if __name__ == "__main__":
    main()
