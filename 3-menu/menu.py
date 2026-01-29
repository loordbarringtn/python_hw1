food_category: str = input(
    "Введите категорию блюда: «напиток», «суп», «десерт» ")

match food_category:
    case "напиток":
        drink_name: str = input(
            "Введите название напитка: «чай», «кофе», «сок» ")
        print("Вы выбрали напиток:", drink_name)
    case "суп":
        soup_name: str = input(
            "Введите название супа: «борщ», «щи», «суп-пюре» ")
        print("Вы выбрали суп:", soup_name)
    case "десерт":
        dessert_name: str = input(
            "Введите название десерта: «торт», «мороженое», «фрукты» ")
        print("Вы выбрали десерт:", dessert_name)
    case _:
        print("Неизвестная категория:", food_category)
