from model.contact import CONTACT


def test_modifyok_contact(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    app.open_home_page()
    old_contacts = app.add_new.get_add_new_list()
    contact = CONTACT(name="New contact")
    contact.id = old_contacts[0].id
    if contact.name is None:
           contact.name = old_contacts[0].name
    if contact.lastname is None:
            contact.lastname = old_contacts[0].lastname
    app.add_new.modifyok_first_contact(contact)
    new_contacts = app.add_new.get_add_new_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=CONTACT.id_or_max) == sorted(new_contacts, key=CONTACT.id_or_max)



#def test_modifyok_contact_middlename(app):
#    if app.add_new.count() == 0:
#        app.add_new.create(CONTACT(name="test"))
#    app.open_home_page()
#    old_contacts = app.add_new.get_add_new_list()
#    app.add_new.modifyok_first_contact(CONTACT(middlename="New middlename"))
#    new_contacts = app.add_new.get_add_new_list()
#    assert len(old_contacts) == len(new_contacts)