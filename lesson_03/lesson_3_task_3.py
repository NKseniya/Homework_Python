
from address import Address
from mailing import Mailing

# Создаём адрес отправителя
from_addr = Address("101000", "Москва", "ул. Пушкина", "д. 10", "кв. 5")

# Создаём адрес получателя
to_addr = Address("630000", "Новосибирск", "пр. Ленина", "д. 25", "кв. 12")

# Создаём отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=345.50,
    track="RU123456789RU"
)

# Распечатываем отправление — сработает __str__
print(mailing)
