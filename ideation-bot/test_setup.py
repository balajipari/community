#!/usr/bin/env python3
"""
Simple test script to verify the CLI setup
"""
import sys
import importlib

def test_imports():
    """Test if all required modules can be imported"""
    required_modules = [
        'click',
        'rich',
        'requests',
        'dotenv'
    ]
    
    print("Testing imports...")
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            return False
    
    return True

def test_local_modules():
    """Test if our local modules can be imported"""
    local_modules = [
        'config',
        'ai_client',
        'cli'
    ]
    
    print("\nTesting local modules...")
    for module in local_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            return False
    
    return True

def test_system_prompt():
    """Test if system prompt file can be read"""
    try:
        with open('system_prompt.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'STRUCTURED_SYSTEM_PROMPT' in content:
                print("✅ system_prompt.txt")
                return True
            else:
                print("❌ system_prompt.txt: Invalid content")
                return False
    except Exception as e:
        print(f"❌ system_prompt.txt: {e}")
        return False

def main():
    print("🚀 Testing Ideation Buddy CLI Setup\n")
    
    all_tests_passed = True
    
    # Test imports
    if not test_imports():
        all_tests_passed = False
    
    # Test local modules
    if not test_local_modules():
        all_tests_passed = False
    
    # Test system prompt
    if not test_system_prompt():
        all_tests_passed = False
    
    print("\n" + "="*50)
    if all_tests_passed:
        print("🎉 All tests passed! Your CLI is ready to use.")
        print("\nNext steps:")
        print("1. Copy env_example.txt to .env")
        print("2. Add your API keys to .env")
        print("3. Run: python cli.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\nTry running: pip install -r requirements.txt")
    
    print("="*50)

if __name__ == '__main__':
    main()
