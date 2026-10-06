def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[-1]
    cheaper = []
    expensive = []

    for booking in bookings[:-1]:
        if booking["price"] <= pivot["price"]:
            cheaper.append(booking)
        else:
            expensive.append(booking)

    return quick_sort(cheaper) + [pivot] + quick_sort(expensive)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    print("\nBooking", i + 1)

    ticket = int(input("Enter Ticket Number: "))
    name = input("Enter Customer Name: ")
    price = int(input("Enter Ticket Price: "))

    bookings.append({
        "ticket": ticket,
        "name": name,
        "price": price
    })

bookings = quick_sort(bookings)

print("\n--- Bookings Sorted by Ticket Price ---")

for b in bookings:
    print("Ticket:", b["ticket"],
          "| Name:", b["name"],
          "| Price:", b["price"])