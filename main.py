#    string_slicing
#    indexing[] or slice()
#    [start:stop:step]

name = "Hahah Heheh"
first_name = name[:name.find(" ")]
last_name = name[name.find(" ")+1:]

funky_name = name[::2]
reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)


website = "http://google.com"
website2 = "http://gagrugraraasfasf.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])