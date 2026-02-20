"""
Flask Web Application for Personal Safety Risk Analyzer
Provides a web interface for the safety analyzer
"""

from flask import Flask, render_template, request, jsonify
from safety_analyzer import SafetyAnalyzer, CrowdDensity
import os

app = Flask(__name__)
analyzer = SafetyAnalyzer()

# Store assessment history
assessment_history = []


@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/api/assess', methods=['POST'])
def assess_safety():
    """API endpoint for safety assessment"""
    try:
        data = request.get_json(force=True)

        # Parse input data safely
        hour = int(data.get('hour', 12))
        latitude = float(data.get('latitude', 0))
        longitude = float(data.get('longitude', 0))
        crowd_density_str = str(data.get('crowd_density', 'MEDIUM'))
        crime_score = int(data.get('crime_score', 50))
        movement_speed = float(data.get('movement_speed', 1.0))
        network_available = str(data.get('network_available', True)).lower() in ['true', '1', 'yes']

        # Convert crowd density string to enum
        crowd_density_map = {
            'LOW': CrowdDensity.LOW,
            'MEDIUM': CrowdDensity.MEDIUM,
            'HIGH': CrowdDensity.HIGH
        }
        crowd_density = crowd_density_map.get(crowd_density_str.upper(), CrowdDensity.MEDIUM)

        # Perform assessment
        assessment = analyzer.assess_safety(
            hour=hour,
            latitude=latitude,
            longitude=longitude,
            crowd_density=crowd_density,
            crime_score=crime_score,
            movement_speed=movement_speed,
            network_available=network_available
        )

        # Prepare response
        response = {
            'risk_score': assessment.risk_score,
            'risk_level': assessment.risk_level,
            'threat_reason': assessment.threat_reason,
            'recommended_action': assessment.recommended_action,
            'emergency_actions': assessment.emergency_actions or [],
            'timestamp': data.get('timestamp', ''),
            'location': {
                'latitude': latitude,
                'longitude': longitude
            }
        }

        # Add to history
        assessment_history.append(response)

        return jsonify({'success': True, 'data': response})

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get assessment history"""
    return jsonify({'success': True, 'history': assessment_history})


@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear assessment history"""
    global assessment_history
    assessment_history = []
    return jsonify({'success': True, 'message': 'History cleared'})


@app.route('/api/validate', methods=['POST'])
def validate_inputs():
    """Validate input parameters"""
    try:
        data = request.get_json(force=True)
        errors = []

        hour = int(data.get('hour', 12))
        if not (0 <= hour < 24):
            errors.append('Hour must be between 0 and 23')

        latitude = float(data.get('latitude', 0))
        if not (-90 <= latitude <= 90):
            errors.append('Latitude must be between -90 and 90')

        longitude = float(data.get('longitude', 0))
        if not (-180 <= longitude <= 180):
            errors.append('Longitude must be between -180 and 180')

        crime_score = int(data.get('crime_score', 50))
        if not (0 <= crime_score <= 100):
            errors.append('Crime score must be between 0 and 100')

        movement_speed = float(data.get('movement_speed', 1.0))
        if movement_speed < 0:
            errors.append('Movement speed must be 0 or greater')

        if errors:
            return jsonify({'success': False, 'errors': errors}), 400

        return jsonify({'success': True, 'message': 'All inputs valid'})

    except Exception:
        return jsonify({'success': False, 'error': 'Invalid input format'}), 400


if __name__ == '__main__':
    print("="*70)
    print("Personal Safety Risk Analyzer - Web Application")
    print("="*70)

    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() in ('1', 'true', 'yes')

    app.run(debug=debug, host=host, port=port)
