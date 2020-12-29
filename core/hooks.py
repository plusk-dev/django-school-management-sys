from dhooks import Webhook

hooks = {
	'class-10': '',
	'exam-notifications': '',
	'teachers-general': '',
	'announcements': '',
}

def send(to, message):
	hook = Webhook(hooks[to])
	hook.send(message)

