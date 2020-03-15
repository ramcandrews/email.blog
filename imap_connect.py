import imaplib
import email.message

from pprint import pprint

msg_number = int()
server = input("server address:")
username =input("username:")
password = input("password:")
port = int()

# Connect to the server
print('Connecting to ', server)
connection = imaplib.IMAP4_SSL(server, port)

# Login to our account
print('Logging in as ', username)
connection.login(username, password)

try:
    typ, data = connection.list()
    print('Response code:', typ)
    print('Response:')
    pprint(data)

    typ, data  = connection.select('Drafts', readonly=True)
    print(typ, data)
    num_msgs = int(data[0])
    print('There are %d messages in Drafts' % num_msgs)
    for message in range(5):
        msg_number += 1
        typ, msg_data = connection.fetch("{}".format(msg_number), '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                meta = email.message_from_string(response_part[1].decode("utf-8"))
                for header in [ 'to', 'from', 'subject' ]:
                    print('%-8s: %s' % (header.upper(), meta[header]))
                if meta.is_multipart():
                    print('BODY: ', meta.get_payload()[0]) #plain
                    #print(meta.get_payload()[1]) #html                
                else:
                    print('BODY: ', meta.get_payload(None, True))
finally:
    try:
        connection.close()
    except:
        pass
        connection.logout()

