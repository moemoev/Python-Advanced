class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.id = Customer.ID # self.id = type(self).get_next_id()
        self.name = name
        self.address = address
        self.email = email

        Customer.ID = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        return  Customer.ID

    def __repr__(self):
        result = f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
        return result