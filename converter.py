# Файл converter.py
# Автор: Шестериков А.Г.
# Вариант: 5
# Этот файл является частью проекта 'hello-engineer'

def run_converter():
    """Основная функция для запуска калькулятора систем счисления."""
    print("\nИнженерный калькулятор систем счисления")
    mode = input("Выберите исходную систему (dec, bin, hex): ").lower().strip()
    number_str = input("Введите число для конвертации: ").strip()

    if mode == "dec":
        try:
            dec_number = int(number_str)
            if dec_number < 0:
                print(
                    "Ошибка: введено отрицательное число. Поддерживаются только неотрицательные целые числа.")
                return
            print(f"Двоичное: {bin(dec_number)}")
            print(f"Шестнадцатеричное: {hex(dec_number)}")
        except ValueError:
            print("Ошибка: введено неверное десятичное число.")

    elif mode == "bin":
        # Убираем возможный префикс '0b', если пользователь его ввёл
        clean_number = number_str.replace('0b', '')
        if not clean_number:
            print("Ошибка: пустая строка.")
            return
        if not all(c in '01' for c in clean_number):
            print("Ошибка: введено неверное двоичное число (разрешены только 0 и 1).")
            return
        try:
            dec_number = int(clean_number, 2)
            print(f"Десятичное: {dec_number}")
            print(f"Шестнадцатеричное: {hex(dec_number)}")
        except ValueError:
            print("Ошибка: невозможно преобразовать число.")

    elif mode == "hex":
        # Убираем возможный префикс '0x'
        clean_number = number_str.replace('0x', '').lower()
        if not clean_number:
            print("Ошибка: пустая строка.")
            return
        valid_hex_chars = "0123456789abcdef"
        if not all(c in valid_hex_chars for c in clean_number):
            print("Ошибка: введено неверное шестнадцатеричное число.")
            return
        try:
            dec_number = int(clean_number, 16)
            print(f"Десятичное: {dec_number}")
            print(f"Двоичное: {bin(dec_number)}")
        except ValueError:
            print("Ошибка: невозможно преобразовать число.")

    else:
        print("Ошибка: выбран неверный режим. Доступные режимы: dec, bin, hex.")


if __name__ == "__main__":
    run_converter()
