#!usr/bin/python3

#standard imports
import os
import time

#third party imports
import getpass
from dotenv import load_dotenv


# Global Variables
load_dotenv()
HOST=os.getenv('HOST')
PORT=os.getenv('PORT')
DB_USER=os.getenv('DB_USER')
DB_PASS=os.getenv('DB_PASS')

enc_pass = getpass.getpass(prompt='Enter password to encrypt:')
DB = os.popen(f"mysql -h {HOST} -P {PORT} -u {DB_USER} -p{DB_PASS} -e \"show databases;\"")
databases = DB.readlines()

str_databases = []
for element in databases:
	str_databases.append(element.strip())


filestamp = time.strftime('%Y-%m-%d-%I')

def get_dump(database):
	os.system(f"mysqldump -h {HOST} -P {PORT} -u {DB_USER} -p{DB_PASS} {database} > dec/{database}_{filestamp}.sql")

def encrypt(database):
	os.system(f"openssl enc -aes-256-cbc -base64 -in dec/{database}_{filestamp}.sql -out enc/{database}_{filestamp}.sqlenc -k {enc_pass}")

for db in str_databases:
	get_dump(db)
	encrypt(db)
os.system("rm -f dec/*")

