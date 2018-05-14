# -*- coding: utf-8 -*-
from model.contact import CONTACT
import pytest
import random
import string

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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    pass
    old_contacts = app.add_new.get_add_new_list()
    app.add_new.open_add_new_page()
    app.add_new.create(contact)
    assert len(old_contacts) + 1 == app.add_new.count()
    new_contacts = app.add_new.get_add_new_list()
    app.add_new.return_to_home_page()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)




