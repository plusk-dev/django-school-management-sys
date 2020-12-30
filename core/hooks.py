from dhooks import Webhook

#Add your webhook URLs Here:
#Pro Tip: Paste the same URL in all LOL.
hooks = {
	'class-6': '',
	'class-7': '',
	'class-8': '',
	'class-9': '',
    'class-10': '',
    'class-6-teachers': '',
    'class-7-teachers': '',
    'class-8-teachers': '',
    'class-9-teachers': '',
    'class-10-teachers': '',
    'exam-notifications': '',
    'teachers-general': '',
    'announcements': '',
}

def send(to, message):
	hook = Webhook(hooks[to])
	hook.send(message)

