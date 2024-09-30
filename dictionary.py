# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates


capitals = {"USA": "Washignton D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Russia"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else: 
#     print("That capital doesn't exist")

# capitals.update({"Germany" : "Berlin", 
#                  "Mexico": "Mexico City"})
# print(capitals)

# removes the item; doesnt need the value, just he key. If no key specified, it removes the last item in the list. 
# capitals.pop("China")
# print(capitals)

#clears the dictionary
# capitals.clear()
# print(capitals)

#returns a list of keys only, not values
# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# prints only values 
# values = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")