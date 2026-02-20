# Web Frontend Setup Guide

## 🌐 Personal Safety Risk Analyzer - Web Application

A modern, responsive web interface for the Personal Safety Risk Analyzer.

## 📋 Requirements

- Python 3.8+
- Flask (`pip install flask`)
- All existing analyzer components

## 🚀 Quick Start

### Step 1: Install Flask

```bash
pip install flask
```

### Step 2: Run the Web Application

```bash
python app.py
```

You should see:
```
Personal Safety Risk Analyzer - Web Application
================================================

🌐 Starting server...
📍 Open your browser and go to: http://localhost:5000

Press Ctrl+C to stop the server
```

### Step 3: Open in Browser

Navigate to: **http://localhost:5000**

## 🎨 Features

### User-Friendly Interface
- Clean, modern design
- Responsive layout (works on desktop, tablet, mobile)
- Real-time input validation
- Visual risk indicators (🟢🟡🔴)

### Interactive Form
- Time of day picker (0-23)
- GPS coordinate input (with validation)
- Crowd density selector
- Crime score slider
- Movement speed input
- Network status toggle

### Dynamic Results Display
- Risk score (0-100) with visual emphasis
- Risk level with color coding
- Threat reason explanation
- Recommended actions
- Emergency actions (if high risk)
- Parameter summary

### Assessment History
- Track all assessments
- View timestamps
- Risk level badges
- Clear history option

## 📁 File Structure

```
safe/
├── app.py                      # Flask web application
├── templates/
│   └── index.html             # Web interface (HTML/CSS/JS)
├── safety_analyzer.py         # Core analyzer (unchanged)
└── other files...
```

## 🔧 How It Works

### Architecture

```
Browser (User Interface)
       ↓
   HTML/CSS/JavaScript
       ↓
   Flask Web Server (app.py)
       ↓
   Safety Analyzer (safety_analyzer.py)
       ↓
   Risk Assessment Results
       ↓
   JSON Response
       ↓
   Display Results in Browser
```

### API Endpoints

#### 1. POST `/api/assess`
Performs safety assessment

**Request:**
```json
{
    "hour": 23,
    "latitude": 40.7128,
    "longitude": -74.0060,
    "crowd_density": "LOW",
    "crime_score": 65,
    "movement_speed": 0.5,
    "network_available": false,
    "timestamp": "2/19/2026, 10:30:00 PM"
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "risk_score": 72,
        "risk_level": "High",
        "threat_reason": "Multiple risk factors...",
        "recommended_action": "Prioritize immediate safety...",
        "emergency_actions": ["Trigger Alarm", "Send SOS", ...],
        "location": {"latitude": 40.7128, "longitude": -74.0060}
    }
}
```

#### 2. GET `/api/history`
Retrieves assessment history

**Response:**
```json
{
    "success": true,
    "history": [...]
}
```

#### 3. POST `/api/clear-history`
Clears assessment history

**Response:**
```json
{
    "success": true,
    "message": "History cleared"
}
```

#### 4. POST `/api/validate`
Validates input parameters

**Request:**
```json
{
    "hour": 25,
    "latitude": 100,
    "longitude": 200,
    "crime_score": 150,
    "movement_speed": -5
}
```

**Response:**
```json
{
    "success": false,
    "errors": [
        "Hour must be between 0 and 23",
        "Latitude must be between -90 and 90",
        ...
    ]
}
```

## 🎯 User Guide

### Assessing Safety

1. **Enter Time of Day** (0-23)
   - 0-6: Night (higher risk)
   - 6-21: Day (lower risk)
   - 21-23: Evening (increasing risk)

2. **Enter Location**
   - Latitude: -90 to 90
   - Longitude: -180 to 180
   - Example: NYC = 40.7128, -74.0060

3. **Select Crowd Density**
   - Low: Isolated areas
   - Medium: Normal population
   - High: Crowded areas (safer)

