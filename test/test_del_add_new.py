


def test_delete_first_add_new(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_new.delete_first_add_new()
    app.add_new.return_to_home_page()
    app.session.logout()