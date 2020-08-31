# Start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

while unconfirmed_users:
	current_user  = unconfirmed_users.pop()
	confirmed_users.append(current_user)

# display all the confirmed users
print("\n The following user have been confirmed")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())