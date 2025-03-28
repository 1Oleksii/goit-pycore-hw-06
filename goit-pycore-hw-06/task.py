# Імпортую необхідні бібліотеки для роботи з колекціями та регулярними виразами
from collections import UserDict
import re

class Field:
    # Створюю базовий клас для зберігання значень полів
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # Перетворюю значення поля на рядок для виведення
        return str(self.value)

class Name(Field):
    # Створюю клас для зберігання імені контакту
    def __init__(self, value):
        # Роблю перевірку, що ім'я не є порожнім рядком
        if not value or not isinstance(value, str):
            raise ValueError("Ім'я має бути непорожнім рядком")
        super().__init__(value)

class Phone(Field):
    # Створюю клас для зберігання та перевірки номера телефону
    def __init__(self, value):
        # Роблю валідацію номера телефону (10 цифр)
        if not self.validate_phone(value):
            raise ValueError("Номер телефону повинен складатися з 10 цифр")
        super().__init__(value)

    def validate_phone(self, phone):
        # Перевіряю, що номер телефону складається з 10 цифр
        return isinstance(phone, str) and re.match(r'^\d{10}$', phone) is not None

class Record:
    def __init__(self, name):
        # Створюю запис з іменем та порожнім списком телефонів
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додаю новий телефон до списку
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        # Видаляю телефон зі списку
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Редагую телефон у списку
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Телефон {old_phone} не знайдено")

    def find_phone(self, phone):
        # Шукаю телефон у списку
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        # Створюю текстове представлення запису
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Додаю запис до книги контактів
        self.data[record.name.value] = record

    def find(self, name):
        # Шукаю запис за ім'ям
        return self.data.get(name)

    def delete(self, name):
        # Видаляю запис за ім'ям
        if name in self.data:
            del self.data[name]

def main():
    # Створюю нову адресну книгу
    book = AddressBook()

    # Створюю запис для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додаю запис John до адресної книги
    book.add_record(john_record)

    # Створюю та додаю новий запис для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виводжу всі записи у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходжу та редагую телефон для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Шукаю конкретний телефон у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видаляю запис Jane
    book.delete("Jane")

# Перевіряю, чи скрипт запускається безпосередньо
if __name__ == "__main__":
    main()