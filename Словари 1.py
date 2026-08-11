def get_age_suffix(age: int) -> str:
    """Возвращает правильное окончание: год/года/лет"""
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        return "года"
    else:
        return "лет"


pets = {}

# Получаем данные от пользователя
pet_name = input("Введите имя питомца: ")
pet_species = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Заполняем словарь
pets[pet_name] = {
    "Вид питомца": pet_species,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

# Формируем строку с информацией, используя keys() и values()
pet_key = list(pets.keys())[0]          # имя питомца (ключ)
pet_data = list(pets.values())[0]       # словарь с данными о питомце

age_word = get_age_suffix(pet_data["Возраст питомца"])

result_string = (
    f"Это {pet_data['Вид питомца']} по кличке \"{pet_key}\". "
    f"Возраст питомца: {pet_data['Возраст питомца']} {age_word}. "
    f"Имя владельца: {pet_data['Имя владельца']}"
)

print(result_string)
