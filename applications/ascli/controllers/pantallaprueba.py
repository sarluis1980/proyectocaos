# -*- coding: utf-8 -*-
def index():
    #formulario = SQLFORM(db.hijo)
    #if formulario.process().accepted:
     #   response.flash = 'registro insertado'
    #return dict(formulario=formulario)

    form=SQLFORM.smartgrid(db.tbtmp_linea_venta, editable=True,deletable=True,create=True)

    response.flash="Bienvenido"

    return dict(forma=form)
