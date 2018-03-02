'''Post Request Practice

Post First and Last name in the two form fields of given page.'''

import requests


def post_name(first, last):
	params = {'firstname': first, 'lastname': last}
	r = requests.post("http://pythonscraping.com/files/processing.php", data = params)
	print(r.text)

first_input = input("Enter your first name -->")
last_input = input("Enter your last name -->")

post_name(first_input, last_input)