class UserNotFoundError(Exception):
    def __init__(self, message = "User not found"):
        super().__init__(message)
class WrongPasswordError(Exception):
    def __init__(self, message="Wrong password"):
        super().__init__(message)
class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            print(username)
            raise UserNotFoundError
        if self.users[username] != password:
            print(username)
            raise WrongPasswordError
    print("Logowanie powiodło się")


auth = UserAuth({"admin" : "1234" , "user":"abcd"})

try:
    auth.login("admin","1234")
    auth.login("unknow","pass")
    auth.login("user", "wrongpass")
except Exception as e:
    print(f"Błąd: {e} ")