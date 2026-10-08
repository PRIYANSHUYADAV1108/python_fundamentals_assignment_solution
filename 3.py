class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.review =[]
    def add_review(self,review):
        self.review.append(review)
        print("review added successfully")
    def count(self):
        print(f"count of review is " , len(self.review))

    def display_review(self):
        print("review")
        for review in self.review:
            print("",review)


Book = book("Harry Potter and The Philosopher,stone","j.k.Rowling")



Book.add_review("A magical and exciting story with memorable character")
Book.add_review("the book is entertraining and perfect for fantasy lovers") 
Book.add_review("harry journey at hogwarts is adventurous") 


Book.count()

Book.display_review()
