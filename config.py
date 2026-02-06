import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False
    
    # CORS Configuration
    CORS_ORIGINS = ['*']  # Allow all origins by default
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization']

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    CORS_ORIGINS = [
        'http://localhost:4200',  # Angular
        'http://localhost:3000',  # React
        'http://localhost:5173',  # Vite
        'http://127.0.0.1:4200',
        'http://127.0.0.1:3000',
        'http://127.0.0.1:5173',
    ]

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # In production, specify your actual frontend domains
    CORS_ORIGINS = [
        'https://your-frontend-domain.com',
        'https://api-py-flask-study.vercel.app',
    ]

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get configuration based on environment"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
