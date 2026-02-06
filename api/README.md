# API Directory

This directory contains the Vercel serverless function entry point.

## Files

- `index.py` - Main entry point for Vercel deployment
- `__init__.py` - Makes this directory a Python package

## How it works

Vercel treats this directory as serverless functions. The `index.py` file exports the Flask app instance which Vercel uses to handle all incoming requests.

All routes defined in your Flask app (in `src/`) are automatically available through this entry point.
