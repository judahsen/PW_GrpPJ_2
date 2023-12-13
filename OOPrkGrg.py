class Parking_Garage():

    def __init__(self, tickets, parking_spaces):
        self.current_ticket = {"paid": ""}
        self.tickets = list(range(1, tickets + 1))
        self.parking_spaces = list(range(1, parking_spaces + 1))

    def take_ticket(self):
        if not self.tickets:
            print("Sorry, the parking garage is full.")
            return

        s = int(input(f"Available spaces: {self.parking_spaces}\nChoose a space: "))
        if s in self.parking_spaces:
            self.tickets.remove(s)
            self.parking_spaces.remove(s)
            print(f"Ticket issued for space {s}")
        else:
            print("Invalid space. Please choose an available space.")

    def pay_for_parking(self):
        while True:
            print(self.parking_spaces)
            payment = int(input("Please enter payment: "))
            if payment >= 1:
                print("Payment accepted. Please exit within 15 minutes!")
                self.current_ticket["paid"] = str(payment)
                break
            else:
                print("Invalid payment.")

    def leave_garage(self):
        if self.current_ticket["paid"]:
            print("Thank you, have a nice day!")

    def runner(self):
        while True:
            check_point = input("Are you entering or exiting? ").lower()
            if check_point == "entering":
                self.take_ticket()
            elif check_point == "exiting":
                self.pay_for_parking()
                self.leave_garage()
                break

user = Parking_Garage(tickets=5, parking_spaces=5)
user.runner()
