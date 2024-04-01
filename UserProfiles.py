def build_profile(first , last , **others):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in others.items():
        profile[key] = value
    return profile
profile = build_profile('sian' , 'daniel' , age = 21 , address = 'ampalaya village gun ob' , gender = 'boy')
for key , value in profile.items():
    print(key + " : " + str(value))