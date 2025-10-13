# sets = collection which is unordered, unindexed. no duplicate values

utensils = {"fork","spoon","plate","plate","plate","plate"}
dishes = {"bowl","plate","cup"}

# utensils.add("napkin")
# utensils.remove("plate")

# for x in utensils:
#     print(x)

# utensils.clear()

# utensils.update(dishes)

# dinner_table = utensils.union(dishes)

# for x in dinner_table:
#     print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))