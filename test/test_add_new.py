# -*- coding: utf-8 -*-
from model.contact import CONTACT
import pytest

from data.add_new import constant as testdata



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




