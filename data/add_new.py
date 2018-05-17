from model.contact import CONTACT
import random
import string

constant = [
CONTACT(name='name1', middlename='middlename1', lastname='lastname1', nickname='nickname1',
                               title='title1', company='company1', address='address1',
                               mobile='mobile1', work='work1', fax='fax1', email='email1',
                               byear='byear1',
                               address2='address21', phone2='phone21', notes='notes1'),
CONTACT(name='name2', middlename='middlename2', lastname='lastname2', nickname='nickname2',
                               title='title2', company='company2', address='address2',
                               mobile='mobile2', work='work2', fax='fax2', email='email2',
                               byear='byear2',
                               address2='address22', phone2='phone22', notes='notes2')
]


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
               for i in range(5)
    ]
