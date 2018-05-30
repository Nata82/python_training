from model.contact import CONTACT
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="NEW"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_add_new_in_group(group)) == 0:
        app.add_new.create(CONTACT(name="New"))
    contact = random.choice(orm.get_add_new_not_in_group(group))
    app.add_new.add_to_group(contact.id, group.id)
    assert contact in orm.get_add_new_in_group(group)


def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="NEW"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_add_new_list()) == 0:
        app.add_new.create(CONTACT(name="New"))
    if len(orm.get_add_new_in_group(group)) == 0:
        contact = random.choice(orm.get_add_new_list())
        app.add_new.add_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_add_new_in_group(group))
    app.add_new.remove_from_group(contact.id, group.id)
    assert contact in orm.get_add_new_not_in_group(group)














