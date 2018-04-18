from model.group import Group

def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_group()
    app.group.create(Group(name="hjhj", header="jhjhjh", footer="jhjhhj"))
    app.session.logout()