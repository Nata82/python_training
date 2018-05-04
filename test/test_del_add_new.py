from model.contact import CONTACT
from random import randrange

def test_delete_some_add_new(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    old_contacts = app.add_new.get_add_new_list()
    index = randrange(len(old_contacts))
    app.add_new.delete_add_new_by_index(index)
    new_contacts = app.add_new.get_add_new_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    app.add_new.return_to_home_page()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts



