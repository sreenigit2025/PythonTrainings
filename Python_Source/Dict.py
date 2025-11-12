
d1 = {"name": "sreeni", "age": 30, "city": "hyderabad"}
print(d1)

print(d1["name"])   # Accessing value by key

print("keys in dictionary:")
print(d1.keys())

# OR
for key in d1:
    print(key)

print("values in dictionary:")

print(d1.values()  )
# OR
for value in d1.values():
    print(value)

print("key-value pairs in dictionary:")
print(d1.items())
# OR
for key, value in d1.items():
    print(f"{key}: {value}")