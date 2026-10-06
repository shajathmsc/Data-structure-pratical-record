# Movie Ticket Booking System using Quick Sort

def quick_sort(bookings):

    if len(bookings) <= 1:
        return bookings

    pivot = bookings[-1]

    smaller = []
    greater = []

    for booking in bookings[:-1]:

        if booking["ticket_no"] <= pivot["ticket_no"]:
            smaller.append(booking)
        else:
            greater.append(booking)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


# Get booking details
n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):

    print("\nBooking", i + 1)

    ticket_no = int(input("Enter Ticket Number: "))
    name = input("Enter Customer Name: ")
    movie = input("Enter Movie Name: ")
    seats = int(input("Enter Number of Seats: "))

    bookings.append({
        "ticket_no": ticket_no,
        "name": name,
        "movie": movie,
        "seats": seats
    })


# Display original bookings
print("\n--- Original Booking Details ---")

for booking in bookings:
    print(
        booking["ticket_no"],
        booking["name"],
        booking["movie"],
        booking["seats"]
    )


# Sort bookings
bookings = quick_sort(bookings)


# Display sorted bookings
print("\n--- Sorted Booking Details ---")

for booking in bookings:
    print(
        "Ticket No:", booking["ticket_no"],
        "| Name:", booking["name"],
        "| Movie:", booking["movie"],
        "| Seats:", booking["seats"]
    )