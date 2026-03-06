# Drishyamitra

## Project Structure

    drishyamitra/
    │
    ├── backend/
    │   ├── app.py                  # Flask application factory
    │   ├── start_server.py         # Development server entry point
    │   ├── run_production.py       # Production server script
    │   ├── config.py               # Application configuration
    │   ├── requirements.txt        # Python dependencies
    │   ├── .env.example            # Example environment variables
    │
    │   ├── models/                 # Database models
    │   │
    │   ├── routes/                 # API route blueprints
    │   │   ├── auth_routes.py
    │   │   ├── chat_routes.py
    │   │   ├── photo_routes.py
    │   │   ├── delivery_routes.py
    │   │   ├── history_routes.py
    │   │   ├── edit_routes.py
    │   │   └── face_routes.py
    │
    │   ├── services/               # Business logic (to be implemented)
    │   │   └── __init__.py
    │
    │   ├── utils/                  # Helper utilities
    │   │
    │   ├── database/               # Database initialization
    │   │
    │   ├── migrations/             # Database migration scripts
    │   │
    │   └── data/                   # File storage
    │       ├── photos/             # Uploaded images
    │       ├── faces/              # Cropped face images
    │       └── delivery_photos/    # Temporary delivery files
    │
    └── frontend/
        ├── public/
        ├── src/
        │   ├── App.jsx
        │   ├── components/
        │   ├── services/
        │   └── utils/
    │
        ├── package.json
        ├── package-lock.json
        └── .env

------------------------------------------------------------------------

# Backend Setup

### 1. Navigate to backend

    cd backend

### 2. Create virtual environment

    python3 -m venv venv

### 3. Activate virtual environment

Mac / Linux

    source venv/bin/activate

Windows

    venv\Scripts\activate

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Configure environment variables

Create `.env` file:

    cp .env.example .env

Example `.env` values:

    SECRET_KEY=your-secret-key
    DATABASE_URL=sqlite:///database/drishyamitra.db
    GROQ_API_KEY=your-groq-api-key
    GMAIL_EMAIL=your-email@gmail.com
    GMAIL_PASSWORD=your-app-password
    JWT_SECRET_KEY=your-jwt-secret-key

### 6. Run backend server

    python start_server.py

Backend runs on:

    http://localhost:5001

Test endpoint:

    http://localhost:5001/api/health

------------------------------------------------------------------------

# Frontend Setup

### 1. Navigate to frontend

    cd frontend

### 2. Install dependencies

    npm install

### 3. Configure environment variables

Create `.env` file:

    REACT_APP_API_URL=http://localhost:5001

### 4. Run frontend

    npm start

Frontend runs on:

    http://localhost:3000

------------------------------------------------------------------------

# Running the Project

Start backend first:

    cd backend
    source venv/bin/activate
    python start_server.py

Start frontend:

    cd frontend
    npm start

Open:

    http://localhost:3000

------------------------------------------------------------------------

# Development Notes

-   Backend APIs are available under `/api/*`
-   Services layer will contain business logic (face recognition,
    delivery, chat).
-   Frontend communicates with backend using Axios through
    `REACT_APP_API_URL`.
