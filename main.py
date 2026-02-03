"""
Main entry point for the application
Handles core functionality and module integration
"""
from config import settings
from utils import helpers

def main():
    """Primary application workflow"""
    print(f"Starting {settings.APP_NAME} (v{settings.VERSION})")
    
    # Process data
    data = [1, 5, 3, 8, 2]
    print(f"Original data: {data}")
    
    # Use helper functions
    print(f"Sorted data: {helpers.sort_data(data)}")
    print(f"Sum: {helpers.calculate_sum(data)}")
    
    print("Application completed successfully")

if __name__ == "__main__":
    main()