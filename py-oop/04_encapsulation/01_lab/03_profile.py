class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username: str):
        count_chars = len(new_username)
        if not (5 <= count_chars <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password: str):
        if not self.__password_is_valid(new_password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = new_password

    def __password_is_valid(self, pw: str):
        rules = [
            len(pw) >= 8,
            any(ch.isdigit() for ch in pw),
            any(ch.isupper() for ch in pw),
        ]

        return all(rules)

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)