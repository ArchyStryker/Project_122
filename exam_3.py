# test_1
def check_number(card_number):
    if len(card_number) == 16:
        for i in card_number:
            if i.isdigit():
                pass
            else:
                return "Incorrect card number!"
    else:
        return "Incorrect card number!"

    def credit_card(card_number):
        four_digits = card_number[12: 16]
        return f"Card number: **** **** **** {four_digits}"

    return credit_card(card_number)


card = input("Enter your number of credit card (16-digits): ")


# test_2
def palindrome(word):
    if len(word) % 2 != 0:
        half_first = word[0:(len(word) // 2)]
        half_second = word[(len(word) // 2) + 1:]
    else:
        half_first = word[0:(len(word) // 2)]
        half_second = word[(len(word) // 2):]
    if half_first == half_second[::-1]:
        message = "Word is palindrome"
    else:
        message = "Word is not palindrome"

    return message


word = input("Enter some word: ")

if __name__ == "__main__":
    print(check_number(card))
    print(palindrome(word))


# test_3
class Tomato:

    __states = {1: "no ripe", 2: "about ripe", 3: "ripe"}
    i = 1

    def __init__(self, index: int, state=__states[i]):
        self._index = index
        self._state = state

    def grow(self):
        if self.i < 3:
            self.i += 1
            self._state = self.__states[self.i]
        else:
            self._state = self.__states[3]
            return self._state

    def is_ripe(self):
        if self._state == self.__states[3]:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, amount: int):
        self.tomatoes = [Tomato(i) for i in range(0, amount)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes = []
            return True


class Gardener:

    def __init__(self, name: str, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.give_away_all():
            return "Harvest is harvested"

    @staticmethod
    def knowledge_base():
        print("In order to grow a good crop of tomatoes: "
              "you need soil rich in mineral salts, "
              "a humid warm climate and bright sun.")


Gardener.knowledge_base()
plant_1 = TomatoBush(6)
plant_1.grow_all()
gardener = Gardener("Boris", plant_1)
print(gardener.harvest())
print(plant_1.all_are_ripe())
gardener.work()
print(plant_1.all_are_ripe())
print(gardener.harvest())
