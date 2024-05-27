class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year
    def infa(self):
        print(f"Название {self.name}, автор {self.author}, год написания {self.year}")

book1 =Book("OMG", "Natasha", 1991)
book1.infa()
