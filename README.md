# Personal Safety Risk Analyzer

A comprehensive system for evaluating personal safety based on environmental and situational factors.

## Overview

The Personal Safety Risk Analyzer uses machine learning principles to assess safety levels by analyzing:
- **Time of Day** (21:00–06:00 is considered night)
- **Location Context** (GPS coordinates validation)
- **Crowd Density** (Low/Medium/High)
- **Area Crime History** (0–100 score)
- **User Movement** (speed tracking)
- **Network Connectivity** (availability status)

## Files

### 1. `safety_analyzer.py` (Core Engine)
The main safety analysis module with the `SafetyAnalyzer` class.

**Key Components:**
- `SafetyAssessment` dataclass: Holds risk assessment results
- `SafetyAnalyzer` class: Performs all risk calculations
- Risk scoring algorithm with weighted factors
- Input validation

**Risk Level Scale:**
- **Low (0–30)**: Safe environment, normal activities recommended
- **Medium (31–60)**: Caution advised, increase awareness
- **High (61–100)**: Immediate safety concerns, emergency actions needed

### 2. `interactive_analyzer.py` (Interactive CLI)
User-friendly command-line interface for real-time assessments.

**Features:**
- Interactive input collection with validation
- Visual risk level indicators (🟢/🟡/🔴)
- Emergency action recommendations for high-risk scenarios
- Loop for multiple assessments

### 3. `test_analyzer.py` (Unit Tests)
Comprehensive test suite validating all analyzer functions.

## Usage

### Method 1: Interactive CLI (Recommended for Manual Use)

```bash
python interactive_analyzer.py
```

**Steps:**
1. Enter current time (0–23 hours)
2. Provide GPS coordinates (latitude/longitude)
3. Select crowd density level
4. Enter area crime history score (0–100)
5. Input movement speed
6. Specify network availability

**Output:**
```
Risk Score: 47/100
Risk Level: 🟡 Medium
Threat Reason: Multiple risk factors: night hours, low crowd density
Recommended Action: Increase vigilance. Consider moving to a safer area...
```

### Method 2: Direct Python API

```python
from safety_analyzer import SafetyAnalyzer, CrowdDensity

analyzer = SafetyAnalyzer()

assessment = analyzer.assess_safety(
    hour=23,
    latitude=40.7128,
    longitude=-74.0060,
    crowd_density=CrowdDensity.LOW,
    crime_score=65,
    movement_speed=0.5,
    network_available=False
)

print(assessment)
```

### Method 3: Example Scenarios

Run the built-in demos:

```bash
python safety_analyzer.py
```

This demonstrates:
1. **Low Risk**: Safe daytime scenario
2. **Medium Risk**: Night with low crowd density
3. **High Risk**: Dangerous isolated situation
4. **Edge Case**: Invalid GPS coordinates

### Method 4: Run Test Suite

```bash
python test_analyzer.py
```

Executes all unit tests validating:
- Risk factor calculations
- Coordinate validation
- Edge cases
- Risk scoring algorithm

## Risk Factor Weights

The analyzer uses weighted factors to calculate final risk score:

| Factor | Weight | Impact |
|--------|--------|--------|
| Crime History | 25% | Most significant impact |
| Movement Speed | 20% | Stationary increases risk |
| Night Time | 15% | High-risk hours |
| Crowd Density | 15% | Isolation increases risk |
| GPS Validity | 15% | Unknown location increases risk |
| Network | 10% | No connectivity increases risk |

## Risk Assessment Rules

1. **Night Time (21:00–06:00)**: +15 risk points
2. **Low Crowd Density**: +15 risk points
3. **High Crime Score**: Up to +25 risk points (scales with score)
4. **No Network**: +10 risk points
5. **Zero/Low Movement**: +20 risk points (especially in crime areas)
6. **Invalid GPS**: +15 risk points

## Emergency Actions (High Risk Only)

