def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[-1]
    before = []
    after = []

    for booking in bookings[:-1]:
        if booking["movie"].lower() <= pivot["movie"].lower():
            before.append(booking)
        else:
            after.append(booking)

    return quick_sort(before) + [pivot] + quick_sort(after)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    print("\nBooking", i + 1)

    ticket = int(input("Enter Ticket Number: "))
    name = input("Enter Customer Name: ")
    movie = input("Enter Movie Name: ")

    bookings.append({
        "ticket": ticket,
        "name": name,
        "movie": movie
    })

bookings = quick_sort(bookings)

print("\n--- Bookings Sorted by Movie ---")

for b in bookings:
    print("Ticket:", b["ticket"],
          "| Name:", b["name"],
          "| Movie:", b["movie"])