class User():
    """Mostra informações sobre um usuário."""

    def __init__(self, first_name, last_name, age, fav_animal, job):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = int(age)
        self.fav_animal = fav_animal
        self.job = job
        self.login_attemps = 0

    def describe_user(self):
        print("\n-->Nome completo: " + self.full_name.title())
        print("-->Idade: " + str(self.age) + " anos.")
        print("-->Animal favorito: " + self.fav_animal.title())
        print("-->Emprego: " + self.job.title())
        print("-->Tentativas de login: " + str(self.login_attemps))

    def greet_user(self):
        print("\nOlá " + self.first_name.title() + "! Welcome again.")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, fav_animal, job):
        super().__init__(first_name, last_name, age, fav_animal, job)
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can stop the server', 'can see the database']

    


class Privilegies():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can stop the server', 'can see the database']

    def show_admin_privileges(self):
        print("Administradores conseguem: ")
        for privilege in self.privileges:
            print("-->" + privilege.title())

im_admin = Admin('eduardo', 'santos', '17', 'cachorro', 'CEO')
im_admin.increment_login_attemps()
im_admin.describe_user()
im_admin.greet_user()
im_admin.show_admin_privileges()
