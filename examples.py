"""
Quick Start Guide - Personal Safety Risk Analyzer
Examples and common use cases
"""

from safety_analyzer import SafetyAnalyzer, CrowdDensity


def example_1_safe_commute():
    """Example 1: Safe daytime commute"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Daytime Commute - Should be LOW RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Monday morning, heading to work
    assessment = analyzer.assess_safety(
        hour=8,                           # Morning
        latitude=40.7128,                 # NYC
        longitude=-74.0060,
        crowd_density=CrowdDensity.HIGH,  # Rush hour - many people
        crime_score=25,                   # Generally safe area
        movement_speed=2.5,               # Walking/moving
        network_available=True            # Connected
    )
    
    print(assessment)


def example_2_night_alone():
    """Example 2: Risky solo travel at night"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Night Travel Alone - MEDIUM RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Late night return home
    assessment = analyzer.assess_safety(
        hour=23,                          # Night time
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.LOW,   # Fewer people at night
        crime_score=50,                   # Moderate crime area
        movement_speed=1.2,               # Moderate pace
        network_available=True            # Connected
    )
    
    print(assessment)
    print("\n💡 TIP: Try to travel with others or in well-lit areas")


def example_3_emergency_situation():
    """Example 3: Dangerous situation requiring immediate action"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Dangerous Situation - HIGH RISK (Emergency)")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Alone at night, isolated, in gang territory, no network
    assessment = analyzer.assess_safety(
        hour=2,                           # 2 AM
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.LOW,   # Isolated area
        crime_score=85,                   # High crime zone
        movement_speed=0.0,               # Stranded/stopped
        network_available=False           # No signal
    )
    
    print(assessment)
    print("\n🆘 URGENT: Follow emergency actions immediately!")


def example_4_invalid_location():
    """Example 4: Unknown/Invalid location"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Unknown Location - INCREASED RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: GPS not working, unknown area
    assessment = analyzer.assess_safety(
        hour=15,                          # Afternoon
        latitude=200.0,                   # INVALID GPS
        longitude=300.0,                  # INVALID GPS
        crowd_density=CrowdDensity.MEDIUM,
        crime_score=40,
        movement_speed=1.5,
        network_available=False           # Can't get help
    )
    
    print(assessment)
    print("\n📍 TIP: Use offline maps or landmarks to determine location")


def example_5_bustling_area():
    """Example 5: Safe in numbers (crowded area)"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Crowded Event/Festival - LOW RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Concert or festival
    assessment = analyzer.assess_safety(
        hour=20,                          # Evening
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.HIGH,  # Very crowded
        crime_score=35,                   # Moderate crime area
        movement_speed=0.5,               # Moving slowly through crowd
        network_available=True            # Secure connection
    )
    
    print(assessment)
    print("\n👥 NOTE: Large crowds provide security through numbers")


def example_6_business_travel():
    """Example 6: Business travel in unfamiliar city"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Business Travel - MEDIUM RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Late evening, hotel to restaurant, downtown area
    assessment = analyzer.assess_safety(
        hour=19,                          # Early evening
        latitude=37.7749,                 # San Francisco
        longitude=-122.4194,
        crowd_density=CrowdDensity.MEDIUM,  # City streets
        crime_score=55,                   # Moderate area
        movement_speed=1.5,               # Walking pace
        network_available=True            # Hotel WiFi + Mobile
    )
    
    print(assessment)
    print("\n✓ RECOMMEND: Tell someone your route and ETA")


