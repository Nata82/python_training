# -*- coding: utf-8 -*-
from model.contact import CONTACT


def test_add_new(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_add_new_list()
    app.add_new.open_home_page()
    app.add_new.create(contact)
    new_contacts = db.get_add_new_list()
    app.add_new.return_to_home_page()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)




