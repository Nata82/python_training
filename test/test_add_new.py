# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.add_new import ADD_NEW


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
# Ввод новый контакт
def test_add_new(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_new.open_add_new_page()
    app.add_new.create(
            ADD_NEW(name="ededede", middlename="deded", lastname="dededed", nickname="nickname", title="dededed",
                    company="dededed", address="dededede",
                    mobile="89032012010", work="87451241210", fax="87451201454", email="dsdsdfs@mail.ru", byear="1985",
                    address2="dedededededrftrgtg", phone2="gtggtgtgtgtg", notes="gtgrfrffrfrfrf"))
    app.add_new.return_to_home_page()
    app.session.logout()

def test_add_empty_new(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.add_new.open_add_new_page()
    app.add_new.create(ADD_NEW(name="", middlename="", lastname="", nickname="",
                               title="", company="", address="",
                               mobile="", work="", fax="", email="",
                               byear="",
                               address2="", phone2="", notes=""))
    app.add_new.return_to_home_page()
    app.session.logout()


