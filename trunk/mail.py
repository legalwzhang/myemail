from poplib import POP3, error_proto
from email.mime.text import MIMEText
import smtplib
import mail_conf as conf
import email
import time
import execution

POP3SVR = conf.POP3SVR
USER = conf.USER
PSW = conf.PSW
SMTPSCR = conf.SMTPSCR
POSTFIX = conf.POSTFIX
DICT_ORDER = execution.DICT_ORDER


def login_email():
    try:
        pop_conn = POP3(POP3SVR)
        pop_conn.user(USER+'@'+POSTFIX)
        pop_conn.pass_(PSW)
    except error_proto,e:
        print "login failed", e
        return None
    return pop_conn

def analyze_email(pop_conn):
    try:
        for item in pop_conn.list()[1]:
            num, oc = item.split(' ')
            lines = pop_conn.retr(num)[1]
            msg = email.message_from_string("\n".join(lines))
            addfrom = msg.get('from')
            obj = msg.get('subject')
            if obj in DICT_ORDER.keys():
                pop_conn.dele(num)
                pop_conn.quit()
                return addfrom, obj
    except error_proto,e:
        print e    
    pop_conn.quit()
    return None,None

def send_email(addto, msg):
    addfrom = USER + '<' + USER + '@' + POSTFIX + '>'
    msg += ' success'
    msg_head = MIMEText(msg)
    msg_head['Subject'] = msg
    msg_head['From'] = addfrom
    msg_head['To'] = addto
    try:
        sm = smtplib.SMTP()
        sm.connect(SMTPSCR)
        sm.login(USER, PSW)
        sm.sendmail(addfrom, addto, msg_head.as_string())
        sm.close()
        return True
    except Except,e:
        print e
        return False



def respond_order(obj):
    for order in DICT_ORDER.keys():
        if obj == order:
            DICT_ORDER[order].action()
            return True


if __name__ == '__main__':
    while True:
        time.sleep(1)
        pop_conn = login_email()
        if pop_conn:
            addfrom, obj = analyze_email(pop_conn)
            print addfrom, obj
            if obj:
                if respond_order(obj):
                    send_email(addfrom, obj)


