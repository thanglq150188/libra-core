import re
import pydantic
from typing import Dict, Any

def to_pascal(snake: str) -> str:
    """Convert a snake_case string to PascalCase.

    Args:
        snake (str): The snake_case string to be converted.

    Returns:
        str: The converted PascalCase string.
    """
    # Check if the string is already in PascalCase
    if re.match(r'^[A-Z][a-zA-Z0-9]*([A-Z][a-zA-Z0-9]*)*$', snake):
        return snake
    # Remove leading and trailing underscores
    snake = snake.strip('_')
    # Replace multiple underscores with a single one
    snake = re.sub('_+', '_', snake)
    # Convert to PascalCase
    return re.sub(
        '_([0-9A-Za-z])',
        lambda m: m.group(1).upper(),
        snake.title(),
    )
    

def json_to_well_formatted(data: Dict[str, str]) -> str:
    well_formatted_text = ""
    for key in data:
        well_formatted_text += f'{key}: {data[key]}\n'
    return well_formatted_text


PYDANTIC_V2 = pydantic.VERSION.startswith("2.")


from typing import Any, Union

def json_to_simple_format(data: Union[dict, list, Any], prefix: str = '') -> str:
    """
    Convert a JSON-serializable Python object to a simple key-value format.
    
    Args:
    data (Union[dict, list, Any]): The data to format. Can be a dict, list, or any JSON-serializable type.
    prefix (str): The prefix to use for nested structures (used for recursion).
    
    Returns:
    str: A formatted string representation of the input data.
    """
    result = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                result.append(f"{prefix}{key}:")
                result.append(json_to_simple_format(value, prefix + '  '))
            else:
                result.append(f"{prefix}{key}: {_format_value(value)}")
    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, (dict, list)):
                result.append(f"{prefix}{i}:")
                result.append(json_to_simple_format(item, prefix + '  '))
            else:
                result.append(f"{prefix}{i}: {_format_value(item)}")
    
    else:
        result.append(f"{prefix}{_format_value(data)}")
    
    return '\n'.join(result)

def _format_value(value: Any) -> str:
    """Helper function to format individual values."""
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)

# Example usage
if __name__ == "__main__":
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "grades": [85, 90, 78, 92],
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "country": "USA"
        },
        "hobbies": ["reading", "swimming", None],
        "metadata": {
            "last_updated": "2023-08-17",
            "version": 1.1
        }
    }

    formatted_output = json_to_simple_format(sample_data)
    print(formatted_output)