from users import User
class Privilegies():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can stop the server', 'can see the database']

    def show_admin_privileges(self):
        print("Administradores conseguem: ")
        for privilege in self.privileges:
            print("-->" + privilege.title())


class Admin(User):
    def __init__(self, first_name, last_name, age, fav_animal, job):
        super().__init__(first_name, last_name, age, fav_animal, job)
        self.show_privileges = Privilegies()

