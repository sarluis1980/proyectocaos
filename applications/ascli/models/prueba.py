# -*- coding: utf-8 -*-
#db = DAL("sqlite://db.db")
db.define_table('hijo',
     Field('nombre'),
     Field('peso', 'double'),
     Field('fecha_nacimiento', 'double'),
     Field('hora_nacimiento', 'double'))

db.hijo.nombre.requires=IS_NOT_EMPTY()
db.hijo.peso.requires=IS_FLOAT_IN_RANGE(0,100)
#db.hijo.fecha_nacimiento.requires=IS_DATE()
#db.hijo.hora_nacimiento.requires=IS_TIME()
