from model.contact import CONTACT
import random

def test_delete_some_add_new(app, db, check_ui):
    if len (db.get_add_new_list()) == 0:
        app.add_new.create(CONTACT(name="test"))
    old_contacts = db.get_add_new_list()
    contact = random.choice(old_contacts)
    print(contact.id)
    app.add_new.delete_add_new_by_id(contact.id)
    new_contacts = db.get_add_new_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    app.add_new.return_to_home_page()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=CONTACT.id_or_max) == sorted(app.add_new.get_add_new_list(),key=CONTACT.id_or_max)




