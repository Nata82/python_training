


def test_delete_first_add_new(app):
    app.open_home_page()
    app.add_new.delete_first_add_new()
    app.add_new.return_to_home_page()
