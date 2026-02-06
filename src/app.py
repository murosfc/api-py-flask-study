from flask import Flask, jsonify

app = Flask(__name__)


VERSION = '1.0.0'
VERSION_PREFIX = f'api/v{VERSION.split(".")[0]}'

blueprints = [
    {'blueprint': 'sensors_bp', 'url_prefix': f'/{VERSION_PREFIX}/sensors'},
]

for blueprint in blueprints:
    app.register_blueprint(blueprint.blueprint, url_prefix=blueprint.url_prefix)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'version': VERSION}), 200

if __name__ == '__main__':
    app.run(debug=True)