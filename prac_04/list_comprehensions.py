names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_initials = [name[0] for name in names]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

print(" ".join(sorted(names)))

lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(n) for n in almost_numbers]
print(numbers)

numbers_over_nine = [n for n in numbers if n > 9]
print(numbers_over_nine)

long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_names)
