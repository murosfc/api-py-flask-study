# CORS Configuration Guide

## What is CORS?

CORS (Cross-Origin Resource Sharing) is a security feature that controls which domains can access your API. Without CORS properly configured, browsers will block requests from your frontend to your API if they're on different domains.

## Current Configuration

The API is configured with Flask-CORS to handle cross-origin requests.

### Development Environment

In development mode, the following origins are allowed:

```
http://localhost:4200  (Angular default)
http://localhost:3000  (React default)
http://localhost:5173  (Vite default)
http://127.0.0.1:4200
http://127.0.0.1:3000
http://127.0.0.1:5173
```

### Production Environment

For production (Vercel), you should specify your actual frontend domain in `config.py`:

```python
class ProductionConfig(Config):
    CORS_ORIGINS = [
        'https://your-frontend-domain.com',
        'https://your-app.vercel.app',
    ]
```

## Configuration Files

### 1. `config.py`

Contains environment-specific configurations:
- `DevelopmentConfig` - For local development
- `ProductionConfig` - For Vercel/production
- `TestingConfig` - For running tests

### 2. `api/index.py`

Loads the configuration and applies CORS settings:

```python
from flask_cors import CORS
from config import get_config

app.config.from_object(get_config())
CORS(app, resources={
    r"/*": {
        "origins": app.config['CORS_ORIGINS'],
        "methods": app.config['CORS_METHODS'],
        "allow_headers": app.config['CORS_ALLOW_HEADERS']
    }
})
```

## Allowed HTTP Methods

- GET
- POST
- PUT
- DELETE
- OPTIONS (required for preflight requests)

## Allowed Headers

- Content-Type
- Authorization

## Testing CORS

### Using curl

```bash
curl -H "Origin: http://localhost:4200" \
     -H "Access-Control-Request-Method: GET" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -X OPTIONS \
     http://localhost:5000/api/v1/sensors/
```

### Using Browser Console

```javascript
fetch('http://localhost:5000/api/v1/sensors/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('CORS Error:', error));
```

### Expected Response Headers

When CORS is properly configured, you should see these headers in the response:

```
Access-Control-Allow-Origin: http://localhost:4200
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
```

## Common CORS Errors

### Error: "No 'Access-Control-Allow-Origin' header"

**Cause:** CORS is not configured or the origin is not in the allowed list.

**Solution:** 
1. Make sure Flask-CORS is installed: `pip install Flask-CORS`
2. Check that your origin is in `CORS_ORIGINS` in `config.py`
3. Restart the Flask server

### Error: "Preflight request doesn't pass access control check"

**Cause:** OPTIONS method is not allowed or headers are not permitted.

**Solution:**
- Ensure OPTIONS is in `CORS_METHODS`
- Add required headers to `CORS_ALLOW_HEADERS`

## Security Best Practices

### ✅ DO:

1. **Specify exact origins in production:**
   ```python
   CORS_ORIGINS = ['https://your-app.com']
   ```

2. **Limit allowed methods:**
   ```python
   CORS_METHODS = ['GET', 'POST']  # Only what you need
   ```

3. **Use environment variables for sensitive configs**

### ❌ DON'T:

1. **Never use `origins: "*"` in production:**
   ```python
   # BAD for production
   CORS_ORIGINS = ['*']
   ```

2. **Don't allow all headers:**
   ```python
   # BAD - too permissive
   CORS_ALLOW_HEADERS = ['*']
   ```

3. **Don't expose sensitive headers**

## Environment Variables

You can override CORS settings using environment variables:

```bash
# .env file
CORS_ORIGINS=http://localhost:4200,https://your-app.com
```

Then in `config.py`:

```python
CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:4200').split(',')
```

## Vercel Deployment

When deploying to Vercel, set the environment variable:

1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add: `FLASK_ENV=production`
3. Add: `CORS_ORIGINS=https://your-frontend-domain.com`
4. Redeploy

## Troubleshooting

### Check if CORS is working:

```bash
# Should return CORS headers
curl -I -X OPTIONS http://localhost:5000/api/v1/sensors/
```

### View CORS configuration:

Visit `http://localhost:5000/debug` to see current configuration (in development only).

## Resources

- [Flask-CORS Documentation](https://flask-cors.readthedocs.io/)
- [MDN CORS Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Understanding CORS](https://web.dev/cross-origin-resource-sharing/)
