"""
Personal Safety Risk Analyzer
Evaluates safety level based on environmental and situational inputs
"""

from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Optional
import math


class CrowdDensity(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass
class SafetyAssessment:
    risk_score: int
    risk_level: str
    threat_reason: str
    recommended_action: str
    emergency_actions: list = None

    def __str__(self):
        result = f"""Risk Score: {self.risk_score}
Risk Level: {self.risk_level}
Threat Reason: {self.threat_reason}
Recommended Action: {self.recommended_action}"""
        if self.emergency_actions:
            result += f"\nEmergency Actions:\n"
            for action in self.emergency_actions:
                result += f"  - {action}\n"
        return result


class SafetyAnalyzer:
    """Analyzes personal safety based on multiple environmental factors"""
    
    # Risk score thresholds
    LOW_RISK_MAX = 30
    MEDIUM_RISK_MAX = 60
    HIGH_RISK_MIN = 61
    
    # Risk contribution weights
    WEIGHTS = {
        "night_time": 15,
        "crowd_density": 15,
        "crime_history": 25,
        "network_availability": 10,
        "movement_speed": 20,
        "gps_validity": 15
    }
    
    def __init__(self):
        pass
    
    def is_valid_coordinates(self, latitude: float, longitude: float) -> bool:
        """Validate GPS coordinates"""
        try:
            lat_valid = -90 <= latitude <= 90
            lon_valid = -180 <= longitude <= 180
            return lat_valid and lon_valid
        except (TypeError, ValueError):
            return False
    
    def calculate_night_time_risk(self, hour: int) -> float:
        """Calculate risk factor for time of day (21-6 is night)"""
        if not 0 <= hour < 24:
            return 0.5  # Invalid time increases risk
        
        if 21 <= hour or hour < 6:
            return 1.0  # Night time: high risk
        return 0.0  # Daytime: low risk
    
    def calculate_crowd_density_risk(self, crowd_density: CrowdDensity) -> float:
        """Calculate risk factor for crowd density (low density = higher risk)"""
        density_map = {
            CrowdDensity.LOW: 1.0,     # Isolated areas increase risk
            CrowdDensity.MEDIUM: 0.5,  # Medium density reduces risk
            CrowdDensity.HIGH: 0.2     # Crowded areas are safer
        }
        return density_map.get(crowd_density, 0.5)
    
    def calculate_crime_history_risk(self, crime_score: int) -> float:
        """Calculate risk factor based on area crime history (0-100)"""
        if not 0 <= crime_score <= 100:
            return 0.5  # Invalid score increases risk
        return crime_score / 100.0
    
    def calculate_network_risk(self, network_available: bool) -> float:
        """Calculate risk factor for network availability"""
        return 0.0 if network_available else 1.0
    
    def calculate_movement_speed_risk(self, speed: float, crime_score: int) -> float:
        """
        Calculate risk factor for movement speed
        Sudden stop or zero speed in risky areas increases risk
        """
        if speed < 0:
            return 0.5  # Invalid speed
        
        # If stationary (speed = 0) and in high-crime area, high risk
        if speed == 0 and crime_score > 60:
            return 1.0
        
        # Moving provides some safety
        if speed > 0:
            return 0.3
        
        return 0.5
    
    def calculate_gps_validity_risk(self, latitude: float, longitude: float) -> float:
        """Calculate risk factor for GPS validity"""
        return 0.0 if self.is_valid_coordinates(latitude, longitude) else 1.0
    
    def assess_safety(self,
                     hour: int,
                     latitude: float,
                     longitude: float,
                     crowd_density: CrowdDensity,
                     crime_score: int,
                     movement_speed: float,
                     network_available: bool) -> SafetyAssessment:
        """
        Comprehensive safety assessment combining all factors
        
        Args:
            hour: Time of day (0-23)
            latitude: GPS latitude (-90 to 90)
            longitude: GPS longitude (-180 to 180)
            crowd_density: CrowdDensity enum
            crime_score: Crime history score (0-100)
            movement_speed: Current movement speed (>= 0)
            network_available: Boolean for network availability
            
        Returns:
            SafetyAssessment object with score, level, reasons, and actions
        """
        
        # Calculate individual risk factors
        night_risk = self.calculate_night_time_risk(hour)
        crowd_risk = self.calculate_crowd_density_risk(crowd_density)
        crime_risk = self.calculate_crime_history_risk(crime_score)
        network_risk = self.calculate_network_risk(network_available)
        movement_risk = self.calculate_movement_speed_risk(movement_speed, crime_score)
        gps_risk = self.calculate_gps_validity_risk(latitude, longitude)
        
        # Calculate weighted risk score
        total_score = (
            night_risk * self.WEIGHTS["night_time"] +
            crowd_risk * self.WEIGHTS["crowd_density"] +
            crime_risk * self.WEIGHTS["crime_history"] +
            network_risk * self.WEIGHTS["network_availability"] +
            movement_risk * self.WEIGHTS["movement_speed"] +
            gps_risk * self.WEIGHTS["gps_validity"]
        ) / sum(self.WEIGHTS.values()) * 100
        
        risk_score = int(round(total_score))
        
        # Determine risk level
        if risk_score <= self.LOW_RISK_MAX:
            risk_level = "Low"
        elif risk_score <= self.MEDIUM_RISK_MAX:
            risk_level = "Medium"
        else:
            risk_level = "High"
        
        # Generate threat reason
        threat_reasons = []
        if night_risk > 0.5:
            threat_reasons.append("night hours")
        if crowd_risk > 0.5:
            threat_reasons.append("low crowd density")
        if crime_risk > 0.5:
            threat_reasons.append("high crime area")
        if network_risk > 0.5:
            threat_reasons.append("no network connectivity")
        if movement_risk > 0.5:
            threat_reasons.append("stationary or slow movement")
        if gps_risk > 0.5:
            threat_reasons.append("invalid GPS coordinates")
        
        if threat_reasons:
            threat_reason = "Multiple risk factors: " + ", ".join(threat_reasons)
        else:
            threat_reason = "Safe conditions detected"
        
        # Generate recommended action
        if risk_level == "Low":
            recommended_action = "Continue normal activities. Stay aware of surroundings."
        elif risk_level == "Medium":
            recommended_action = "Increase vigilance. Consider moving to a safer area or increasing visibility. Contact trusted contacts about your location."
        else:  # High
            recommended_action = "Prioritize immediate safety. Move to a well-lit, populated area immediately."
        
        # Emergency actions for high risk
        emergency_actions = None
        if risk_level == "High":
            emergency_actions = [
                "Trigger Alarm",
                "Send SOS to emergency contacts",
                "Flashlight Activation",
                "Move to safer area immediately",
                "Contact local authorities if needed"
            ]
        
        return SafetyAssessment(
            risk_score=risk_score,
            risk_level=risk_level,
            threat_reason=threat_reason,
            recommended_action=recommended_action,
            emergency_actions=emergency_actions
        )


def main():
    """Example usage of the SafetyAnalyzer"""
    analyzer = SafetyAnalyzer()
    
    # Example 1: Safe daytime scenario
    print("=" * 60)
    print("SCENARIO 1: Safe Daytime in Populated Area")
    print("=" * 60)
    assessment1 = analyzer.assess_safety(
        hour=14,
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.HIGH,
        crime_score=25,
        movement_speed=1.5,
        network_available=True
    )
    print(assessment1)
    
    # Example 2: Medium risk scenario
    print("\n" + "=" * 60)
    print("SCENARIO 2: Medium Risk - Night Time, Low Crowd")
    print("=" * 60)
    assessment2 = analyzer.assess_safety(
        hour=23,
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.LOW,
        crime_score=45,
        movement_speed=0.8,
        network_available=True
    )
    print(assessment2)
    
    # Example 3: High risk scenario
    print("\n" + "=" * 60)
    print("SCENARIO 3: High Risk - Night, Isolated, No Network")
    print("=" * 60)
    assessment3 = analyzer.assess_safety(
        hour=2,
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.LOW,
        crime_score=80,
        movement_speed=0.0,
        network_available=False
    )
    print(assessment3)
    
    # Example 4: Invalid coordinates
    print("\n" + "=" * 60)
    print("SCENARIO 4: Invalid GPS - Coordinates Out of Range")
    print("=" * 60)
    assessment4 = analyzer.assess_safety(
        hour=15,
        latitude=150.0,  # Invalid latitude
        longitude=200.0,  # Invalid longitude
        crowd_density=CrowdDensity.MEDIUM,
        crime_score=30,
        movement_speed=2.0,
        network_available=True
    )
    print(assessment4)


if __name__ == "__main__":
    main()
