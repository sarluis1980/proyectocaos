# -*- coding: utf-8 -*-
# Create a database named 'person' with 'last_name' and 'first_name' fields.
# web2py also creates a field named 'id' automatically.
db.define_table('person',Field('last_name'), Field('first_name'))
 
# If no database exists, generate a database of 101 unique records
# with names in the form John1 Smith1, John43 Smith43, etc.
if db(db.person).isempty():
    for eachName in range(101):
        nextNumber=str(eachName)
        db.person.update_or_insert(last_name='Smith'+nextNumber,first_name='John'+nextNumber)
