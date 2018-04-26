from model.contact import CONTACT


def test_delete_first_add_new(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="test"))
    app.add_new.delete_first_add_new()
    app.add_new.return_to_home_page()
