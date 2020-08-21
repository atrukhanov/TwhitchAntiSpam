
from twitchio.ext import commands
import Recognizer


class Bot(commands.Bot):

	recognizer = Recognizer('ipsum')

	def __init__(self):
		super().__init__(irc_token='...', client_id='...', nick='...', prefix='!',
						 initial_channels=['...'])

	async def event_message(self, message):
		if recognizer.check_message(message.content):
			id = recognizer.check_matching(message.content)
			if (id == -1):
				recognizer.push_buffer(message)
			else:
				if !check_flag(id):
					message.channel.ban(recognizer.get_message(id).author)
					set_ban(id)
				message.channel.ban(message.author)

if __name__ == '__main__':

	bot = Bot()
	bot.run()