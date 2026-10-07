class book:
    def __init__(self,author, title):
       self.author = author
       self.title = title
       self.review = []
 
    def add_review(self,review):
        self.review.append(review)
        print("the review is added successfully")
    def count_review(self):
        print(f"the count of review is ",len(self.review))
    def display_review(self):
        print ("review")
        for review in self.review:
            print(" ",review)

Book = book("priyanshu","the wall of success")

Book.add_review("the book is good")
Book.add_review("the book is very good")
Book.add_review("the book is excellent good")
Book.add_review("the book is loverly")

Book.count_review()
Book.display_review()
