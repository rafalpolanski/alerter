import traverser as ts
import auxiliaries as ax
import smtplib
import glob
import os

# CONSTANTS
filename = "config.txt"

# get key from config INI section

def send_email_alert(email_recipient, miner, email_body):
    gmail_user = 'koparkofile@gmail.com'
    gmail_password = '123koparka'

    sent_from = "Kopareczka" + miner + "@"
#   to = ['me@gmail.com', email_recipient]
    subject = 'Alert'

    email_text = """
    From: {0}
    To: {1}
    Subject: {2}

    {3}
    """.format(sent_from, email_recipient, subject, email_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()

        server.login(gmail_user, gmail_password)

        server.sendmail(gmail_user, email_recipient, email_text)

        server.close()

        print('Email sent!')
    except Exception as e:
        print("alert not sent to",email_recipient)
        print(e)



list_of_files = glob.glob(ax.get_value_from_config(filename, "INI", "log_dir") + "*")
latest_file = max(list_of_files, key = os.path.getctime)

memo = ts.traverse_log(latest_file)
print(memo)

config_file = ax.open_log_file(filename)

number_email  = int(ax.get_value_from_config(filename, "INI", "n_ppl_to_notify"))
i = 0
while i < number_email:
    send_email_alert(ax.get_value_from_config(filename,"INI", "e_"+str(i+1)), ax.get_value_from_config(filename, "INI", "miner_identifier"), memo)
    i += 1

ax.close_log_file(config_file)
