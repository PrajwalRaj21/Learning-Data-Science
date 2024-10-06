def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Happy you!")
    print()


happy_birthday("Bro", 20)  #passing arguments
happy_birthday("Steve", 30)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill is ${amount:1f} is due: {due_date}")


display_invoice("Purnika", 42.69, "01/01")
display_invoice("Prajwal", 40, "02/02" )

def add(x, y):
    z = x+y
    print(z)
    return z

add (4,5)


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Harry", "Kane")

print(full_name)


def funny_name(first, last):
    first = first.upper()
    last = last.upper()
    full_name = first + " "+ last

    print(full_name)


funny_name ("Purnika", "sharma")