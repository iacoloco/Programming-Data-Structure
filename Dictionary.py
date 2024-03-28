#remove the None Item from the Dictionary

user_preferences = { 
    "Time Zone" : "GMT",
    "language" : "Spanish",
    "Notificatins" : None , 
    "currency" : "USD",
    "theme" : None
}


def update_preferences(user_pref):
    update_preferences= {}
    for key, valiue in user_pref.items():
        if valiue is not None :
            update_preferences[key] = valiue
    
    
    return update_preferences


print(update_preferences(user_preferences))