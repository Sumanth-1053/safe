# Getting Started - Personal Safety Risk Analyzer

## 📁 Project Files

```
safe/
├── safety_analyzer.py          # Core analyzer engine
├── interactive_analyzer.py     # Interactive CLI tool
├── test_analyzer.py            # Comprehensive test suite (30 tests)
├── examples.py                 # 10 real-world examples
├── README.md                   # Full documentation
└── QUICKSTART.md              # This file
```

## 🚀 Quick Start - 3 Ways to Use

### Option 1: Interactive Mode (Recommended for beginners)
```bash
python interactive_analyzer.py
```
**Best for:** Real-time personal safety assessments
- Answer guided prompts
- Get instant safety assessment
- Visual risk indicators
- Emergency recommendations if needed

### Option 2: View Examples (Learn by example)
```bash
python examples.py
```
**Best for:** Understanding how the system works
- 10 real-world scenarios
- Parametric testing
- Interactive selection menu

### Option 3: Run Tests (Verify functionality)
```bash
python test_analyzer.py
```
**Best for:** Technical verification
- 30 comprehensive unit tests
- All tests PASS ✓
- Validates all components

## 📊 Basic Usage Pattern

```python
from safety_analyzer import SafetyAnalyzer, CrowdDensity

# Initialize
analyzer = SafetyAnalyzer()

# Assess safety
assessment = analyzer.assess_safety(
    hour=23,                        # 11 PM
    latitude=40.7128,              # NYC
    longitude=-74.0060,
    crowd_density=CrowdDensity.LOW, # Few people
    crime_score=60,                # Moderate-high
    movement_speed=0.5,            # Slow/stopped
    network_available=False        # No signal
)

# Get results
print(assessment.risk_score)        # 0-100
print(assessment.risk_level)        # "Low"/"Medium"/"High"
print(assessment.threat_reason)     # Explanation
print(assessment.recommended_action) # Guidance
```

## 📋 Input Parameters Reference

| Parameter | Range | Example | Notes |
|-----------|-------|---------|-------|
| `hour` | 0-23 | 14 | 0=Midnight, 12=Noon, 23=11PM |
| `latitude` | -90 to 90 | 40.7128 | NYC: 40.7128, SF: 37.7749 |
| `longitude` | -180 to 180 | -74.0060 | NYC: -74.0060, SF: -122.4194 |
| `crowd_density` | LOW/MEDIUM/HIGH | HIGH | Affects risk calculation |
| `crime_score` | 0-100 | 50 | 0=Safe, 50=Moderate, 100=Dangerous |
| `movement_speed` | ≥ 0 | 1.5 | m/s or km/h, 0=Stationary |
| `network_available` | True/False | True | Mobile/WiFi connectivity |

## 🎯 Example Scenarios

### Safe Travel ✓
```python
assessment = analyzer.assess_safety(
    hour=10,                          # Morning
    latitude=40.7128,
    longitude=-74.0060,
    crowd_density=CrowdDensity.HIGH,  # Crowded
    crime_score=20,                   # Low crime
    movement_speed=2.0,               # Moving
    network_available=True            # Connected
)
# Expected: Risk Score ~15, Status: LOW ✓
```

### Risky Situation ⚠️
```python
assessment = analyzer.assess_safety(
    hour=2,                           # 2 AM
    latitude=40.7128,
    longitude=-74.0060,
    crowd_density=CrowdDensity.LOW,   # Isolated
    crime_score=80,                   # High crime
    movement_speed=0.0,               # Stopped
    network_available=False           # No signal
)
# Expected: Risk Score ~80, Status: HIGH, Emergency Actions Recommended
```

## 🔴 Risk Level Guide

- **🟢 LOW (0-30)**: Safe environment
  - Continue normal activities
  - Stay normally aware
  - Example: Busy mall at noon

- **🟡 MEDIUM (31-60)**: Increased caution
  - Increase vigilance
  - Avoid isolated areas
  - Share location with contacts
  - Example: Downtown at 11 PM

- **🔴 HIGH (61-100)**: Serious risk
  - Immediate safety priority
  - Move to safe area
  - Contact authorities if needed
  - Emergency actions recommended
  - Example: Alone at 2 AM in crime zone

## 📱 Safety Features

### Emergency Actions (High Risk Only)
- 🚨 Trigger Alarm
- 📱 Send SOS to emergency contacts
- 🔦 Activate Flashlight
- 🏃 Move to safer area
- 📞 Contact authorities

### Risk Factors Analyzed
1. **Night Time (21:00-06:00)** → Increased risk
2. **Isolated Location** → Increased risk
3. **High Crime Area** → Increased risk
4. **No Network** → Increased risk
5. **Stationary/Slow Movement** → Increased risk
6. **Invalid GPS** → Increased risk

## 🧪 Testing

All functionality thoroughly tested:
```bash
python test_analyzer.py
```

**Test Coverage:**
- ✓ 30 unit tests
- ✓ Coordinate validation
- ✓ Risk factor calculations
- ✓ Edge case handling
- ✓ Assessment consistency
- ✓ Emergency actions
- ✓ All tests PASS

## 💡 Tips & Best Practices

### Personal Safety
✓ Check assessments regularly in new areas
✓ Share your location with trusted contacts
✓ Trust high-risk warnings
✓ Move to well-lit, populated areas when alerted
✓ Keep network enabled for emergencies

### Using the Tool
✓ Update parameters as you move
✓ React quickly to HIGH risk alerts
✓ Use in combination with your instincts
✓ Review threat reasons for context
✓ Follow recommended actions

### Emergency Situations
If HIGH risk is detected:
1. Move to a safe location immediately
2. Activate alarms/signal for help
3. Contact emergency services (911, 112, etc.)
4. Inform trusted contacts of situation
5. Do not confront threats

## 🏥 Emergency Services

**International Emergency Numbers:**
- 🇺🇸 USA: 911
- 🇬🇧 UK/EU: 112
- 🇦🇺 Australia: 000
- 🇮🇳 India: 100/112
- 🇨🇦 Canada: 911

## ⚠️ Disclaimer

This tool is for informational purposes to support personal safety awareness. It should NOT be your only safety measure.

**Always:**
- Trust your instincts first
- In emergencies, call local authorities immediately  
- Use common sense and awareness
- Combine with real-world safety practices

## 📚 Full Documentation

For complete documentation, see [README.md](README.md)

## 🤝 Support

**Issues or Questions?**
1. Check examples.py for usage patterns
2. Review test_analyzer.py for expected behavior
3. See README.md for comprehensive documentation

## 📝 File Descriptions

### safety_analyzer.py
- Core SafetyAnalyzer class
- Risk calculation engine
- Input validation
- Assessment data structures

### interactive_analyzer.py
- User-friendly CLI
- Input prompts
- Visual indicators
- Multi-assessment loop

### test_analyzer.py
- 30 unit tests
- All validation tests
- Edge case coverage
- Runs with: `python test_analyzer.py`

### examples.py
- 10 real-world scenarios
- Parametric testing
- Interactive menu
- Educational purposes

---

**Stay Safe! 🛡️**

*Personal Safety Risk Analyzer - Powered by intelligent risk assessment*
