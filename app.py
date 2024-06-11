from flask import Flask, request, jsonify
import polars as pl

app = Flask(__name__)

# Load the card data from a CSV file
card_data = pl.read_csv('card_data.csv')

# Function to analyze the deck
def analyze_deck(deck_list):
    total_weight = 0
    card_breakdown = []
    
    for line in deck_list.split('\n'):
        line = line.strip()
        if line:
            parts = line.split(None, 1)
            if len(parts) == 1:
                quantity = 1
                card_name = parts[0]
            else:
                if parts[0].isdigit():
                    quantity = int(parts[0])
                    card_name = parts[1]
                else:
                    quantity = 1
                    card_name = line
            
            card_weight = card_data.filter(pl.col('name') == card_name)['weight']
            if not card_weight.is_empty():
                weight = card_weight[0]
                total_weight += weight * quantity
                card_breakdown.append({'card': card_name, 'quantity': quantity, 'weight': weight})
    
    return total_weight, card_breakdown

@app.route('/analyze', methods=['POST'])
def analyze():
    deck_list = request.json['decklist']
    total_weight, card_breakdown = analyze_deck(deck_list)
    
    response = {
        'total_weight': total_weight,
        'card_breakdown': card_breakdown
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()