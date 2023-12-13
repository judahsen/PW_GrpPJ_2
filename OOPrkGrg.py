

"""
Your parking gargage class should have the following methods:

- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1

- payForParking

- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid)
-> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage

- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"

- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary
"""

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

        

