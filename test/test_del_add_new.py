from model.contact import CONTACT


def test_delete_first_add_new(app):
    if app.add_new.count() == 0:
        app.add_new.create(CONTACT(name="ededede", middlename="deded", lastname="dededed", nickname="nickname", title="dededed",
                    company="dededed", address="dededede",
                    mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                    address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf"))
    app.add_new.delete_first_add_new()
    app.add_new.return_to_home_page()
