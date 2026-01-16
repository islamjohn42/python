toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])

toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'
# TypeError: 'tuple' object does not support item assignment

toys = list(toys)
print(toys)
toys[3] = "dragon"
print(toys)

toys = tuple(toys)
print(type(toys))
