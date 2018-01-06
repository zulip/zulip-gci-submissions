Instead of making a bot which calculates which messages are 'hello' messages,
 The bot now listens for new users, and sends them a Private Message with
 some information about zulip. The user can then ask questions to the bot,
 which is powered by DialogFlow. This is because it would be difficult to
 correctly train the bot, and, with testing, the bot was coming up with
 too many false positives. Furthermore, it was very hard to set up the
 bot to listen to all messages in a specific channel.

I started by making the part of the bot which listens for new members,
then sends them a message. Because we would not be using functions in
the interactive bots API, I decided to initially make this a standalone
script. It took me a long time to figure out how the zulip API worked,
and, after a bit of help from mentors, I found out how to use the API
correctly, and how the server would respond, as the `realm_user` event
response was not in the documentation. Once I had found that out, it
was simple to create a bot which responds to these events. I decided
to put this code in the WelcomeHandler class, so that it could be
easily called from the main bot handler class.

To make the actual bot, which answers questions, I made a bot which
inherits `DialogFlowHandler` which I made earlier. The only thing
I had to do in this class was to override the `initialize` function,
and add a call to the other `WelcomeHandler` class, which runs in
another thread.

At the moment, the bot has "small talk" enabled, with some custom
responses and is trained to answer one question ("How can I contribute?")

I couldn't figure out how to easily test the automatic welcome text,
however, I have thoroughly checked the code.

Although this approach works, we have decided to change how the bot works.
It is not going to use DF anymore, and is going to send the welcome message
when the user sends their first message.
