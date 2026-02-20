"""
Web Application Startup Script
Checks dependencies and starts the web server
"""

import os
import sys
import subprocess
import platform


def check_python_version():
    """Check if Python 3.8+ is installed"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor} detected")
    return True


def check_flask_installed():
    """Check if Flask is installed"""
    try:
        import flask
        print(f"✓ Flask {flask.__version__} installed")
        return True
    except ImportError:
        print("❌ Flask is not installed")
        return False


def check_required_files():
    """Check if required files exist"""
    required_files = [
        'safety_analyzer.py',
        'app.py',
        'templates/index.html'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} found")
        else:
            print(f"❌ {file} not found")
            all_exist = False
    
    return all_exist


def install_flask():
    """Install Flask if not present"""
    print("\n📦 Installing Flask...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask', '--quiet'])
        print("✓ Flask installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Flask")
        return False


def start_web_app():
    """Start the Flask web application"""
    print("\n" + "="*70)
    print("Starting Web Application...".center(70))
    print("="*70)
    print()
    print("🌐 Web Server Starting...")
    print("📍 Open your browser and navigate to: http://localhost:5000")
    print()
    print("🔗 Default Location: NYC (40.7128, -74.0060)")
    print("💡 Tip: Adjust parameters and click 'Assess Safety' to get started")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    print("="*70 + "\n")
    
    try:
        import app
        app.app.run(debug=True, host='localhost', port=5000)
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("Server stopped. Stay safe! 🛡️".center(70))
        print("="*70)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)


def main():
    """Main startup sequence"""
    print("\n" + "="*70)
    print("Personal Safety Risk Analyzer - Web Application".center(70))
    print("="*70 + "\n")
    
    print("📋 Checking System Requirements...\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check Flask
    flask_installed = check_flask_installed()
    
    if not flask_installed:
        response = input("\n❓ Flask not found. Install now? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            if not install_flask():
                sys.exit(1)
        else:
            print("❌ Flask is required to run the web application")
            print("   Install it with: pip install flask")
            sys.exit(1)
    
    # Check required files
    print("\n📁 Checking Required Files...\n")
    if not check_required_files():
        print("\n❌ Some required files are missing")
        print("   Please ensure you're in the correct directory")
        sys.exit(1)
    
    # All checks passed
    print("\n✅ All requirements met!\n")
    
    # Start the application
    start_web_app()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nShutdown requested.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
