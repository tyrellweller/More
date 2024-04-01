def show_magicians(magicians):
    for magic in magicians:
        print("\t\t" + magic)
def make_great(magicians):
    newList = []
    for magic in magicians:
        message = "The great magician " + magic
        newList.append(message)
    return newList
magicians = ['sian' , 'daniel' , 'loreto']
newList = magicians[:]
newList = make_great(newList)
show_magicians(newList)