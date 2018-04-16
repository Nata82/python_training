# -*- coding: utf-8 -*-
import pytest
from add_new import ADD_NEW
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_new_page()
    app.create_add_new(
            ADD_NEW(name="ededede", middlename="deded", lastname="dededed", nickname="nickname", title="dededed",
                    company="dededed", address="dededede",
                    mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                    address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf"))
    app.return_to_home_page()
    app.logout()

def test_add_empty_new(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_new_page()
    app.create_add_new(ADD_NEW(name="", middlename="", lastname="", nickname="",
                                    title="", company="", address="",
                                    mobile="", work="", fax="", email="",
                                    byear="",
                                    address2="", phone2="", notes=""))
    app.return_to_home_page()
    app.logout()
