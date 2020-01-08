class ContactList(list):
	def __init__(self, my_list):
		list.__init__(self)
		self.my_list = my_list

	def search_by_name(self, name):
		self.name = name
		for i in self.my_list:
			if i == name:
				print(i)
			else:
				pass


all_contacts = ContactList(['juma', 'juma', 'jumatay', 'zhumatay', 'juma', 'zhumatai'])
all_contacts.search_by_name("juma")