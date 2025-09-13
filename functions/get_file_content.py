# functions/get_file_content.py
import os
import config

def get_file_content(working_directory, file_path):
    """
    Safely reads the content of a file within a specific working directory.

    Args:
        working_directory (str): The directory where operations are permitted.
        file_path (str): The path to the file, relative to the working directory.

    Returns:
        str: The content of the file, or an error message.
    """
    try:
        # Create absolute paths for security checks
        base_path = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(base_path, file_path))

        # Security check: Ensure the resolved path is within the working directory
        if not full_file_path.startswith(base_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if the path points to a regular file
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file content
        with open(full_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Truncate if the content is too long
        if len(content) > config.MAX_FILE_SIZE:
            truncated_content = content[:config.MAX_FILE_SIZE]
            return f'{truncated_content}[...File "{file_path}" truncated at {config.MAX_FILE_SIZE} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"