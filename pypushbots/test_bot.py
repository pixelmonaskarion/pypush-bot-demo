from imessage import iMessageUser, iMessage
import bot

def test_bot(msg: iMessage, im: iMessageUser):
    im.send_text("Hello World!", msg.sender)

bot.add_bot(test_bot)
bot.start()