from flask import Blueprint, jsonify
from utils.functions import get_card_flag

bp_info_card = Blueprint('info_card', __name__)


@bp_info_card.route('/checkCard/<string:card_number>', methods=['POST'])
def verify_creditCard(card_number):
    try:
        bandeira = get_card_flag(card_number)

        if bandeira is False:
            return jsonify({'card_number': card_number, 'is_valid': False}), 200
        
        if bandeira == -1:
            return jsonify({'card_number': card_number, 'flag': 'not found'}), 200
        
        if bandeira:
            return jsonify({'card_number': card_number, 'is_valid': True, 'flag': bandeira}), 200
    

    except:
        return 'Server Error:', 500