def example_7_isolated_hiking():
    """Example 7: Remote location (hiking)"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Remote Hiking Trail - MEDIUM TO HIGH RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Hiking in remote area
    assessment = analyzer.assess_safety(
        hour=14,                          # Afternoon hike
        latitude=40.2732,                 # Mountain area
        longitude=-74.5243,
        crowd_density=CrowdDensity.LOW,   # Remote
        crime_score=20,                   # Nature area (low crime)
        movement_speed=0.8,               # Hiking pace
        network_available=False           # No cell coverage
    )
    
    print(assessment)
    print("\n🥾 SAFETY TIPS:")
    print("  - Tell someone where you're going and when you'll return")
    print("  - Carry a physical map and compass")
    print("  - Bring first aid kit and whistle")
    print("  - Start early to avoid traveling in dark")


def example_8_late_night_delivery():
    """Example 8: Delivery driver late night"""
    print("\n" + "="*70)
    print("EXAMPLE 8: Late Night Delivery - MEDIUM TO HIGH RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Delivery at 1 AM
    assessment = analyzer.assess_safety(
        hour=1,                           # 1 AM
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.LOW,   # Few people at night
        crime_score=65,                   # Mixed neighborhood
        movement_speed=2.0,               # Driving/moving
        network_available=True            # Connected to dispatch
    )
    
    print(assessment)
    print("\n🚗 SAFETY TIPS:")
    print("  - Keep vehicle running and doors locked")
    print("  - Stay in contact with dispatch")
    print("  - Take well-lit routes")
    print("  - Trust your instincts")


def example_9_group_travel():
    """Example 9: Group travel (safer)"""
    print("\n" + "="*70)
    print("EXAMPLE 9: Group Travel - REDUCED RISK")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    
    # Scenario: Late night group returning from event
    assessment = analyzer.assess_safety(
        hour=22,                          # Night
        latitude=40.7128,
        longitude=-74.0060,
        crowd_density=CrowdDensity.MEDIUM,  # Group of people
        crime_score=55,                   # Moderate area
        movement_speed=1.5,               # Walking as group
        network_available=True            # Multiple phones
    )
    
    print(assessment)
    print("\n👫 SAFETY FACT: 'Safety in numbers' - Groups deter threats")


def example_10_parametric_test():
    """Example 10: Testing different parameters"""
    print("\n" + "="*70)
    print("EXAMPLE 10: How Different Factors Affect Risk")
    print("="*70)
    
    analyzer = SafetyAnalyzer()
    base_params = {
        'latitude': 40.7128,
        'longitude': -74.0060,
        'crowd_density': CrowdDensity.MEDIUM,
        'crime_score': 50,
        'movement_speed': 1.0,
        'network_available': True
    }
    
    print("\n📊 Effect of Time of Day:")
    for hour in [8, 14, 20, 2]:
        params = {**base_params, 'hour': hour}
        assessment = analyzer.assess_safety(**params)
        time_label = "🌅 Morning" if hour == 8 else "☀️ Afternoon" if hour == 14 else "🌙 Evening" if hour == 20 else "🌑 Night"
        print(f"  {time_label} (Hour {hour:02d}:00): Risk = {assessment.risk_score} ({assessment.risk_level})")
    
    print("\n📊 Effect of Crowd Density:")
    for density in [CrowdDensity.LOW, CrowdDensity.MEDIUM, CrowdDensity.HIGH]:
        params = {**base_params, 'hour': 20, 'crowd_density': density}
        assessment = analyzer.assess_safety(**params)
        print(f"  {density.value:8} Crowd: Risk = {assessment.risk_score} ({assessment.risk_level})")
    
    print("\n📊 Effect of Crime History:")
    for crime in [10, 30, 50, 70, 90]:
        params = {**base_params, 'hour': 20, 'crime_score': crime}
        assessment = analyzer.assess_safety(**params)
        print(f"  Crime Score {crime:2d}/100: Risk = {assessment.risk_score} ({assessment.risk_level})")


def run_all_examples():
    """Run all examples"""
    examples = [
        ("Safe Commute", example_1_safe_commute),
        ("Night Alone", example_2_night_alone),
        ("Emergency", example_3_emergency_situation),
        ("Invalid Location", example_4_invalid_location),
        ("Crowded Area", example_5_bustling_area),
        ("Business Travel", example_6_business_travel),
        ("Hiking", example_7_isolated_hiking),
        ("Late Delivery", example_8_late_night_delivery),
        ("Group Travel", example_9_group_travel),
        ("Parametric Test", example_10_parametric_test),
    ]
    
    print("\n" + "🛡️  PERSONAL SAFETY RISK ANALYZER - EXAMPLES ".center(70, "="))
    print(f"\nAvailable Examples ({len(examples)} total):\n")
    
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    
    print("\n" + "="*70)
    
    while True:
        try:
            choice = input("\nSelect example (1-{}, or 'all', or 'q' to quit): ".format(len(examples))).strip().lower()
            
            if choice == 'q':
                print("\nStay safe! 🛡️\n")
                break
            elif choice == 'all':
                for _, func in examples:
                    func()
                print("\n" + "="*70)
                print("All examples completed!")
                break
            else:
                idx = int(choice) - 1
                if 0 <= idx < len(examples):
                    examples[idx][1]()
                else:
                    print("Invalid selection")
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")
            break


if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║             🛡️  PERSONAL SAFETY RISK ANALYZER - QUICK START  🛡️           ║
║                                                                            ║
║  This tool demonstrates practical safety scenarios and how the analyzer   ║
║  evaluates risk in real-world situations.                                  ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    run_all_examples()
