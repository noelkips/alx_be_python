def safe_divide_enhanced(numerator, denominator, precision=1):
    """
    Enhanced version of safe_divide with additional features.
    
    Args:
        numerator: The dividend
        denominator: The divisor
        precision (int): Number of decimal places for the result
        
    Returns:
        str: Result or error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero explicitly (though try-except will catch it)
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / denom
        
        # Format result with specified precision
        if precision == 0:
            return f"The result of the division is {int(result)}"
        else:
            return f"The result of the division is {result:.{precision}f}"
            
    except ValueError as e:
        # More specific error handling for different ValueError scenarios
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except Exception as e:
        # Catch any other unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

def get_division_info(numerator, denominator):
    """
    Get detailed information about a division operation.
    
    Args:
        numerator: The dividend
        denominator: The divisor
        
    Returns:
        dict: Dictionary containing operation details
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        
        if denom == 0:
            return {
                "success": False,
                "error": "Division by zero",
                "numerator": num,
                "denominator": denom,
                "result": None
            }
        
        result = num / denom
        return {
            "success": True,
            "error": None,
            "numerator": num,
            "denominator": denom,
            "result": result,
            "is_integer": result.is_integer(),
            "is_positive": result > 0
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid input - non-numeric values",
            "numerator": numerator,
            "denominator": denominator,
            "result": None
        }