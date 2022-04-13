#!usr/bin/python3

#standard imports
import os

#third party imports
import getpass

dec_pass = getpass.getpass(prompt='Enter password to decrypt:')

enc=os.popen("ls enc")
databases=enc.readlines()

str_databases = []
for element in databases:
        str_databases.append(element.strip())

def decrypt(database):
	os.system("openssl enc -aes-256-cbc -d -base64 -in enc/%s -out dec/%s.sql -k %s" % (database,database,dec_pass))

for db in str_databases:
	decrypt(db)

os.system("rm -f enc/*")
