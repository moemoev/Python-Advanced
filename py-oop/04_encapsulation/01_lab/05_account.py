class Account:
    wrong_pin_message = "Wrong pin"

    def __init__(self, user_id: str, balance: int, pin: str):
        self.__id = user_id
        self.balance = balance
        self.__pin = pin



    def get_id(self, pin):
        if not pin == self.__pin:
            return self.wrong_pin_message

        return self.__id

    def change_pin(self,old_pin, new_pin):
        if not self.__pin == old_pin:
            return self.wrong_pin_message

        self.__pin = new_pin

        return f"Pin changed"

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))