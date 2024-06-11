# Deck Analyzer API

This project is a simple Flask-based API to analyze a deck of cards. It reads card data from a CSV file and provides an endpoint to analyze the total weight of the deck and break down the individual card weights.

## Requirements

- Python >= 3.8
- Flask
- Polars

## Installation

    git clone https://github.com/yourusername/deck-analyzer.git
    cd deck-analyzer
    pip install -r requirements.txt

## Usage

Run the Flask application:

    python app.py

Send a POST request to the /analyze endpoint with the deck list in JSON format. The decklist field should contain the deck list as a string. Each line should contain either the card name or the quantity followed by the card name.

## Example Deck List
- Thalia and The Gitrog Monster
- Ambitious Farmhand
- Anguished Unmaking
- Arboreal Grazer

Example Request


```
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"decklist": "Thalia and The Gitrog Monster\nDeck\nAmbitious Farmhand\n Anguished Unmaking\n Arboreal Grazer\n Island"}'
```
Example Response

```json
{
    "card_breakdown": [
        {
            "card": "Thalia and The Gitrog Monster",
            "quantity": 1,
            "weight": 9
        },
        {
            "card": "Ambitious Farmhand",
            "quantity": 1,
            "weight": 18
        },
        {
            "card": "Anguished Unmaking",
            "quantity": 1,
            "weight": 15
        },
        {
            "card": "Arboreal Grazer",
            "quantity": 1,
            "weight": 9
        }
    ],
    "total_weight": 51
}
```