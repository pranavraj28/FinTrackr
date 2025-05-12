from flask import Blueprint, jsonify
from ..models import Transaction
from .. import db

finance_bp = Blueprint('finance', __name__, url_prefix='/api')

@finance_bp.route('/summary')
def get_summary():
    income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type='income').scalar() or 0
    expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type='expense').scalar() or 0
    return jsonify({ 'income': income, 'expense': expense })