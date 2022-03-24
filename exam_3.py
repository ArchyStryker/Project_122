# # test_1
# def check_number(card_number):
#     if len(card_number) == 16:
#         for i in card_number:
#             if i.isdigit():
#                 pass
#             else:
#                 return "Incorrect card number!"
#     else:
#         return "Incorrect card number!"
#
#     def credit_card(card_number):
#         four_digits = card_number[12: 16]
#         return f"Card number: **** **** **** {four_digits}"
#
#     return credit_card(card_number)
#
#
# card = input("Enter your number of credit card (16-digits): ")
#
#
# # test_2
# def palindrome(word):
#     if len(word) % 2 != 0:
#         half_first = word[0:(len(word) // 2)]
#         half_second = word[(len(word) // 2) + 1:]
#     else:
#         half_first = word[0:(len(word) // 2)]
#         half_second = word[(len(word) // 2):]
#     if half_first == half_second[::-1]:
#         message = "Word is palindrome"
#     else:
#         message = "Word is not palindrome"
#
#     return message
#
#
# word = input("Enter some word: ")
#
# if __name__ == "__main__":
#     print(check_number(card))
#     print(palindrome(word))


# test_3
class Tomato:
    states = {1: "no ripe", 2: "about ripe", 3: "ripe"}
    i = 1

    def __init__(self, index: int, state=states[i]):
        self._index = index
        self._state = state

    def grow(self):
        self.i += 1
        self._state = self.states[self.i]
        return self._state

    def is_ripe(self):
        if self._state == self.states[3]:
            return "Tomato is ripe!"
        else:
            return "Wait!"


class TomatoBush:


t = Tomato(1)
print(t._state)
print(t.is_ripe())
print(t.grow())
print(t.is_ripe())
print(t.grow())
print(t.is_ripe())
