def person_items(*items):
    for item in items:
        print("\n" + item + " has being ordered")
person_items('ham' , 'cheese')
person_items("egg" , "bacon" , "barbeque")
person_items("omelet" , "tuna" , "hotdog" , "egg")