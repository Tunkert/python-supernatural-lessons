sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3, 3.14}

print("The length of the sample set is \
" + str(len(sample_set)) + ".")

sample_set.add("Castiel")

print("The length of the sample set is \
" + str(len(sample_set)) + ".")

sample_set.add("Castiel")

print(sample_set)

sample_set_2 = sample_set.copy()

print(sample_set_2)

for item in sample_set_2:
    print(item)
