from model.contact import CONTACT


def test_delete_first_add_new(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    old_contacts = app.add_new.get_add_new_list()
    app.add_new.delete_first_add_new()
    new_contacts = app.add_new.get_add_new_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    app.add_new.return_to_home_page()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
