# The main (parent) class for all items in the library
class StockItem:
    def __init__(self, title, date_acquired, on_loan=False):
        self.title = title
        self.date_acquired = date_acquired
        self.on_loan = on_loan

    def set_loan(self, loan_status):
        """Change the loan status (True = on loan, False = available)."""
        self.on_loan = loan_status

    def display_details(self):
        """Show the basic details about this item."""
        print(f"Title: {self.title}")
        print(f"Date Acquired: {self.date_acquired}")
        print(f"On Loan: {'Yes' if self.on_loan else 'No'}")


# A child class for books
class Book(StockItem):
    def __init__(self, title, author, isbn, date_acquired, on_loan=False):
        super().__init__(title, date_acquired, on_loan)  # reuse StockItem setup
        self.author = author
        self.isbn = isbn

    def display_details(self):
        """Show details specific to a book."""
        super().display_details()  # show common info
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")


# A child class for CDs
class CD(StockItem):
    def __init__(self, title, artist, playing_time, date_acquired, on_loan=False):
        super().__init__(title, date_acquired, on_loan)
        self.artist = artist
        self.playing_time = playing_time  # in minutes

    def display_details(self):
        """Show details specific to a CD."""
        super().display_details()
        print(f"Artist: {self.artist}")
        print(f"Playing Time: {self.playing_time} minutes")


# Create a Book
book1 = Book("1984", "George Orwell", "9780451524935", "2025-01-12")
book1.display_details()

print("\nSetting book on loan...\n")
book1.set_loan(True)
book1.display_details()

# Create a CD
print("\n-----\n")
cd1 = CD("Abbey Road", "The Beatles", 47, "2024-10-01")
cd1.display_details()