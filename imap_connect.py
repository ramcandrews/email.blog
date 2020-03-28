import imaplib
import email.message

import json
import re

import secrets

from pprint import pprint

# Connect to the server
print('Connecting to ', secrets.server)
connection = imaplib.IMAP4_SSL(secrets.server, secrets.port)

# Login to our account
print('Logging in as ', secrets.username)
connection.login(secrets.username, secrets.password)

msg_number = int()

try:
    typ, data = connection.list()
    print('Response code:', typ)
    print('Response:')
    pprint(data)

    typ, data  = connection.select('Drafts', readonly=True)
    print(typ, data)
    num_msgs = int(data[0])
    print('There are %d messages in Drafts' % num_msgs)

    theDict = dict()
    with open("test_dump.json", "w") as write_file:
    
        # num_msgs to read all messages.
        for message in range(num_msgs):
            msg_number += 1
            #theDict[msg_number] = list()
            typ, msg_data = connection.fetch("{}".format(msg_number), '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    meta = email.message_from_string(response_part[1].decode("utf-8"))
                    #for header in [ 'to', 'from', 'subject' ]:
                        #theDict[msg_number].append(meta[header])
                    if str(meta.is_multipart()):
                        try:
                            # Plaintext
                            if meta.get_payload()[0]:
                                for line in str(meta.get_payload()[0]).splitlines():
                                    if re.match('https?://+', line):
                                        theDict[meta['subject']] = line
                                    else:
                                        pass
                            #html
                            elif meta.get_payload()[1]:
                                for line in str(meta.get_payload()[1]).splitlines():
                                    if re.match('https?://+', line):
                                        theDict[meta['subject']] = line
                            
                        except:
                            theDict[meta['subject']] = None
                    else:
                        theDict[meta['subject']] = meta.get_payload(None, True)
            #print(theDict[meta['subject']])
        json.dump(theDict, write_file)
finally:
    try:       
        connection.close()
    except:
        pass
        connection.logout()

