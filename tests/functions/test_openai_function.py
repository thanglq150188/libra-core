from libra.functions import OpenAIFunction

# Define a sample function
def sample_function(input_text: str, threshold: float) -> bool:
    """
    Một hàm mẫu kiểm tra xem độ dài của văn bản đầu vào có vượt quá ngưỡng cho trước hay không.

    Args:
        input_text (str): Văn bản đầu vào cần kiểm tra.
        threshold (float): Độ dài ngưỡng.

    Returns:
        bool: True nếu độ dài của văn bản đầu vào vượt quá ngưỡng, False trong trường hợp ngược lại.
    """
    return len(input_text) > threshold

# Create an OpenAIFunction object for the sample function
sample_openai_function = OpenAIFunction(sample_function)

# Get the OpenAI tool schema for the sample function
sample_tool_schema = sample_openai_function.get_openai_tool_schema()

# Print the tool schema
print(sample_tool_schema)

# Validate the tool schema
OpenAIFunction.validate_openai_tool_schema(sample_tool_schema)

# Use the sample function with some inputs
input_text = "Hello, world!"
threshold = 10
result = sample_openai_function.func(input_text, threshold)

# Print the result
print(result)