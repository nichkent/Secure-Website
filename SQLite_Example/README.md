### Database Flask Final Project

## Setup
To run this program first make sure that you have the database setup correctly. You can do this by opening testing.py 
and executing this file. In the console it should display the user, password, and access level. (If this does not happen
refer below) Once you have verified that the database is set up; run launch.py. This will open a window where you can
access the login and create user pages.

## If Database Setup Fails
You will have to manually set up the database yourself with the add_user(username, password) function. It will the
username and password as parameters as strings. To modify the access levels you will need to hard code them into the 
code for add_user. The variable is called access_level = 'BaseAccess'. Modify the BaseAccess string to AdminAccess,
EngineeringAccess, AccountingAccess, and BaseAccess depending on the information for the default accounts. Here's all
account's login information in case this is required (passwords will auto salt and hash once entered into add_user()):

chanbl42_1,Waluigi1%,AdminAccess
larible492,So$1cahtoa,EngineeringAccess
Genie678!,Wow(Nice1,AccountingAccess
NewGuy685),GoodL0rd%,BaseAccess

## Login Screen
Enter your username and password into the provided boxes. The access level will auto-assign based on this information.
Once entered, depending on which access_level you have provided, you will be sent to a screen specific for that access
level.

## Create User Screen
To create a user, enter the users new name and password into the boxes. Once entered, it will have 'BaseAccess' assigned
by default and the new user will be added to the database. (You will know this works if the page reloads after hitting
the button)(I wanted to add a confirmation message but, I ran out of time)

On this screen, there is a strong random password generator button that will bring you to a page with a strong random
password.

To navigate to any other pages click the links below these buttons.