# -*- coding: utf-8 -*-
from model.contact import CONTACT




def test_add_new(app, data_contacts):
    contact = data_contacts
    old_contacts = app.add_new.get_add_new_list()
    app.add_new.open_add_new_page()
    app.add_new.create(contact)
    assert len(old_contacts) + 1 == app.add_new.count()
    new_contacts = app.add_new.get_add_new_list()
    app.add_new.return_to_home_page()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)




