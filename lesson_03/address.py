class Address:
    def __init__(
        self,
        index: str,
        city: str,
        street: str,
        house: str,
        apartment: str,
    ):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self) -> str:
        return (
            f"{self.index}, {self.city}, {self.street}, "
            f"{self.house} - {self.apartment}"
        )
