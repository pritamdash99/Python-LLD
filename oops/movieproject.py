"""
Create a class Movie with the following - 

Attributes -
movie_name -> name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods - 
book_ticket(num_tickets) - 
    books the given number of tickets. 
    If enough seats are available, confirm the booking and show the total amount to pay. 
    If not, show "sorry, not enough seats available"

show_status() - display movie name, seats availble, and seats booked so far.
"""

class Movie:

    def __init__(self, movie_name, total_seats, ticket_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets):
        if num_tickets <= (self.total_seats - self.booked_seats):
            self.booked_seats += num_tickets
            total_amount = num_tickets * self.ticket_price
            print(f"Booking confirmed for {num_tickets} tickets. Total amount to pay: ${total_amount}")
        else:
            print("Sorry, not enough seats available")

    def show_status(self):
        available_seats = self.total_seats - self.booked_seats
        print(f"Movie Name: {self.movie_name}")
        print(f"Seats Available: {available_seats}")
        print(f"Seats Booked: {self.booked_seats}")

movie1 = Movie("Inception", 100, 499)
movie1.show_status()
# Movie Name: Inception
# Seats Available: 100
# Seats Booked: 0

movie1.book_ticket(70)
# Booking confirmed for 70 tickets. Total amount to pay: $34930
movie1.show_status()
# Movie Name: Inception 
# Seats Available: 30
# Seats Booked: 70

movie1.book_ticket(70)
# Sorry, not enough seats available

