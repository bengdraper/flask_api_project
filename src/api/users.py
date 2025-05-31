'''
exposes
/users
/users/id
'''

from flask import Blueprint, jsonify
from ..models import User


bp = Blueprint('users', __name__, url_prefix='/users')
@bp.route('', methods=['GET'])
def index():

    users = User.query.order_by(User.id).all()
    result = []

    for u in users:
        result.append(u.serialize())

    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):

    u = User.query.get_or_404(id)

    return jsonify(u.serialize())
