import re
from model.contact import CONTACT

def test_phones_on_home_page(app, db):
    contact_from_home_page = app.add_new.get_add_new_list()
    contact_from_homes_page = db.get_add_new_list()
    assert sorted(contact_from_homes_page, key=CONTACT.id_or_max) == sorted(contact_from_home_page, key=CONTACT.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.home,contact.mobile,contact.work,contact.phone2]))))

def  merge_email_like_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))