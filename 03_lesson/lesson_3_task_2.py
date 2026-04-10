from smartphone import Smartphone

# Создаем пустой список для каталога
catalog = []

# Наполняем список пятью разными экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+79111234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79212345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79313456789"))
catalog.append(Smartphone("Google", "Pixel 8", "+79414567890"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79515678901"))


for phone in catalog:
    
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")