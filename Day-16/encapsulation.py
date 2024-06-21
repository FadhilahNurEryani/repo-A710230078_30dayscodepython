class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_price(self, price):
        self.__price = price
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price

# Create a Book object
book = Book("Python Programming", "John Smith", 49.99)

# Set the title, author, and price
book.set_title("Python Programming")
book.set_author("Baba")
book.set_price("Rp 99.999")

# Get the title, author, and price
print("Title:", book.get_title())
print("Author:", book.get_author())
print("Price:", book.get_price())