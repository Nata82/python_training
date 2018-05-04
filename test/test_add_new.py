# -*- coding: utf-8 -*-
from model.contact import CONTACT


# Ввод новый контакт
def test_add_new(app):
    old_contacts = app.add_new.get_add_new_list()
    app.add_new.open_add_new_page()
    contact = CONTACT(name="ededede", middlename="deded", lastname="dededed", nickname="nickname", title="dededed",
                    company="dededed", address="dededede",
                    mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                    address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf")
    app.add_new.create(contact)
    assert len(old_contacts) + 1 == app.add_new.count()
    new_contacts = app.add_new.get_add_new_list()
    app.add_new.return_to_home_page()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)

#def test_add_empty_new(app):
#    old_contacts = app.add_new.get_add_new_list()
#    app.add_new.open_add_new_page()
#    contact = CONTACT(name="", middlename="", lastname="", nickname="",
#            title="", company="", address="",
#            mobile="", work="", fax="", email="",
#            byear="",
#            address2="", phone2="", notes="")
#    app.add_new.create(contact)
#    new_contacts = app.add_new.get_add_new_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    app.add_new.return_to_home_page()
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)




