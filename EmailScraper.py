import email, getpass, os, re, headerparser

""" Connecting to GMail account"""

user = raw_input("Enter your GMail username --> ")
pwd = getpass.getpass("Enter your password --> ")

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)

""" Parsing Headers"""

parser = headerparser.HeaderParser()
