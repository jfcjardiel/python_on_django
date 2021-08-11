magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for value in range(1,5):
    print(value)

lista = list(range(1,6))
print(lista)

#slicing a list with positive and negative numbers
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())