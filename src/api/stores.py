'''
exposes
/stores
'''

from flask import Blueprint, jsonify
from ..models import Store

bp = Blueprint('stores', __name__, url_prefix='/stores')

@bp.route('', methods=['GET'])
def index():
    print('hello stores')

    data = Store.query.all()

    result = []

    for d in data:
        result.append(d.serialize())

    return jsonify(result)