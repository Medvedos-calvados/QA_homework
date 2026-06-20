from address import Address
from mailing import Mailing

sender_address = Address("190000", "Санкт-Петербург", "Невский проспект", "10", "5")

receiver_address = Address("101000", "Москва", "Зверская улица", "22", "14")


shipment = Mailing(
    to_address=receiver_address,
    from_address=sender_address,
    cost=350,
    track="RU123456789"
)

print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, {shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
    f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, {shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)