# -*- coding: utf-8 -*-
# intente algo como
def index():
    import json
    # Select all the records, to show how
    # datatables.net paginates.
    # Rows can't be serialized because they contain
    # an open database connection. Use as_list()
    # to serialize the query result.
    people = json.dumps(db(db.person).select().as_list())
    return dict(results=XML(people))
