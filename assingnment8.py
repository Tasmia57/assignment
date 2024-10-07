class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"


book1=Book("Atomic Habit", "James Cler", 162)

print(book1.get_description())