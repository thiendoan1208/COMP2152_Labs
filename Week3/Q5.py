print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}
print("Alice's phone number: ", contacts["Alice"])

contacts.update({"Diana": "555-4321"})
print("Contact after adding Diana: ", contacts)

contacts["Bob"] = "555-000"
print("Contact after updating Bob: ", contacts)

del contacts["Charlie"]
print("Contact after deleting Charlie: ", contacts)

print("All contact names: ", contacts.keys())
print("All contact numbers: ", contacts.values())

print("Total number:", len(contacts))