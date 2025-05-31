'''
exposing the following routes
/recipes
/recipes/plated
/recipes/plated/<id>
/recipes/nested
/recipes/nested/<id>
/recipes/ingredient_types
'''

from flask import Blueprint, jsonify, request
from ..models import db, RecipeNested, RecipePlated, IngredientType

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

# ALL RECIPES


@bp.route('', methods=['GET'])
def index_recipes():

    plated = RecipePlated.query.order_by(RecipePlated.id).all()
    nested = RecipeNested.query.order_by(RecipeNested.id).all()
    result = []
    for p in plated:
        result.append(p.serialize())
    for n in nested:
        result.append(n.serialize())

    return jsonify(result)

# PLATE RECIPES


@bp.route('/plated', methods=['GET'])
def index_recipes_plated():

    response = RecipePlated.query.order_by(RecipePlated.id).all()
    result = []
    for r in response:
        result.append(r.serialize())

    return jsonify(result)


@bp.route('/plated/<int:id>', methods=['GET'])
def show_plated(id: int):

    r = RecipePlated.query.get_or_404(id)

    return jsonify(r.serialize())


@bp.route('/plated', methods=['POST'])
def create_plated():

    recipe = RecipePlated(
        description=request.json['description'],
        notes=request.json['notes'],
        recipe_type=request.json['recipe_type'],
        sales_price_basis=request.json['sales_price_basis']
    )

    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.serialize()), 201


@bp.route('/plated/test-create', methods=['GET'])
def test_create_recipe_plated():

    # Define your test payload
    test_data = {
        'description': 'Test Plated Recipe',
        'notes': 'Test notes',
        'recipe_type': 'Test type',
        'sales_price_basis': 9.99
    }
    recipe = RecipePlated(
        description=test_data['description'],
        notes=test_data['notes'],
        recipe_type=test_data['recipe_type'],
        sales_price_basis=test_data['sales_price_basis']
    )
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.serialize()), 201

# NESTED RECIPES


@bp.route('/nested', methods=['GET'])
def index_recipes_nested():

    response = RecipeNested.query.order_by(RecipeNested.id).all()
    recipes = []
    for r in response:
        recipes.append(r.serialize())

    return jsonify(recipes)


@bp.route('/nested/<int:id>', methods=['GET'])
def show_nested(id: int):

    r = RecipeNested.query.get_or_404(id)

    return jsonify(r.serialize())


@bp.route('/nested', methods=['POST'])
def create_nested():

    recipe = RecipeNested(
        description=request.json['description'],
        notes=request.json['notes'],
        recipe_type=request.json['recipe_type'],
        yield_amount=request.json['yield_amount'],
        yield_uom=request.json['yield_uom']
    )

    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.serialize()), 201

# INGREDIENT TYPES


@bp.route('/ingredient_types', methods=['GET'])
def index_ingredient_types():

    response = IngredientType.query.order_by(IngredientType.id).all()
    ingredient_types = []
    for r in response:
        ingredient_types.append(r.serialize())

    return jsonify(ingredient_types)


@bp.route('/ingredient_types/<int:id>', methods=['GET'])
def show_ingredient_type(id: int):

    r = IngredientType.query.get_or_404(id)

    return jsonify(r.serialize())
