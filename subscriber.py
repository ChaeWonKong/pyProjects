'''O'REILLY Newsletter Subscriber


Automatically join programming newsletter e-mail subscription.'''


import requests


def email_subscriber(email, first, last):
	params = {'email_addr': email, 'first_name': first, 'last_name': last}
	url = "http://post.oreilly.com/form/oreilly/signup4"
	r = requests.post(url, data = params)
	print(r.text)
	


address = input("Enter your e-mail address -->")
first_name = input("Enter your first name -->")
last_name = input("Enter your last name -->")

email_subscriber(address, first_name, last_name)

'''Currently not working!'''