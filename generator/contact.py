from model.contact import CONTACT
import random
import string
import os.path
import json
import getopt
import sys



try:
    opts, args =getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [CONTACT(name="", middlename="", lastname="", nickname="",
                               title="", company="", address="",
                               mobile="", work="", fax="", email="",
                               byear="",
                               address2="", phone2="", notes="")] + [

               CONTACT(name=random_string("name", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 15),
                       company=random_string("company", 7), address=random_string("address", 8),
                       home=phone(9),
                       mobile=phone(9), work=random_string("work", 10), fax=random_string("fax", 9),
                       email=random_string("email", 10), byear=random_string("byear", 8),
                       address2=random_string("address2", 20), phone2=random_string("phone2", 8),
                       notes=random_string("notes", 10))
               for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))