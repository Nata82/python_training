from model.contact import CONTACT

def test_modify_add_new_name(app):
    app.open_home_page()
    app.add_new.modify_first_contact(CONTACT("ededede","deded","dededed","nickname","dededed",
                    "dededed","dededede","89032012010","87451241210","87451201454","dsdsdfs@mail.ru","1985",
                    "dedededededrftrgtg","gtggtgtgtgtg","gtgrfrffrfrfrf"))


    #app.add_new.return_to_home_page()



#def test_modify_add_new_middlename(app):
 #   app.open_home_page()
  #  app.add_new.open_add_new_page()
   # app.add_new.modify_first_contact(CONTACT(middlename="New middlename"))
    #app.add_new.return_to_home_page()