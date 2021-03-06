import pymysql.cursors
from model.group import Group
from model.contact import CONTACT


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            self.connection.commit()
            cursor.close()
        return list

    # def get_contact_list(self):
    #     list = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
    #         for row in cursor:
    #             (id, firstname, lastname) = row
    #             list.append(CONTACT(id=str(id), firstname=firstname, lastname=lastname))
    #     finally:
    #         cursor.close()
    #     return list



    def get_add_new_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname, address, email, email2, email3,'
                           'home, mobile, work, fax, phone2 from addressbook where deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, phone2) = row
                list.append(CONTACT(id=str(id), name=firstname, lastname=lastname, address=address, email=email,
                                email2=email2, email3=email3, home=home, mobile=mobile, work=work, fax=fax,
                                phone2=phone2))
        finally:
            self.connection.commit()
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
