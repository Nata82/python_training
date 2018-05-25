import re
from model.contact import CONTACT

def test_phones_on_home_page(app, db):
    from_ui = sorted(app.add_new.get_add_new_list(), key=CONTACT.id_or_max)
    from_db = sorted(db.get_add_new_list(), key=CONTACT.id_or_max)
    assert len(from_ui) == len(from_db)
    for i in range(len(from_ui)):
        assert clear(from_ui[i].all_phones_from_home_page) == merge_phones_like_on_home_page(from_db[i])
        assert clear(from_ui[i].all_email_from_home_page) == merge_email_like_on_home_page(from_db[i])
        assert from_ui[i].address == from_db[i].address
        assert from_ui[i].lastname == from_db[i].lastname

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