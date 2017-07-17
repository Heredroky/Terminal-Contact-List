class Contact:
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

class Agenda:
	def __init__(self):
		self._contacts = []

	def add(self, name, phone, email):
		contact = Contact(name, phone, email)
		self._contacts.append(contact)

	def list(self):
		for contact in self._contacts:
			self._print_contact(contact)

	def _print_contact(self, contact):
		print '*--*--*--*--*--*--*--*--*--*--*--*'
		print 'Name: {}'.format(contact.name)
		print 'Phone: {}'.format(contact.phone)
		print 'Email: {}'.format(contact.email)


def run():

	agenda = Agenda()
	while True:
		print '''What do you wanna do?
	[a]Add Contact
	[u]Update Contact
	[s]Search Contact
	[r]Remove Contact
	[l]List Contacts
	[e]Exit'''
		cmd = str(raw_input('=> '))

		if cmd == 'a':
			name = str(raw_input('Contact\'s name: '))
			phone = str(raw_input('Contact\'s phone: '))
			email = str(raw_input('Contact\'s email: '))
			agenda.add(name, phone, email)

		elif cmd == 'u':
			print ''
		elif cmd == 's':
			print ''
		elif cmd == 'r':
			print ''
		elif cmd == 'l':
			agenda.list()
		elif cmd == 'e':
			break
		else:
			print 'Choose a valid action.'

if __name__ == '__main__':
	run()