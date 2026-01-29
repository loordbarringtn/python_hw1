food_category: str = input(
    "Введите категорию блюда: «напиток», «суп», «десерт» ")

match food_category:
    case "напиток":
        drink_name: str = input(
            "Введите название напитка: «чай», «кофе», «сок» ")
        print("Вы выбрали напиток:", drink_name)
        match drink_name:
            case "чай":
                price: int = 50
            case "кофе":
                price = 100
            case "сок":
                price = 80
            case _:
                price = 0
        print(f"Цена: {price} руб.")
    case "суп":
        soup_name: str = input(
            "Введите название супа: «борщ», «щи», «суп-пюре» ")
        print("Вы выбрали суп:", soup_name)
        match soup_name:
            case "борщ":
                price: int = 150
            case "щи":
                price = 140
            case "суп-пюре":
                price = 160
            case _:
                price = 0
        print(f"Цена: {price} руб.")
    case "десерт":
        dessert_name: str = input(
            "Введите название десерта: «торт», «мороженое», «фрукты» ")
        print("Вы выбрали десерт:", dessert_name)
        match dessert_name:
            case "торт":
                price: int = 300
            case "мороженое":
                price = 120
            case "фрукты":
                price = 200
            case _:
                price = 0
        print(f"Цена: {price} руб.")
    case _:
        print("Неизвестная категория:", food_category)
