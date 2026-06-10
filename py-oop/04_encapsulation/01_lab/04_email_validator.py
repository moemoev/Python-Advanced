class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, username: str):

        return  len(username) >= self.min_length


    def __is_mail_valid(self, mail: str):

        return mail in self.mails


    def __is_domain_valid(self, domain: str):

        return domain in self.domains

    def validate(self, email: str):
        username, mail_address = email.split('@')
        mail, domain = mail_address.split('.')

        rules = [
            self.__is_name_valid(username),
            self.__is_mail_valid(mail),
            self.__is_domain_valid(domain)
        ]

        return all(rules)

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))