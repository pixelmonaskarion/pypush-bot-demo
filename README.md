# Creating a bot
creating a bot is very simple, here are the instructions:
1. import bot from the pypushbots folder `import pypushbots.bot as bots`
2. (optional) import iMessage and iMessageUser for code linting `from pypushbots.imessage import iMessageUser, iMessage`
3. create a bot function with parameters for the message and user `def bot(msg: iMessage, im: iMessageUser):`
4. run logic in the body of that function
5. register the function as a bot `bots.add_bot(bot)`
6. start pypush `bots.start()