
class Publisher:
    def __init__(self, name):
        self.publisher = name

class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, name, title, author, price):
        Book.__init__(self, name, title, author)
        self.price = price

    def display(self,):
        print("Publisher:", self.publisher)
        print("Book Title:", self.title)
        print("Author:", self.author)

    def display(self, price):
        print("Publisher:", self.publisher)
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", price)


p = Python("ABC Publications", "Python Programming", "John", 450)

p.display(450)
