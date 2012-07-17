from flask import Blueprint, request, make_response, current_app
api = Blueprint('api', __name__)

from flask.ext.security import roles_required
from bson  import json_util
import json

import actions

collections = actions.get_collections()

@api.errorhandler(404)
def page_not_found(error):
    return error, 404

def fetch_context(action, args):
    if action in actions.__dict__:
        query, result = actions.__dict__[action]()
    elif action in collections:
        query, result = actions.get_collection(action, args)
    else:
        return page_not_found('no action or collection found')

    return query, {'data': { action : result}}

@api.route('/api/<action>')
@roles_required('admin')
def execute(action):
    query, result = fetch_context(action, request.args)

    response = make_response(json.dumps(result, default=json_util.default))

    if current_app.debug:
        current_app.logger.debug('query: ' + str(query))
        response.headers['X-HT-Query'] = query

    return response
