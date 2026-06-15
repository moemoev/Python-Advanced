from project.customer import Customer
from project.dvd import DVD

class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def get_cust(self, cust_id) -> Customer:
        for customer in self.customers:
            if customer.id == cust_id:

                return customer

        raise ValueError("Customer not found")

    def get_dvd(self, dvd_id) -> DVD:
        for dvd in self.dvds:
            if dvd.id == dvd_id:

                return dvd

        raise ValueError("DVD not found")

    def rent_dvd(self, cust_id: int, dvd_id: int):
        customer = self.get_cust(cust_id)
        dvd = self.get_dvd(dvd_id)

        if dvd.id in [dvd.id for dvd in customer.rented_dvds]:

            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:

            return f"DVD is already rented"

        if customer.age < dvd.age_restriction:

            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, cust_id: int, dvd_id: int):
        customer = self.get_cust(cust_id)
        dvd = self.get_dvd(dvd_id)

        if dvd not in customer.rented_dvds:

            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = '\n'.join(str(customer) for customer in self.customers) + "\n"
        result += '\n'.join(str(dvd) for dvd in self.dvds)

        return result