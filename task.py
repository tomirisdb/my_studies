class website:
    def __init__(self, name, country_hosting):
        self.name = name
        self.country_hosting = country_hosting
        self.user_list = {}

    def welcome_user(self, name1):
        print(f'{name1} , WELCOME!')

    def create_account(self):
        name1 = input('what is your name?')
        password = input('what is your password?')
        self.user_list[name1] = password

    def sign_in(self):
        name1 = input('what is your account name?')
        password = input('write your password')
        if self.user_list[name1] == password:
            self.welcome_user(name1)

    def menu_of_website(self):
        print('create account\nsign in')
        x = input()
        while x != 'exit':
            if x == 'create account':
                self.create_account()
            elif x == 'sign in':
                self.sign_in()
            else:
                print('Invalid answer')
            print('create account\nsign in')
            x = input()


website = website('Netflix', 'USA')
website.menu_of_website()
