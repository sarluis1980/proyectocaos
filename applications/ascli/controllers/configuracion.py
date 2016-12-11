# -*- coding: utf-8 -*-
# intente algo como
#def index(): return dict(message="hello from configuracion.py")
def index():
    form=SQLFORM.smartgrid(db.tbconfigura, editable=True,deletable=True,create=True)

    response.flash="Bienvenido"

    return dict(forma=form)
