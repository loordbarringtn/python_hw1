food_exp: int = int(input("Сколько ты потратил на еду за сегодня? : "))
transport_exp: int = int(
    input("Сколько ты потратил на транспорт за сегодня? : "))
entertainment_exp: int = int(
    input("Сколько ты потратил на развлечения за сегодня? : "))
total_exp: int = food_exp + transport_exp + entertainment_exp
average_exp: float = total_exp / 3

print("Общие расходы за сегодня составили: ", total_exp)
print("Средние расходы за категорию составили: ", average_exp)
