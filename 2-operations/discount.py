good_price: int = int(input("Введите цену товара: "))
discount_percent: int = int(input("Введите процент скидки: "))
discount_amount: float = good_price * (discount_percent / 100)

final_price: float = good_price - discount_amount
print("Цена товара со скидкой составляет: ", final_price)
