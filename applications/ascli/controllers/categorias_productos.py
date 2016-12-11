# -*- coding: utf-8 -*-
# intente algo como
def index():
    form=SQLFORM.smartgrid(db.tbCategorias, editable=True,deletable=True,create=True)

    response.flash="Bienvenido"

    return dict(forma=form)
