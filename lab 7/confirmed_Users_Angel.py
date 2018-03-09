#lab 07
#file_name: confirmed_users_Angel.py
#date:03/08/13
#Start with users that need to be verified
#and an empty list to hold confirmed users.

unconfirmed_users = ['Alice','Brian','Candance']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

    #display confirmed users
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
        
