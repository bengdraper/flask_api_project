'''
exposing routes
/vendors
/vendors/items
'''

from flask import Blueprint, jsonify
from ..models import Vendor, IngredientsVendorItem

bp = Blueprint('vendors', __name__, url_prefix='/vendors')


@bp.route('', methods=['GET'])
def index():

    response = Vendor.query.order_by(Vendor.id).all()
    result = []

    for r in response:
        result.append(r.serialize())

    return jsonify(result)


@bp.route('/items', methods=['GET'])
def index_vendor_items():

    response = IngredientsVendorItem.query.order_by(
        IngredientsVendorItem.id).all()
    result = []

    for r in response:
        result.append(r.serialize())

    return jsonify(result)