4. **Enter Crime Score** (0-100)
   - 0-30: Safe area
   - 30-70: Moderate crime
   - 70-100: High crime area

5. **Enter Movement Speed** (≥0)
   - 0 = Stationary
   - 1-3 = Walking
   - 5+ = Vehicle/fast movement

6. **Select Network Status**
   - Connected: Can reach help
   - Not Connected: Isolated

7. **Click "Assess Safety"**

### Understanding Results

**Risk Score (0-100)**
- Visual representation of overall risk
- Color-coded for quick assessment

**Risk Level**
- 🟢 **Low (0-30)**: Safe environment
- 🟡 **Medium (31-60)**: Increased caution
- 🔴 **High (61-100)**: Urgent action needed

**Threat Reason**
- Explains which factors increased risk
- Helps you understand the situation

**Recommended Action**
- Specific guidance based on risk level
- Actionable steps to take

**Emergency Actions** (High Risk Only)
- Trigger Alarm
- Send SOS
- Flashlight Activation
- Move to safer area
- Contact authorities

### Tracking History

All assessments are saved and displayed in chronological order:
- View past assessments
- See trends over time
- Clear history when desired

## 🛠️ Configuration

### Change Port

Edit `app.py` line at the bottom:

```python
app.run(debug=True, host='localhost', port=8000)  # Change 5000 to 8000
```

### Enable Remote Access

Change `localhost` to `0.0.0.0`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Then access from other machines at: `http://[your-ip]:5000`

### Disable Debug Mode (Production)

```python
app.run(debug=False, host='localhost', port=5000)
```

## 📦 Deployment

### Local Network

```bash
python app.py
# Access from other computers: http://[your-computer-ip]:5000
```

### Using Gunicorn (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t safety-analyzer .
docker run -p 5000:5000 safety-analyzer
```

## 🔒 Security Notes

### Current Status (Development)
- Debug mode enabled (development only)
- No authentication
- No HTTPS
- Local only by default

### Production Recommendations
1. Disable debug mode
2. Add authentication if exposing publicly
3. Use HTTPS with SSL certificate
4. Set strong CORS policy
5. Add rate limiting
6. Implement input sanitization
7. Use production-grade server (Gunicorn, uWSGI)

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find process using port 5000
lsof -i :5000

# Change port in app.py to different number (e.g., 8000)
```

### Flask Not Found

```bash
pip install flask
```

### Template Not Found Error

Ensure `templates` folder exists with `index.html` inside:
```
safe/
├── app.py
├── templates/
│   └── index.html
└── ...
```

### CSS/JS Not Loading

Clear browser cache (Ctrl+Shift+Delete) and refresh page.

## 📊 Example Workflows

### Scenario 1: Quick Safety Check
1. Use default values as starting point
2. Adjust only necessary parameters
3. Click "Assess Safety"
4. View instant results

### Scenario 2: Commute Tracking
1. Fill in your current location and time
2. Select appropriate options
3. Track multiple points during journey
4. View history for pattern analysis

### Scenario 3: Emergency Planning
1. Test different high-risk scenarios
2. Compare results
3. Plan safety responses
4. Use emergency actions as guide

## 🔗 Integration

The web app integrates seamlessly with:
- `safety_analyzer.py` - Core engine (unchanged)
- `SafetyAnalyzer` class - Risk calculations
- `CrowdDensity` enum - Valid options

All existing Python code continues to work as before.

## 📝 Browser Compatibility

✓ Chrome/Chromium 90+
✓ Firefox 88+
✓ Safari 14+
✓ Edge 90+
✓ Mobile browsers (iOS Safari, Chrome Mobile)

## 🎉 Next Steps

1. Run Flask app
2. Open http://localhost:5000
3. Fill in your information
4. Get instant safety assessment
5. Track history over time

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Review Flask documentation
3. Verify analyzer works: `python safety_analyzer.py`
4. Check browser console for errors (F12)

---

**Enjoy the web interface! Stay safe! 🛡️**
