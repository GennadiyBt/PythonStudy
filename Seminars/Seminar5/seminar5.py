quantity = int(input("Введите количество конфет: "))
min_sweets = 1
max_sweets = int(input("Введите максимальное количество конфет за ход: "))
if quantity%(max_sweets+1) == 0:
    user_take = int(input("Сделайте свой ход: "))
    quantity = quantity - user_take
    print(f"Бот взял {quantity%(max_sweets+1)} конфет(ы).")
    quantity = quantity - (quantity%(max_sweets+1))
else:   
    print(f"Бот взял {quantity%(max_sweets+1)} конфет(ы).")
    quantity = quantity - (quantity%(max_sweets+1))

while quantity != 0:
    print(f"Оставшееся количество перед вашим ходом {quantity}")
    user_take = int(input("Сделайте свой ход: "))
    quantity = quantity - user_take
    temp = quantity%(max_sweets+1)
    quantity = quantity - (quantity%(max_sweets+1))
    print(f"Бот взял {temp} конфет(ы).")
print("Вы проиграли!!! :(")
