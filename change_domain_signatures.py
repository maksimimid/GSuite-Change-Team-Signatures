
'''
Prepare API key and put it in directory with script
Prepare 'template.mustache' file with your desired template
Prepare your 'Team Information - Email-Signatures.csv' with  name, title, mobile, email filed columns
'''

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools, service_account
from pystache import Renderer
import os
import csv

path = os.getcwd()
scopes = ['https://www.googleapis.com/auth/gmail.settings.basic']
credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(f'{path}/service_account_key.json', scopes)


def change_signature(email, name, title, mobile):
    delegated_credentials = credentials.create_delegated(email)
    http_auth = delegated_credentials.authorize(Http())
    gmail = discovery.build('gmail', 'v1', http=http_auth)
    send_as_body = {
        'signature': Renderer().render_path('template.mustache', {
            'name': name,
            'title': title,
            'mobile': mobile            
        })
    }

    print('Changing signature for {0}'.format(email))

    gmail.users().settings().sendAs().update(
        userId='me',
        sendAsEmail=email,
        body=send_as_body
    ).execute()


with open(f'{path}/Team Information - Email-Signatures.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)    
    for index, row in enumerate(spamreader, 0):
        if index != 0:  # Index 0 - is our titles of the table, if you remove titles you need to start iteration from 0
            name = row[1]
            title = row[2]
            mobile = row[3]
            email = row[4]
            print('name: ', row[1], 'title: ', row[2], 'mobile: ', row[3], 'email: ', row[4])
            change_signature(email, name, title, mobile)  # Title
input('Finished, enter to exit!')