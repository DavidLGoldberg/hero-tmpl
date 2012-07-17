from flask import current_app
from pymongo import Connection
import json

connection = Connection()
db = connection.btst

####################################
# *One offs*

# NOTE only use these if the 
# get_collection() won't work!
####################################
# Example one off / special case:
#def return_all_from_collection_the_wrong_way():
#    return list(db.<col>.find())

####################################
# *Collections*
####################################
def get_collections():
    return db.collection_names()

def get_collection(action, args):
    query = dict()

    # TODO: better to pull in as one object so that can json.loads just once..
    # also might simplify code a bit...

    for restriction, value in args.iteritems():
        current_app.logger.debug(restriction + ': ' + value)
        params = dict(json.loads(value))
        for k, v in params.iteritems():
            if k in query:
                raise Exception('same field should not exist in includes and excludes')
            query[k] = v if restriction == 'inc' else {'$ne': v}

    return query, list(db[action].find(query))
