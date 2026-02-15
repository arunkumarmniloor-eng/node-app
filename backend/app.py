from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('itemName')
    desc = request.form.get('itemDescription')

    print("Received:", name, desc)

    return jsonify({
        "message": "Data received successfully",
        "name": name,   
        "description": desc
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