When risk score exceeds 60, recommended actions include:
- 🚨 **Trigger Alarm**
- 📱 **Send SOS to emergency contacts**
- 🔦 **Flashlight Activation**
- 🏃 **Move to safer area immediately**
- 📞 **Contact local authorities if needed**

## Example Outputs

### Scenario 1: Safe Hour
```
Hour: 14 (2 PM)
Location: Times Square, NYC
Crowd: High
Crime: Low
Speed: Moving
Network: Connected

Result → Risk Score: 15 | LOW RISK ✓
```

### Scenario 2: Risky Conditions
```
Hour: 2 (2 AM)
Location: Remote area
Crowd: Low
Crime: High (80/100)
Speed: Stationary (0)
Network: Unavailable

Result → Risk Score: 80 | HIGH RISK ⚠️
Emergency: Call police, activate alarm
```

## API Reference

### SafetyAnalyzer.assess_safety()

```python
def assess_safety(
    hour: int,                           # 0-23
    latitude: float,                     # -90 to 90
    longitude: float,                    # -180 to 180
    crowd_density: CrowdDensity,        # LOW/MEDIUM/HIGH
    crime_score: int,                    # 0-100
    movement_speed: float,               # >= 0
    network_available: bool              # True/False
) -> SafetyAssessment
```

**Returns:** `SafetyAssessment` with:
- `risk_score` (int): 0-100
- `risk_level` (str): "Low" / "Medium" / "High"
- `threat_reason` (str): Explanation of detected risks
- `recommended_action` (str): Actionable guidance
- `emergency_actions` (list): Actions for high risk

## Input Validation

| Parameter | Valid Range | Invalid Behavior |
|-----------|------------|-----------------|
| Hour | 0-23 | Returns risk score (0.5 modifier) |
| Latitude | -90 to 90 | Marks as invalid GPS +15 risk |
| Longitude | -180 to 180 | Marks as invalid GPS +15 risk |
| Crime Score | 0-100 | Returns risk score (0.5 modifier) |
| Movement Speed | ≥ 0 | Returns risk score (0.5 modifier) |

## Safety Tips

✓ **Best Practices:**
- Check assessments regularly in unfamiliar areas
- Trust the high-risk warnings
- Move to well-lit, populated areas when alerted
- Keep network enabled for emergency connectivity
- Share your location with trusted contacts
- Maintain awareness of surroundings

## Technology Stack

- **Language**: Python 3.8+
- **Dependencies**: None (Standard library only)
- **Architecture**: Object-oriented design with dataclasses
- **Testing**: Built-in unittest framework

## Deploying on Render.com

Quick steps to deploy this app on Render:

1. Create a GitHub repository and push this project (root should contain `app.py`, `requirements.txt`, `Procfile`, and `render.yaml`).
2. Sign in to https://render.com and create a new Web Service.
    - Connect your GitHub repo and select the branch to deploy (e.g., `main`).
    - Render will detect a Python service; use the build command `pip install -r requirements.txt` and the start command `gunicorn app:app --workers 3 --bind 0.0.0.0:$PORT`.
3. Render sets the `PORT` environment variable automatically; the app honors it. Optionally set `FLASK_DEBUG=true` while testing.
4. Deploy — Render will install dependencies and start the service.

You can also use the provided `render.yaml` for Render's Infrastructure as Code. Place it in the repo root and Render can import the service configuration.

Notes:
- Ensure `requirements.txt` includes `Flask` and `gunicorn` (this repo includes them).
- For production, disable debug mode and enable HTTPS.

## Future Enhancements

- Integration with real-time crime data APIs
- Mobile app version with GPS tracking
- Machine learning predictions based on historical data
- Multi-modal alerts (SMS, push notifications)
- Integration with emergency services
- Community safety mapping
- Real-time threat updates

## Disclaimer

This tool is for informational purposes. In genuine emergencies:
✓ Call local emergency services (911 in US, 112 in EU)
✓ Trust your instincts
✓ Do not rely solely on this analyzer

## License

Open source - Use freely for safety and educational purposes.
