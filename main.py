# dictionaries = changeable, unordered collection of unique key:value pairs


capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')


# # print(capitals['Russia'])

# for x in capitals:
#     print(x+" - "+capitals[x], end="----\n")

# # for x in capitals:
# #     print(capitals[x])

# # print(capitals['Germany']) # Error
# print(capitals.get('Germany')) # None

# print(capitals.items())

# print(capitals.keys())

for key,value in capitals.items():
    print(key,value)

capitals.clear()