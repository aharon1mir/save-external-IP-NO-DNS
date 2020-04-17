#!/usr/bin/python
import imaplib

user = "user@gmail.com"

pwd = "pass"

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/&BdMF1QXQBeg- &BdkF1QXmBdA-")
resp, items = m.search(None, "ALL")
items = items[0].split()
resp, data = m.fetch(items[-1], "(RFC822)")
s = data[0][1].splitlines()[-1].strip()
print s
