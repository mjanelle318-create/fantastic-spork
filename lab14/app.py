
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# IN-MEMORY DATABASE
items = {}


# HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# CREATE AN ITEM
@app.route('/items', methods=['POST'])
def create_item():

    data = request.get_json()

    item_id = str(len(items) + 1)

    items[item_id] = data

    return jsonify({
        'id': item_id,
        'item': data
    }), 201


# GET ALL ITEMS
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# READ, UPDATE, DELETE SINGLE ITEM
@app.route('/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(item_id):

    item = items.get(item_id)

    # READ
    if request.method == 'GET':

        if not item:
            return jsonify({'Error': 'Item not found'}), 404

        return jsonify(item)

    # UPDATE
    elif request.method == 'PUT':

        if not item:
            return render_template(
                'error.html',
                message="NOT FOUND",
                item=item
            ), 404

        data = request.get_json()

        if not data:
            return jsonify({'error': 'Invalid input'}), 400

        items[item_id] = data

        return render_template(
            'update.html',
            item_id=item_id,
            item=data
        )

    # DELETE
    elif request.method == 'DELETE':

        if not item:
            return jsonify({'error': 'Item not found'}), 404

        deleted_item = items.pop(item_id)

        return render_template(
            'delete.html',
            item_id=item_id,
            deleted_item=deleted_item
        )


# RUN APPLICATION
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

