'''O'REILLY Newsletter Subscriber


Automatically join programming newsletter e-mail subscription.'''


import requests


def email_subscriber(email):
	params = {'email_addr': email}
	url = "http://conduit.ipost.com/forms.cgi"
	r = requests.post(url, data = params)
	print(r.text)

address = input("Enter your e-mail address -->")

email_subscriber(address)

'''Currently not working!'''