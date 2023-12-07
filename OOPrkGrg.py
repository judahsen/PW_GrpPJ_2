"""
#Your parking gargage class should have the following methods:

#- takeTicket
#- This should decrease the amount of tickets available by 1
#- This should decrease the amount of parkingSpaces available by 1

#- payForParking

# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid)
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
#parking_spaces = [1, 2, 3, 4, 5]
#tickets = [1, 2, 3, 4, 5,]

        
class Parking_Garage():
#display parking spaces show(parking_spaces) s="(input{f'show'} choose a space:  "):
    
    def __init__(self, tickets, parking_spaces):

        self.current_ticket = {}
        self.tickets = [1, 2, 3, 4, 5,]
        self.parking_spaces = [1, 2, 3, 4, 5]
    
    def take_ticket(self):
        s = input(f"{self.parking_spaces} Choose a space!")
        if (s == 1 or s == 2 or s == 3 or s == 4 or s == 5):
            del self.parking_spaces [s]
            del self.tickets [s]

    def payforparking(self):
        p = int(input("Please enter payment amount..."))
        if p >= 1:
            print("Thank you, have a nice day!")
        else:
            print("Please enter your payment amount")
    
        
    
    












