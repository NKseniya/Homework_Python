
from smartphone import Smartphone

# Создаём список для каталога
catalog = []

# Добавляем пять разных экземпляров класса Smartphone
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79001112233"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79002223344"))
catalog.append(Smartphone("Google", "Pixel 8", "+79005556677"))

# Цикл, который печатает весь каталог в нужном формате
for phone in catalog:
    print(phone)
