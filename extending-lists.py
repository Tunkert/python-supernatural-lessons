list1 = ["Bobby", "Dean", "Sam", "Jo", "Mary", "demon"]
list2 = ["Crowley", "Lucifer", "Michael", "Raphael", "Gabriel", "demon"]

deans_mother = list1.pop()

list1.extend(list2)

print(list1)

print(list1.count("demon"))

list1.remove("Jo")
print(list1)
print(deans_mother)

del list1[6]
print(list1)

# list1.clear()
# print(list1)

print(list1.index("Gabriel"))

list1.sort()
print(list1)

# list1.reverse()
# print(list1)

list1.insert(5, "Lilith")
print(list1)

list1.sort(reverse=True)
print(list1)
