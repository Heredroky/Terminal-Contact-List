from contact import Contact
import csv

class Agenda:
	def __init__(self):
		self._contacts = []

	def add(self, name, phone, email):
		contact = Contact(name, phone, email)
		self._contacts.append(contact)
		self._save()

	def remove_contact(self, name):
		for contact in self._contacts:
			if name == contact.name:
				self._contacts.remove(contact)
				self._save()
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
				self._save()
				break

	def list(self):
		for contact in self._contacts:
			self._print_contact(contact)

	def _save(self):
		with open('contacts.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerow(('name', 'phone', 'email'))
			for contact in self._contacts:
				writer.writerow((contact.name, contact.phone, contact.email))

	def _print_contact(self, contact):
		print '*--*--*--*--*--*--*--*--*--*--*--*'
		print 'Name: {}'.format(contact.name)
		print 'Phone: {}'.format(contact.phone)
		print 'Email: {}'.format(contact.email)