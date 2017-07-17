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

	def remove_contact(self, name):
		for contact in self._contacts:
			if name == contact.name:
				self._contacts.remove(contact)
				break
		else:
			print '{} was not found'.format(name)

		print '{} was removed'.format(name)

	def search_contact(self, name):
		for contact in self._contacts:
			if name == contact.name:
				self._print_contact(contact)
				break
		else:
			print '{} was not found'.format(name)

	def update_contact(self, name, n_name, n_phone, n_email):
		self._contact_to_modify = ''
		for contact in self._contacts:
			if name == contact.name:
				contact.name = n_name
				contact.phone = n_phone
				contact.email = n_email
				break

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
			name = str(raw_input('Contact\'s name: '))
			agenda.search_contact(name)
			n_name = str(raw_input('New name: '))
			n_phone = str(raw_input('New phone: '))
			n_email = str(raw_input('New email: '))
			agenda.update_contact(name, n_name, n_phone, n_email)
		elif cmd == 's':
			name = str(raw_input('Contact\'s name: '))
			agenda.search_contact(name)
		elif cmd == 'r':
			name = str(raw_input('Contact\'s name: '))
			agenda.remove_contact(name)
		elif cmd == 'l':
			agenda.list()
		elif cmd == 'e':
			break
		else:
			print 'Choose a valid action.'

if __name__ == '__main__':
	run()