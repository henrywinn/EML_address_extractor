from email.parser import Parser
from email.message import Message
from os import walk
import re, sys

ignore_to = raw_input('If you would like to filter out emails sent to you, enter your email\n')
output_name = raw_input('Enter the name of the file you would like to output (.csv extension added automatically)\n')
directory = raw_input('Enter the directory where the .eml files are\n')

dictionary = {}
parser = Parser()
return_file = open(output_name+'.csv', 'w')
address_count = 0
file_count = 0

def get_addresses(string):
    regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
    if isinstance(string,basestring):
        matches = regex.findall(string)
        addresses = [x.lower() for x in matches]
        if len(addresses) > 0:
            return addresses
        else:
            return False
    else:
        return False

for (dirpath, dirnames, filenames) in walk(directory):
    for filename in filenames:
        if filename[-3:] == 'eml':
            f = open(dirpath+'/'+filename, 'r')
            file_count += 1
            eml = parser.parse(f, True)
            addresses = get_addresses(eml.get('To'))
            if addresses != False:
                for address in addresses:
                    if address != ignore_to: 
                        if address not in dictionary:
                            dictionary[address] = True
                            return_file.write(address+"\n")
                            address_count += 1
                            sys.stdout.write("\r%s files read" % file_count)
            f.close()

if file_count == 0:
    print 'No files were scanned. Perhaps you entered the directory name incorrectly?'
else:
    sys.stdout.write("\r%s files scanned\n" % file_count)
    sys.stdout.write("%s emails added to csv\n" % address_count)