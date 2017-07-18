from agenda import Agenda
import csv

def run():

	agenda = Agenda()

	with open('contacts.csv', 'r') as f:
		reader = csv.reader(f)
		for idx, row in enumerate(reader):
			if idx == 0:
				continue
			agenda.add(row[0], row[1], row[2])

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
	print '*'*44
	print '|**********WELCOME TO YOUR AGENDA**********|'
	print '*'*44
	run()