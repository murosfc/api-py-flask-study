# Deploy Guide - Vercel

## 📋 Pre-requisites

1. ✅ Git repository created and pushed to GitHub
2. ✅ Vercel account connected to GitHub
3. ✅ Project added to Vercel dashboard

## 🚀 Deployment Steps

### 1. Configure Vercel Project

In your Vercel dashboard, configure:

**Framework Preset:** Other

**Build Command:** (leave empty)

**Output Directory:** (leave empty)

**Install Command:** `pip install -r requirements.txt`

### 2. Environment Variables (Optional)

If you need environment variables, add them in the Vercel dashboard:

- Go to: Project Settings → Environment Variables
- Add variables like:
  - `FLASK_ENV=production`
  - `SECRET_KEY=your-production-secret-key`

### 3. Deploy

Vercel will automatically deploy when you push to your main branch.

Manual deploy:

```bash
git add .
git commit -m "Configure for Vercel deployment"
git push origin main
```

Or using Vercel CLI:

```bash
npm i -g vercel
vercel
```

## 📁 File Structure for Vercel

```
api-py-flask-study/
│
├── api/                      # Vercel serverless functions
│   ├── __init__.py
│   └── index.py             # Main entry point for Vercel
│
├── src/                      # Your application code
│   ├── controllers/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   └── dbs/
│
├── vercel.json              # Vercel configuration
├── requirements.txt         # Python dependencies
├── .vercelignore           # Files to ignore in deployment
└── README.md
```

## 🔍 How It Works

1. **vercel.json** tells Vercel:

   - Build the `api/index.py` file as a Python serverless function
   - Route all requests to this function

2. **api/index.py** is the entry point:

   - Contains the Flask app instance
   - Imports and registers blueprints
   - Handles all routes

3. **Serverless Functions**:
   - Each request triggers the function
   - No persistent state between requests
   - Cold starts may occur

## 🌐 Accessing Your API

After deployment, your API will be available at:

```
https://your-project-name.vercel.app
```

### Endpoints:

- **Home:** `GET /`
- **Health Check:** `GET /health`
- **Sensors API:** `GET /api/v1/sensors`

## 🐛 Troubleshooting

### Error: Module not found

**Solution:** Make sure all imports use absolute paths from project root:

```python
from src.controllers.sensors_contoller import sensors_bp
```

### Error: Build failed

**Solution:** Check that `requirements.txt` only includes production dependencies.

### Cold Starts

Serverless functions on Vercel may have cold starts (first request slower).

**Solutions:**

- Keep the function warm with periodic pings
- Use Vercel's Pro plan for better performance
- Optimize imports and initialization

## 📊 Monitoring

View logs in real-time:

- Go to Vercel Dashboard → Your Project → Deployments
- Click on a deployment → Functions → View logs

## 🔄 Continuous Deployment

Every push to `main` branch automatically triggers:

1. Build
2. Deploy
3. Run checks

To deploy from a different branch, configure in:
**Project Settings → Git → Production Branch**

## 🎯 Important Notes

- ⚠️ Vercel has a **10-second timeout** for serverless functions (hobby plan)
- ⚠️ No persistent storage - use external databases
- ⚠️ Environment is ephemeral - no file uploads persist
- ✅ Perfect for stateless REST APIs
- ✅ Automatic HTTPS
- ✅ Global CDN

## 📚 Resources

- [Vercel Python Documentation](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vercel CLI Documentation](https://vercel.com/docs/cli)
- [Flask on Vercel Guide](https://vercel.com/guides/using-flask-with-vercel)
