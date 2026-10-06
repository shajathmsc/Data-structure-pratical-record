def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[-1]
    smaller = []
    greater = []

    for booking in bookings[:-1]:
        if booking["seats"] <= pivot["seats"]:
            smaller.append(booking)
        else:
            greater.append(booking)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    print("\nBooking", i + 1)

    ticket = int(input("Enter Ticket Number: "))
    name = input("Enter Customer Name: ")
    seats = int(input("Enter Number of Seats: "))

    bookings.append({
        "ticket": ticket,
        "name": name,
        "seats": seats
    })

bookings = quick_sort(bookings)

print("\n--- Bookings Sorted by Seats ---")

for b in bookings:
    print("Ticket:", b["ticket"],
          "| Name:", b["name"],
          "| Seats:", b["seats"])