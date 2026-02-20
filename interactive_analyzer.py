"""
Interactive Safety Risk Analyzer CLI
Allows users to input parameters and get real-time safety assessment
"""

from safety_analyzer import SafetyAnalyzer, CrowdDensity


def get_time_input() -> int:
    """Get hour input from user (0-23)"""
    while True:
        try:
            hour = int(input("Enter time of day (0-23): "))
            if 0 <= hour < 24:
                return hour
            print("❌ Hour must be between 0 and 23")
        except ValueError:
            print("❌ Please enter a valid number")


def get_coordinates_input() -> tuple:
    """Get latitude and longitude from user"""
    while True:
        try:
            lat = float(input("Enter latitude (-90 to 90): "))
            lon = float(input("Enter longitude (-180 to 180): "))
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return lat, lon
            print("❌ Invalid coordinate range. Latitude: -90 to 90, Longitude: -180 to 180")
        except ValueError:
            print("❌ Please enter valid numbers")


def get_crowd_density_input() -> CrowdDensity:
    """Get crowd density from user"""
    print("\nCrowd Density options:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    
    while True:
        choice = input("Select crowd density (1-3): ").strip()
        density_map = {
            "1": CrowdDensity.LOW,
            "2": CrowdDensity.MEDIUM,
            "3": CrowdDensity.HIGH
        }
        if choice in density_map:
            return density_map[choice]
        print("❌ Please select 1, 2, or 3")


def get_crime_score_input() -> int:
    """Get area crime history score from user (0-100)"""
    while True:
        try:
            score = int(input("Enter area crime history score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("❌ Crime score must be between 0 and 100")
        except ValueError:
            print("❌ Please enter a valid number")


def get_movement_speed_input() -> float:
    """Get user movement speed from user (>= 0)"""
    while True:
        try:
            speed = float(input("Enter movement speed (0+, in m/s or km/h): "))
            if speed >= 0:
                return speed
            print("❌ Speed must be 0 or greater")
        except ValueError:
            print("❌ Please enter a valid number")


def get_network_input() -> bool:
    """Get network availability from user"""
    print("\nNetwork Availability options:")
    print("1. Yes (Connected)")
    print("2. No (Not Connected)")
    
    while True:
        choice = input("Select network status (1-2): ").strip()
        if choice == "1":
            return True
        elif choice == "2":
            return False
        print("❌ Please select 1 or 2")


def run_interactive_analyzer():
    """Run the interactive safety analyzer"""
    print("\n" + "=" * 70)
    print(" " * 15 + "PERSONAL SAFETY RISK ANALYZER")
    print("=" * 70)
    print("\nThis tool evaluates your safety based on environmental factors.")
    print("Please provide the following information:\n")
    
    analyzer = SafetyAnalyzer()
    
    # Collect inputs
    hour = get_time_input()
    latitude, longitude = get_coordinates_input()
    crowd_density = get_crowd_density_input()
    crime_score = get_crime_score_input()
    movement_speed = get_movement_speed_input()
    network_available = get_network_input()
    
    print("\n" + "=" * 70)
    print("ANALYZING...")
    print("=" * 70 + "\n")
    
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
    
    # Display results with visual indicators
    print(f"Risk Score: {assessment.risk_score}/100")
    
    # Visual risk level indicator
    if assessment.risk_level == "Low":
        print(f"Risk Level: 🟢 {assessment.risk_level}")
    elif assessment.risk_level == "Medium":
        print(f"Risk Level: 🟡 {assessment.risk_level}")
    else:
        print(f"Risk Level: 🔴 {assessment.risk_level}")
    
    print(f"Threat Reason: {assessment.threat_reason}")
    print(f"Recommended Action: {assessment.recommended_action}")
    
    # Show emergency actions if high risk
    if assessment.emergency_actions:
        print("\n⚠️  EMERGENCY ACTIONS RECOMMENDED:")
        for action in assessment.emergency_actions:
            print(f"  ▸ {action}")
    
    print("\n" + "=" * 70)


def main():
    """Main entry point"""
    while True:
        try:
            run_interactive_analyzer()
            
            # Ask if user wants to run again
            again = input("\nDo you want to run another assessment? (yes/no): ").strip().lower()
            if again not in ["yes", "y"]:
                print("\nStay safe! 🛡️\n")
                break
        except KeyboardInterrupt:
            print("\n\nAnalyzer interrupted. Stay safe! 🛡️\n")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
