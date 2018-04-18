from model.add_new import ADD_NEW




def test_mod_add_new(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_new.mod_add_new()
    app.add_new.create(ADD_NEW(name="dedx", middlename="djk", lastname="swsw", nickname="nickname", title="dededed",
                    company="dededed", address="dededede",
                    mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                    address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf"))

    app.add_new.return_to_home_page()
    app.session.logout()