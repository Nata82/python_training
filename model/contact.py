from sys import maxsize

class CONTACT:
    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 mobile=None, work=None, fax=None, email=None, byear=None, address2=None, phone2=None, notes=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id



    def __repr__(self):
        return "%s %s %s" % (self.id, self.name,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize