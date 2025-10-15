# zip(*iterables) = aggregate lements from two or more iterables (lists, tuples, etc.)
# creates a zip object with paired elements stored in tuples for each element

usernames = ['samuel', 'carla', 'jeffrey']
passwords = ['123', '456', '789']

users = dict(zip(usernames, passwords))
print(type(users))

for key, value in users.items():
    print(f'{key}: {value}')
