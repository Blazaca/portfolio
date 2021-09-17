usernames = ['guccigang', 'freeloader2021',
             'youremom69', 'notabot', 'smurfboy', 'admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print('\nWelcome home Mr.Wayne.')
            print('Would you like to see a status report?')

        else:
            print('Hello ' + str(user) + " thank you for logging in again.")

else:
    print("User registration required.")