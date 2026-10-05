
class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self) -> None:
        print(self.first_name)

    def print_last_name(self) -> None:
        print(self.last_name)

    def print_full_name(self) -> None:
        print(f"{self.first_name} {self.last_name}")
