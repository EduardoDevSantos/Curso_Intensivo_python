class User():
    """Mostra informações sobre um usuário."""
    def __init__(self,first_name,last_name,age,fav_animal,job):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name +" "+ last_name
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
        self.login_attemps+=1
    def reset_login_attemps(self):
        self.login_attemps=0
# acc1 = User('eduardo','santos',17,'cachorro','estudante')
# acc1.describe_user()
# acc1.greet_user()

# acc2 = User('joão','firmino',72,'gato','faz tudo')
# acc2.describe_user()
# acc2.greet_user()

acc3 = User('jorge','firmino',49,'passáro','ajudante de vendas')
acc3.increment_login_attemps()
acc3.increment_login_attemps()
acc3.increment_login_attemps()
acc3.increment_login_attemps()
acc3.increment_login_attemps()
acc3.reset_login_attemps()
acc3.describe_user()
acc3.greet_user()
