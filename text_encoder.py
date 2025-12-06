# text_encoder.py
# Автор: Шестериков А.Г.
# Вариант: 5 (дополнительное задание со звёздочкой)
# Скрипт преобразует каждую букву введённого слова в ASCII-коды (DEC, BIN, HEX)

def encode_text():
    word = input("Введите слово: ").strip()
    if not word:
        print("Ошибка: введена пустая строка.")
        return

    print(f"\nАнализ слова: '{word}'")
    print("-" * 40)
    print(f"{'Символ':<8} {'DEC':<6} {'BIN':<10} {'HEX'}")
    print("-" * 40)

    for char in word:
        dec = ord(char)
        bin_repr = bin(dec)
        hex_repr = hex(dec)
        print(f"'{char}'     {dec:<6} {bin_repr:<10} {hex_repr}")


if __name__ == "__main__":
    encode_text()
