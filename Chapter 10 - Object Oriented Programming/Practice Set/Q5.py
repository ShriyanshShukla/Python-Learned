from random import randint

class Train:
    def __init__(self, destination):
        self.desti = destination
        self.train_no = randint(10000, 20000)

    def book_ticket(self):
        print(f"Your ticket is booked in train no: {self.train_no}")
        
    def get_status(self):
        print(f"The train {self.desti} is running on time")

    def get_info(self):
        print(f"The train no: {self.train_no}\nYour destination is {self.desti}")


yatri = Train("from Chhatarpur to Mathura")
yatri.get_info()
yatri.get_status()
yatri.book_ticket()