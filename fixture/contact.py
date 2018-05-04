from model.contact import CONTACT


class CONTACTHelper:

    def __init__(self, app):
        self.app = app


    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(
                wd.find_element_by_xpath("//input[@value='Send e-Mail']")) > 0):
           wd.find_element_by_link_text("home").click()

    def create(self, add_new):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(add_new)
        # press enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, add_new):
        wd = self.app.wd
        self.change_field_value("firstname", add_new.name)
        self.change_field_value("middlename", add_new.middlename)
        self.change_field_value("lastname", add_new.lastname)
        self.change_field_value("nickname", add_new.nickname)
        self.change_field_value("title", add_new.title)
        self.change_field_value("company", add_new.company)
        self.change_field_value("address", add_new.address)
        self.change_field_value("mobile", add_new.mobile)
        self.change_field_value("work", add_new.work)
        self.change_field_value("fax", add_new.fax)
        self.change_field_value("email", add_new.email)
        self.change_field_value("byear", add_new.byear)
        self.change_field_value("address2", add_new.address2)
        self.change_field_value("phone2", add_new.phone2)
        self.change_field_value("notes", add_new.notes)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()



    def delete_first_add_new(self):
        self.delete_add_new_by_index(0)



    def delete_add_new_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_add_new_page()
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def mod_add_new(self):
        wd = self.app.wd
        # select first add_new
        wd.find_element_by_name("selected[]").click()
        #нажимаем на редактирование
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def modifyok_first_add_new(self):
        self.modifyok_add_new_by_index(0)



    def modifyok_contact_by_index(self, index, new_contact_data):
        #заходим на страницу home page
        wd = self.app.wd
        # wd.find_element_by_name("selected[]").click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        #модификация
        self.fill_contact_form(new_contact_data)
        #подтверждаю изменения
        wd.find_element_by_name("update").click()
        #возвращаемся на страницу
        self.return_to_home_page()
        self.contact_cache = None


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def count(self):
        wd = self.app.wd
        self.open_add_new_page()
        return len(wd.find_elements_by_name("selected[]"))




    contact_cache = None


    def get_add_new_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_xpath(".//td[2]").text
                name = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(CONTACT(lastname=lastname, name=name, id=id))
        return list(self.contact_cache)







