"""Utility functions for data operations"""
def sort_data(data: list) -> list:
    """Sorts numerical data in ascending order"""
    return sorted(data)

def calculate_sum(data: list) -> float:
    """Calculates sum of numerical values"""
    return sum(data)

def calculate_average(data: list) -> float:
    """Calculates average of numerical values"""
    return sum(data) / len(data) if data else 0