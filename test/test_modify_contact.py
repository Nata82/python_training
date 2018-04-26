from model.contact import CONTACT


def test_modifyok_contact_name(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    app.open_home_page()
    app.add_new.modifyok_first_contact(CONTACT(name="New contact"))


def test_modifyok_contact_middlename(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    app.open_home_page()
    app.add_new.modifyok_first_contact(CONTACT(middlename="New middlename"))
