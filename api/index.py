from flask import Flask, jsonify
import sys
import os

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

VERSION = '1.0.0'
VERSION_PREFIX = f'api/v{VERSION.split(".")[0]}'

# Import blueprints
blueprints_registered = False
try:
    from src.controllers.sensors_contoller import sensors_bp
    
    # Register blueprints
    app.register_blueprint(sensors_bp, url_prefix=f'/{VERSION_PREFIX}/sensors')
    blueprints_registered = True
    print(f"Blueprints registered successfully")
except Exception as e:
    print(f"Error importing blueprints: {e}")
    import traceback
    traceback.print_exc()

@app.route('/', methods=['GET'])
def home():
    # List all registered routes
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods - {'HEAD', 'OPTIONS'}),
            'path': str(rule)
        })
    
    return jsonify({
        'message': 'Flask API - Study Project',
        'version': VERSION,
        'blueprints_loaded': blueprints_registered,
        'available_routes': routes,
        'important_endpoints': {
            'health': '/health',
            'sensors_list': f'/{VERSION_PREFIX}/sensors',
            'sensor_by_id': f'/{VERSION_PREFIX}/sensors/<id>'
        }
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'version': VERSION,
        'blueprints_loaded': blueprints_registered
    }), 200

# Debug route to test
@app.route('/debug', methods=['GET'])
def debug():
    return jsonify({
        'python_path': sys.path,
        'current_dir': os.getcwd(),
        'app_routes': [str(rule) for rule in app.url_map.iter_rules()]
    }), 200

# Vercel requires the app to be exported
# This is the entry point for Vercel
if __name__ == '__main__':
    app.run(debug=True)
