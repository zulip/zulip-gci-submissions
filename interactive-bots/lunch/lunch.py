import os
import sys
import random

PATH = os.path.join(os.path.dirname(sys.argv[0]), 'orders.txt')

class LunchBotHandler(object):
    def __init__(self):
        try:
            f = open(PATH, 'r')
        except IOError:
            f = open(PATH, 'w')
            f.write('\n')
            f.close()

    def usage(self):
        return '''
        This is a small Zulip bot for organizing lunch with your friends and 
        coworkers.
        '''

    # DATA OPERATIONS
    # Write
    def write_file(self, lines):
        f = open(PATH, 'w')
        f.write(''.join(lines))
        f.close()

    # Find
    def find_line(self, user, lines):
        num = 0
        for i, line in enumerate(lines):
            if line.split(' **wants**')[0] == user:
                num = i
                break
        return num

    # User finder
    # Finds if a user exists
    # error is True, return an error message
    # error is False, create the user line
    def user_finder(self, user, error):
        f = open(PATH, 'r')
        lines = f.readlines()
        line = self.find_line(user, lines)
        f.close()

        if line != 0:
            return False

        if not error:
            lines.append(user + ' **wants** \n')
            self.write_file(lines)
            return

        if error:
            return 'Sry, @**' + user + "** isn't hungry. :disappointed:"


    # Item interpreter
    # Transforms an array of items into a string
    def item_interpreter(self, items):
        item_str = ''
        for item in items:
            if len(item_str) == 0:
                item_str += ' ' + item
            else:
                if item_str[-1] == ',':
                    item_str += item
                else:
                    item_str += ' ' + item

        return item_str[1:] # Without the first white space

    # Get list of items
    # Returns a certain user's list of items
    def get_items(self, user):
        f = open(PATH, 'r')
        lines = f.readlines()
        line = self.find_line(user, lines)
        f.close()

        return [
            lines[line][:(len(user) + 10)],
            lines[line][(len(user) + 10):]
        ]

    # MESSAGE HANDLING
    # Copies user list
    def copy_user_list(self, original_user, user):
        # Verification
        if self.user_finder(original_user, True): # User doesn't exist so stop
            return self.user_finder(original_user, True)
        self.user_finder(user, False) # Check if user exists and create if it doesn't

        f = open(PATH, 'r')
        lines = f.readlines()
        original_line = self.find_line(original_user, lines)
        new_line = self.find_line(user, lines)
        f.close()

        # Adds the new items and saves
        items = lines[original_line].split('**wants**')[1]
        lines[new_line] = lines[new_line][:-1] + items

        self.write_file(lines)
        return "**Here's the new list of items:** :wink:\n" + lines[new_line]

    # Adds an item to a list
    def add_to_user_list(self, user, items):
        # Verification
        self.user_finder(user, False)

        items = self.item_interpreter(items)
        f = open(PATH, 'r')
        lines = f.readlines()
        user_line = self.find_line(user, lines)
        f.close()

        # Adds the new item
        lines[user_line] = lines[user_line][:-1] + items + ',\n'
        
        self.write_file(lines)

        return "**Here's the new list of items:** :wink:\n" + lines[user_line]

    # Removes an item from a list
    def remove_from_user_list(self, user, items):
        # Verification
        if self.user_finder(user, True):
            return self.user_finder(user, True)

        items = self.item_interpreter(items)
        f = open(PATH, 'r')
        lines = f.readlines()
        user_line = self.find_line(user, lines)
        f.close()

        # Removes the item
        current_list = self.get_items(user)
        current_list[1] = current_list[1].replace(items + ',', '')
        lines[user_line] = ''.join(current_list)

        self.write_file(lines)

        return "**Here's the new list of items:** :wink:\n" + lines[user_line]

    # Removes the list of items
    def remove_all(self, user):
        # Verification
        if self.user_finder(user, True):
            return self.user_finder(user, True)

        f = open(PATH, 'r')
        lines = f.readlines()
        user_line = self.find_line(user, lines)
        f.close()

        # Removes the line
        lines.pop(user_line)

        self.write_file(lines)

        return '**Cleared!** :ok_hand:\n'

    # Shows all orders
    def show_all_orders(self):
        f = open(PATH, 'r')
        return "**Here's the list of orders:**\n" + f.read()
        f.close()

    # Shows a specific order
    def show_order(self, user):
        # Verification
        if self.user_finder(user, True):
            return self.user_finder(user, True)

        f = open(PATH, 'r')
        lines = f.readlines()
        user_line = self.find_line(user, lines)
        f.close()
        return lines[user_line]

    def random_user(self, verb):
        f = open(PATH, 'r')
        lines = f.readlines()
        user_line = random.randint(1, len(lines) - 1) # 0 is an empty line
        f.close()

        # Selects the user
        user = lines[user_line].split()[0]
        verb = self.item_interpreter(verb)
        if verb[-1] == '?':
            verb = verb[:-1]

        return "I think @**" + user + "** should " + verb + ". :stuck_out_tongue:"

    # MESSAGE RECEIVERS
    def handle_message(self, message, bot_handler):
        content = self.keyword_selection(message)
        bot_handler.send_reply(message, content)

    def keyword_selection(self, message):
        msg = message['content'].split()

        if len(msg) == 0:
            return "I don't think I can do that. :frowning:"

        # Check if a user was referenced
        user = message['sender_full_name']
        if msg[0][0] == '@':
            user = msg[0][1:].replace('**', '')
            msg  = msg[1:]

        # Find the command
        if len(msg) == 0:
            return # null

        # <user> I want that
        if msg[-1] == 'that':
            return self.copy_user_list(user, message['sender_full_name'])

        # <user|optional> (I) want <item>
        if msg[0:2] == ['I', 'want']:
            return self.add_to_user_list(user, msg[2:])

        if msg[0] == 'wants':
            return self.add_to_user_list(user, msg[1:])

        # <user|optional> remove all
        if msg == ['remove', 'all']:
            return self.remove_all(user)

        # <user|optional> remove <item>
        if msg[0] == 'remove':
            return self.remove_from_user_list(user, msg[1:])
        
        # orders
        if msg[0] == 'orders':
            return self.show_all_orders()
        
        # <user|optional> order
        if msg[0] == 'order':
            return self.show_order(user)

        # who should <verb>?
        if msg[0:2] == ['who', 'should']:
            return self.random_user(msg[2:])

        if msg[0] == 'help':
            return '''
                <user|optional> (I) want(s) <item>
                Adds <item> to the sender's (or <user>'s if specified) list of items

                <user> I want that
                Adds every item in <user>'s list of items to the sender's list of items

                <user|optional> remove <item>
                Removes <item> to the sender's (or <user>'s if specified) list of items

                <user|optional> remove all
                Removes all items to the sender's (or <user>'s if specified) list of items

                orders
                Show all orders

                <user|optional> order
                Shows all items of the sender's (or <user>'s if specified) list of items

                who should <verb>(?)
                Randomly selects a user from the orders list

                help
                Shows help (this section)
            '''

        return "I don't think I can do that. :frowning:"


handler_class = LunchBotHandler