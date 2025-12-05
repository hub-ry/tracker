# Weight Tracker

## Overview
A simple weight tracking application with a Flask REST API interface. The application allows users to track their weight over time using a file-based storage system. Originally created to track winter 2025 bulk progress.

**Current State**: Fully functional Flask API running on Replit, configured for deployment.

**Version**: 2.0

## Recent Changes (December 1, 2025)
- Imported from GitHub repository (hub-ry/tracker)
- Configured for Replit environment
- Updated Flask API to run on port 5000 (required for Replit webview)
- Added root endpoint (/) showing API information and available endpoints
- Configured deployment settings for autoscale deployment
- Added Python .gitignore

## Project Architecture

### Structure
```
.
├── src/
│   └── weight_tracker/
│       ├── __init__.py          # Package initialization
│       ├── api.py               # Flask REST API server
│       └── cli.py               # Command-line interface (deprecated)
├── pyproject.toml               # Python project configuration
├── weight.txt                   # Data storage file
└── README.md                    # Project documentation
```

### Components

#### Flask REST API (`src/weight_tracker/api.py`)
- **Port**: 5000 (configured for Replit)
- **Host**: 0.0.0.0 (allows external connections)
- **Endpoints**:
  - `GET /` - API information and endpoint listing
  - `POST /add_weight` - Add a new weight entry (expects JSON: `{"weight": value}`)
  - `GET /get_weights` - Retrieve all weight entries

#### CLI Interface (`src/weight_tracker/cli.py`)
- Interactive menu for adding weights, viewing data, and displaying graphs
- Uses matplotlib for data visualization
- Note: Not actively used in the Replit deployment

### Data Storage
- **Format**: Plain text file (`weight.txt`)
- **Structure**: Each line contains: `YYYY-MM-DD, weight`
- **Location**: Project root directory

## Dependencies
- **flask** >= 2.0 - Web framework for REST API
- **matplotlib** >= 3.5 - Plotting library for data visualization
- **gunicorn** >= 23.0 - Production WSGI HTTP server

## Running the Application

### Development (Replit)
The Flask API starts automatically via the configured workflow using gunicorn with 2 workers.

### Manual Start (Production)
```bash
gunicorn --bind 0.0.0.0:5000 --workers 2 weight_tracker.api:app
```

### Manual Start (Development)
```bash
python src/weight_tracker/api.py
```

### Using the API

#### Add a weight entry
```bash
curl -X POST http://localhost:5000/add_weight \
  -H "Content-Type: application/json" \
  -d '{"weight": 175.5}'
```

#### Get all weight entries
```bash
curl http://localhost:5000/get_weights
```

## Deployment
Configured for autoscale deployment on Replit using gunicorn as the production WSGI server. The deployment runs with 2 worker processes for better performance and reliability.

**Deployment Command**: `gunicorn --bind 0.0.0.0:5000 --workers 2 weight_tracker.api:app`

## User Preferences
None specified yet.

## Notes
- The application uses gunicorn as the production WSGI server for security and performance
- Data persists in `weight.txt` file
- The CLI interface includes a matplotlib graphing feature for visualizing weight trends
- Debug mode is disabled in production for security
