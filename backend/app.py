from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from database.database import init_db, db
from datetime import datetime
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Import blueprints
from routes.face_routes import face_bp

load_dotenv()


def create_app():
    """Application factory function"""

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions FIRST
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    init_db(app)
    Config.init_app(app)

    migrate = Migrate(app, db)

    # Import routes
    from routes.auth_routes import auth_bp
    from routes.chat_routes import chat_bp
    from routes.photo_routes import photo_bp
    from routes.delivery_routes import delivery_bp
    from routes.history_routes import history_bp
    from routes.edit_routes import edit_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    app.register_blueprint(photo_bp, url_prefix='/api/photos')
    app.register_blueprint(delivery_bp, url_prefix='/api/delivery')
    app.register_blueprint(history_bp, url_prefix='/api/history')
    app.register_blueprint(edit_bp, url_prefix='/api/edit')
    app.register_blueprint(face_bp, url_prefix='/api/face')

    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({
            "status": "healthy",
            "app": "Drishyamitra",
            "timestamp": datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }), 200

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500

    # Request logging
    @app.before_request
    def log_request():
        app.logger.info(
            f"{request.method} {request.path} - {request.remote_addr}"
        )

    return app