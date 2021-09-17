usernames = ['guccigang', 'freeloader2021',
             'youremom69', 'notabot', 'smurfboy', 'admin']
new_users = ['guCCigang', 'nOtabot', 'Hellacute', 'definitelyagirl', 'looker']

print("Checking username...\n")
for new_user in new_users:
    if new_user.lower() in usernames:
        print("Username " + str(new_user) + " already taken.")
    else:
        print(str(new_user) + " is available!")