def make_album(name , title , number = 0):
    music_album = {'name' : name ,
                   'title' : title}
    if number != 0:
        music_album['tracks'] = number
    return music_album

album1 = make_album("eminem" , "lose yourself")
album2 = make_album("sian" , "pusong bato" , 2)
album3 = make_album("tupac" , "dear mama" , 20)

print(album1)
print(album2)
print(album3)