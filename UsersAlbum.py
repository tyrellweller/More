def make_album(name , title , number = 0):
    music_album = {'name' : name ,
                   'title' : title}
    if number != 0:
        music_album['tracks'] = number
    return music_album
while True:
    name = input("Enter the artist name : ")
    title = input("Enter the title song : ")
    number = int(input("Enter the number of tracks : "))
    album = make_album(name , title , number)
    for key , value in album.items():
        print("\n" + key)
        print("\t\t" + str(value))
    repeater = input("Would you like to add again : ")
    if repeater == 'no':
        break