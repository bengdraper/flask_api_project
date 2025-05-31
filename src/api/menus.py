'''
exposing the following routes
/menus
'''

from flask import Blueprint, jsonify
from ..models import Menu

bp = Blueprint('menus', __name__, url_prefix='/menus')


@bp.route('', methods=['GET'])
def index():

    menus = Menu.query.order_by(Menu.id).all()
    result = []

    for m in menus:
        result.append(m.serialize())

    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):

    r = Menu.query.get_or_404(id)

    return jsonify(r.serialize())