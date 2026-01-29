from random import randint


class Train:
    def __init__(self, train_num):
        self.train_num = train_num

    def bookTicket(self, passenger_name, start, destination):
        print(
            f"ticket booked for {passenger_name} from {start} to {destination} on train number {self.train_num},seat num: {randint(1,100)}"
        )

    def getStatus(self):
        print(f"Train {self.train_num} is running on time.")

    def getFare(self):
        print(f"The price for train {self.train_num} is {randint(100,500)} INR.")


train1 = Train("12345")
train1.bookTicket("Alice","Bengaluru","Chennai");
train1.getStatus();
train1.getFare();