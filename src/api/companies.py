'''
exposes
/companies
'''

from flask import Blueprint, jsonify
from ..models import Company

bp = Blueprint('companies', __name__, url_prefix='/companies')


@bp.route('', methods=['GET'])
def index():
    print('hello companies')

    data = Company.query.all()

    result = []

    for d in data:
        result.append(d.serialize())

    return jsonify(result)
