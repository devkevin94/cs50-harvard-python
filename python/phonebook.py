from cs50 import get_string

people = {
    "Brian": "+1-617-495-100",
    "Brian": "+1-617-495-101"
}

name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")
