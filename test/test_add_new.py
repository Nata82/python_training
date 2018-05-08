# -*- coding: utf-8 -*-
from model.contact import CONTACT
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [
        CONTACT(name="ededede", middlename="deded", lastname="dededed", nickname="nickname", title="dededed",
                company="dededed", address="dededede", home="890320120",
                mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf"),
        CONTACT(name="", middlename="", lastname="", nickname="",
                   title="", company="", address="",
                   mobile="", work="", fax="", email="",
                   byear="",
                   address2="", phone2="", notes="")
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




