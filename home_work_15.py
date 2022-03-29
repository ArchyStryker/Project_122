# test_1
import string


class Human:

    default_name = "Archy"
    default_age = 32

    def __init__(self, name=default_name, age=default_age):
        self.name = str(name)
        self.age = int(age)
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name - {self.name}\nAge - {self.age}\nMoney - {self.__money}\nHouse - {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name - {Human.default_name}\nDefault age - {Human.default_age}")

    def earn_money(self, value: int):
        self.__money += value
        return self.__money

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money!")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


# test_2
class House:

    def __init__(self, area: int, price: int):
        self._area = area
        self._price = price

    def final_price(self, discount: int):
        return self._area * self._price - self._area * self._price * (discount / 100)


class SmallHouse(House):

    default_area = 40

    def __init__(self, price: int):
        super().__init__(SmallHouse.default_area, price)


class Alphabet:

    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def length(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    __letters_num = len(string.ascii_uppercase)

    def __init__(self, lang="En", letters=string.ascii_uppercase):
        super().__init__(lang, letters)

    def is_en_letter(self, letter: str):
        if letter.upper() in self.letters:
            message = "Letter into alphabet!"
        else:
            message = "Letter not into alphabet!"
        return message

    def length(self):
        return self.__letters_num

    def example(self):
        print("this text is an example of english!")


# --test case--
Human.default_info()
h = Human("Iliya", 25)
h.info()
h.earn_money(75)
h.info()

small_house = SmallHouse(500)
h.buy_house(small_house, 15)
h.earn_money(17000)
h.buy_house(small_house, 15)
h.info()

english = EngAlphabet()
print(english.letters)
print(english.length())
print(english.is_en_letter('F'))
print(english.is_en_letter('щ'))
english.example()
