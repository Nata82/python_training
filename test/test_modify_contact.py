from model.contact import CONTACT
import random


def test_modifyok_contact(app, db, check_ui):
    if len(db.get_add_new_list()) == 0:
        app.add_new.create(CONTACT(name="test"))
    app.open_home_page()
    old_contacts = db.get_add_new_list()
    mod_contact = random.choice(old_contacts)
    new_contact = CONTACT(name="New contact")
    new_contact.id = mod_contact.id
    if new_contact.name is None:
        new_contact.name = mod_contact.name
    if new_contact.lastname is None:
        new_contact.lastname = mod_contact.lastname
    id = new_contact.id
    app.add_new.modifyok_contact_by_id(id, new_contact)
    new_contacts = db.get_add_new_list()
    old_contacts.remove(mod_contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(app.add_new.get_add_new_list(), key=CONTACT.id_or_max)



