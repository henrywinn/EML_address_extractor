from email.parser import Parser
from email.message import Message
from os import walk
import re

ignore_to = raw_input('If you would like to filter out emails sent to you, enter your email: ')

dictionary = {}
parser = Parser()
return_file = open('emails.csv', 'w')

def clean_address(string):
	regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
	matches = regex.findall(string)
	if len(matches) > 0:
		return matches[0].lower()
	else:
		return False

for (dirpath, dirnames, filenames) in walk('emails'):
    for filename in filenames:
    	f = open(dirpath+'/'+filename, 'r')
    	eml = parser.parse(f, True)
    	address = clean_address(eml.get('To'))
    	if address != False and address != ignore_to: 
    		if address in dictionary:
    			print 'hit'
    		else:
    			dictionary[address] = True
    			return_file.write(address+"\n")
    			print address