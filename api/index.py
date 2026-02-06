from flask import Flask, jsonify

app = Flask(__name__)

VERSION = '1.0.0'
VERSION_PREFIX = f'api/v{VERSION.split(".")[0]}'

# Import blueprints
try:
    from src.controllers.sensors_contoller import sensors_bp
    
    blueprints = [
        {'blueprint': sensors_bp, 'url_prefix': f'/{VERSION_PREFIX}/sensors'},
    ]
    
    for blueprint in blueprints:
        app.register_blueprint(blueprint['blueprint'], url_prefix=blueprint['url_prefix'])
except Exception as e:
    print(f"Warning: Could not import blueprints: {e}")

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Flask API - Study Project',
        'version': VERSION,
        'endpoints': {
            'health': '/health',
            'sensors': f'/{VERSION_PREFIX}/sensors'
        }
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'version': VERSION}), 200

# Vercel requires the app to be exported
# This is the entry point for Vercel
if __name__ == '__main__':
    app.run(debug=True)
