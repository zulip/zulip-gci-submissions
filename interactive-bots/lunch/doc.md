# Lunch Bot 🍛
A small Zulip bot for organizing lunch with your friends and coworkers.

This bot is a Python clone of the [Hubot-Lunchbot](
https://www.npmjs.com/package/hubot-lunchbot) so if you are familiar with that 
bot you'll feel right home with this one.

## How does it work
Each user is allowed to create a type of shop list for meals

## Commands
`<user|optional> (I) want(s) <item>`
Adds <item> to the sender's (or <user>'s if specified) list of items

`<user> I want that`
Adds every item in <user>'s list of items to the sender's list of items

`<user|optional> remove <item>`
Removes <item> to the sender's (or <user>'s if specified) list of items

`<user|optional> remove all`
Removes all items to the sender's (or <user>'s if specified) list of items

`orders`
Show all orders

`<user|optional> order`
Shows all items of the sender's (or <user>'s if specified) list of items

`who should <verb>?`
Randomly selects a user from the orders list

`help`
Shows help (this section)

## Notes
Currently the bot is using a local JSON file to store all the data, however it 
should be pretty simple to port it over to a NoSQL database (or maybe even a 
SQL database).
