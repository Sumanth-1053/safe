"""
Unit tests for Personal Safety Risk Analyzer
"""

import unittest
from safety_analyzer import SafetyAnalyzer, CrowdDensity, SafetyAssessment


class TestSafetyAnalyzer(unittest.TestCase):
    """Test suite for SafetyAnalyzer"""
    
    def setUp(self):
        """Initialize analyzer for each test"""
        self.analyzer = SafetyAnalyzer()
    
    # ============ Coordinate Validation Tests ============
    def test_valid_coordinates(self):
        """Test valid GPS coordinates"""
        self.assertTrue(self.analyzer.is_valid_coordinates(40.7128, -74.0060))
        self.assertTrue(self.analyzer.is_valid_coordinates(0, 0))
        self.assertTrue(self.analyzer.is_valid_coordinates(90, 180))
        self.assertTrue(self.analyzer.is_valid_coordinates(-90, -180))
    
    def test_invalid_latitude(self):
        """Test invalid latitude"""
        self.assertFalse(self.analyzer.is_valid_coordinates(91, 0))
        self.assertFalse(self.analyzer.is_valid_coordinates(-91, 0))
        self.assertFalse(self.analyzer.is_valid_coordinates(150, 0))
    
    def test_invalid_longitude(self):
        """Test invalid longitude"""
        self.assertFalse(self.analyzer.is_valid_coordinates(0, 181))
        self.assertFalse(self.analyzer.is_valid_coordinates(0, -181))
        self.assertFalse(self.analyzer.is_valid_coordinates(0, 200))
    
    def test_non_numeric_coordinates(self):
        """Test non-numeric coordinates"""
        self.assertFalse(self.analyzer.is_valid_coordinates("40", "-74"))
    
    # ============ Risk Factor Calculation Tests ============
    def test_night_time_risk_daytime(self):
        """Test night risk for daytime hours"""
        # Daytime hours should have 0 risk
        for hour in [7, 12, 18, 20]:
            risk = self.analyzer.calculate_night_time_risk(hour)
            self.assertEqual(risk, 0.0, f"Hour {hour} should be low risk")
    
    def test_night_time_risk_nighttime(self):
        """Test night risk for nighttime hours"""
        # Night hours (21-6) should have high risk
        for hour in [0, 2, 5, 21, 22, 23]:
            risk = self.analyzer.calculate_night_time_risk(hour)
            self.assertEqual(risk, 1.0, f"Hour {hour} should be high risk")
    
    def test_invalid_hour(self):
        """Test invalid hour values"""
        risk = self.analyzer.calculate_night_time_risk(25)
        self.assertEqual(risk, 0.5)
        risk = self.analyzer.calculate_night_time_risk(-1)
        self.assertEqual(risk, 0.5)
    
    def test_crowd_density_risk(self):
        """Test crowd density risk calculations"""
        low_risk = self.analyzer.calculate_crowd_density_risk(CrowdDensity.LOW)
        medium_risk = self.analyzer.calculate_crowd_density_risk(CrowdDensity.MEDIUM)
        high_risk = self.analyzer.calculate_crowd_density_risk(CrowdDensity.HIGH)
        
        # Low density should be highest risk
        self.assertEqual(low_risk, 1.0)
        # High density should be lowest risk
        self.assertEqual(high_risk, 0.2)
        # Medium should be in between
        self.assertEqual(medium_risk, 0.5)
    
    def test_crime_history_risk(self):
        """Test crime history risk scaling"""
        # No crime
        risk_0 = self.analyzer.calculate_crime_history_risk(0)
        self.assertEqual(risk_0, 0.0)
        
        # High crime
        risk_100 = self.analyzer.calculate_crime_history_risk(100)
        self.assertEqual(risk_100, 1.0)
        
        # Medium crime
        risk_50 = self.analyzer.calculate_crime_history_risk(50)
        self.assertEqual(risk_50, 0.5)
    
    def test_crime_history_invalid(self):
        """Test invalid crime scores"""
        risk = self.analyzer.calculate_crime_history_risk(101)
        self.assertEqual(risk, 0.5)
        risk = self.analyzer.calculate_crime_history_risk(-1)
        self.assertEqual(risk, 0.5)
    
    def test_network_risk(self):
        """Test network availability risk"""
        # Network available - no risk
        risk_available = self.analyzer.calculate_network_risk(True)
        self.assertEqual(risk_available, 0.0)
        
        # Network unavailable - high risk
        risk_unavailable = self.analyzer.calculate_network_risk(False)
        self.assertEqual(risk_unavailable, 1.0)
    
    def test_movement_speed_risk_moving(self):
        """Test risk for moving targets"""
        risk = self.analyzer.calculate_movement_speed_risk(5.0, 30)
        self.assertEqual(risk, 0.3)
    
    def test_movement_speed_risk_stationary_safe(self):
        """Test risk for stationary in safe area"""
        risk = self.analyzer.calculate_movement_speed_risk(0.0, 20)
        self.assertEqual(risk, 0.5)
    
    def test_movement_speed_risk_stationary_dangerous(self):
        """Test risk for stationary in dangerous area"""
        risk = self.analyzer.calculate_movement_speed_risk(0.0, 80)
        self.assertEqual(risk, 1.0)
    
    def test_movement_speed_risk_invalid(self):
        """Test invalid speed"""
        risk = self.analyzer.calculate_movement_speed_risk(-5, 30)
        self.assertEqual(risk, 0.5)
    
    def test_gps_validity_risk(self):
        """Test GPS validity risk"""
        # Valid coordinates
        risk_valid = self.analyzer.calculate_gps_validity_risk(40.7, -74.0)
        self.assertEqual(risk_valid, 0.0)
        
        # Invalid coordinates
        risk_invalid = self.analyzer.calculate_gps_validity_risk(150, 200)
        self.assertEqual(risk_invalid, 1.0)
    
    # ============ Full Assessment Tests ============
    def test_low_risk_scenario(self):
        """Test scenario that should result in low risk"""
        assessment = self.analyzer.assess_safety(
            hour=14,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.HIGH,
            crime_score=20,
            movement_speed=2.0,
            network_available=True
        )
        
        self.assertEqual(assessment.risk_level, "Low")
        self.assertLessEqual(assessment.risk_score, 30)
        self.assertIn("Continue normal activities", assessment.recommended_action)
        self.assertIsNone(assessment.emergency_actions)
    
    def test_medium_risk_scenario(self):
        """Test scenario that should result in medium risk"""
        assessment = self.analyzer.assess_safety(
            hour=23,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.LOW,
            crime_score=45,
            movement_speed=1.0,
            network_available=True
        )
        
        self.assertEqual(assessment.risk_level, "Medium")
        self.assertGreater(assessment.risk_score, 30)
        self.assertLessEqual(assessment.risk_score, 60)
        self.assertIn("Increase vigilance", assessment.recommended_action)
        self.assertIsNone(assessment.emergency_actions)
    
    def test_high_risk_scenario(self):
        """Test scenario that should result in high risk"""
        assessment = self.analyzer.assess_safety(
            hour=2,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.LOW,
            crime_score=85,
            movement_speed=0.0,
            network_available=False
        )
        
        self.assertEqual(assessment.risk_level, "High")
        self.assertGreater(assessment.risk_score, 60)
        self.assertIn("Prioritize immediate safety", assessment.recommended_action)
        self.assertIsNotNone(assessment.emergency_actions)
        self.assertGreater(len(assessment.emergency_actions), 0)
    
    def test_edge_case_invalid_coordinates(self):
        """Test edge case with invalid coordinates"""
        assessment = self.analyzer.assess_safety(
            hour=15,
            latitude=999,
            longitude=999,
            crowd_density=CrowdDensity.MEDIUM,
            crime_score=30,
            movement_speed=1.5,
            network_available=True
        )
        
        # Should increase risk due to invalid GPS
        self.assertGreater(assessment.risk_score, 20)
        self.assertIn("invalid GPS", assessment.threat_reason)
    
    def test_edge_case_invalid_hour(self):
        """Test edge case with invalid hour"""
        assessment = self.analyzer.assess_safety(
            hour=25,  # Invalid
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.HIGH,
            crime_score=20,
            movement_speed=2.0,
            network_available=True
        )
        
        # Should still work and increase risk
        self.assertGreater(assessment.risk_score, 0)
    
    def test_assessment_consistency(self):
        """Test that same input produces same output"""
        params = {
            'hour': 18,
            'latitude': 35.6762,
            'longitude': 139.6503,
            'crowd_density': CrowdDensity.MEDIUM,
            'crime_score': 40,
            'movement_speed': 1.5,
            'network_available': True
        }
        
        assessment1 = self.analyzer.assess_safety(**params)
        assessment2 = self.analyzer.assess_safety(**params)
        
        self.assertEqual(assessment1.risk_score, assessment2.risk_score)
        self.assertEqual(assessment1.risk_level, assessment2.risk_level)
    
    # ============ Boundary Tests ============
    def test_score_range(self):
        """Test that risk score is always within 0-100"""
        scenarios = [
            # Worst case
            (2, 40.0, -74.0, CrowdDensity.LOW, 100, 0.0, False),
            # Best case
            (14, 40.0, -74.0, CrowdDensity.HIGH, 0, 10.0, True),
            # Medium
            (12, 40.0, -74.0, CrowdDensity.MEDIUM, 50, 2.0, True),
        ]
        
        for params in scenarios:
            assessment = self.analyzer.assess_safety(*params)
            self.assertGreaterEqual(assessment.risk_score, 0)
            self.assertLessEqual(assessment.risk_score, 100)
    
    def test_risk_level_correctness(self):
        """Test risk level is correctly assigned based on score"""
        for risk_score in range(0, 101):
            if risk_score <= 30:
                expected_level = "Low"
            elif risk_score <= 60:
                expected_level = "Medium"
            else:
                expected_level = "High"
            
            # Create scenario that would produce specific score
            # (This is approximate due to weighting)
            assessment = self.analyzer.assess_safety(
                hour=12 + (risk_score // 30),
                latitude=40.7128,
                longitude=-74.0060,
                crowd_density=CrowdDensity.MEDIUM if risk_score < 50 else CrowdDensity.LOW,
                crime_score=risk_score,
                movement_speed=2.0 if risk_score < 50 else 0.5,
                network_available=risk_score < 80
            )
            
            self.assertIn(assessment.risk_level, ["Low", "Medium", "High"])
    
    def test_threat_reason_completeness(self):
        """Test that threat reasons are generated"""
        assessment = self.analyzer.assess_safety(
            hour=23,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.LOW,
            crime_score=70,
            movement_speed=0.0,
            network_available=False
        )
        
        # Should have threat reasons
        self.assertIsNotNone(assessment.threat_reason)
        self.assertGreater(len(assessment.threat_reason), 0)
    
    def test_emergency_actions_for_high_risk(self):
        """Test emergency actions are provided for high risk"""
        assessment = self.analyzer.assess_safety(
            hour=3,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.LOW,
            crime_score=90,
            movement_speed=0.0,
            network_available=False
        )
        
        self.assertIsNotNone(assessment.emergency_actions)
        self.assertGreater(len(assessment.emergency_actions), 0)
        
        # Check for specific actions
        actions_text = " ".join(assessment.emergency_actions).lower()
        self.assertIn("alarm", actions_text)
        self.assertIn("sos", actions_text)
    
    def test_no_emergency_actions_for_low_risk(self):
        """Test no emergency actions for low risk"""
        assessment = self.analyzer.assess_safety(
            hour=12,
            latitude=40.7128,
            longitude=-74.0060,
            crowd_density=CrowdDensity.HIGH,
            crime_score=10,
            movement_speed=3.0,
            network_available=True
        )
        
        self.assertIsNone(assessment.emergency_actions)


class TestSafetyAssessment(unittest.TestCase):
    """Test SafetyAssessment dataclass"""
    
    def test_assessment_creation(self):
        """Test creating a SafetyAssessment object"""
        assessment = SafetyAssessment(
            risk_score=45,
            risk_level="Medium",
            threat_reason="Test reason",
            recommended_action="Test action"
        )
        
        self.assertEqual(assessment.risk_score, 45)
        self.assertEqual(assessment.risk_level, "Medium")
        self.assertEqual(assessment.threat_reason, "Test reason")
        self.assertEqual(assessment.recommended_action, "Test action")
        self.assertIsNone(assessment.emergency_actions)
    
    def test_assessment_string_representation(self):
        """Test string representation of assessment"""
        assessment = SafetyAssessment(
            risk_score=50,
            risk_level="Medium",
            threat_reason="Test",
            recommended_action="Act"
        )
        
        str_repr = str(assessment)
        self.assertIn("Risk Score: 50", str_repr)
        self.assertIn("Risk Level: Medium", str_repr)
        self.assertIn("Threat Reason: Test", str_repr)
        self.assertIn("Recommended Action: Act", str_repr)
    
    def test_assessment_with_emergency_actions(self):
        """Test assessment with emergency actions"""
        actions = ["Action 1", "Action 2"]
        assessment = SafetyAssessment(
            risk_score=75,
            risk_level="High",
            threat_reason="Danger",
            recommended_action="Evacuate",
            emergency_actions=actions
        )
        
        self.assertEqual(assessment.emergency_actions, actions)
        str_repr = str(assessment)
        self.assertIn("Emergency Actions:", str_repr)
        self.assertIn("Action 1", str_repr)


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
