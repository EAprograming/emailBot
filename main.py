from ast import Try
from collections import Counter
import sendEmail


#

email = ''#my email
password = '' #my password
send_to_email = '' #send_to_email
subject = ''  # The subject line
message = '''
massage
'''
counter = 0

sendEmail.sendemail(email, password, send_to_email, subject, message)

try:
    while True:
        counter = counter+1
        sendEmail.sendemail(email, password, send_to_email, subject, message)
except KeyboardInterrupt:
    pass

print("Total Email Sent: ", counter)
