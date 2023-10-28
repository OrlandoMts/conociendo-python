creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']

toFilter = filter(lambda i: i[0].lower() in 'aeiou', creature_names)

print(list(toFilter))