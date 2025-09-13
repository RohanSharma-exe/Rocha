import os

def write_file(working_directory, file_path, content):
    """
    Writes content to a file within a specified working directory.

    Args:
        working_directory (str): The directory where file operations are permitted.
        file_path (str): The path to the file to be written, relative to the working directory.
        content (str): The content to write to the file.

    Returns:
        str: A success or error message.
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security check to prevent writing outside the working directory.
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # Get the directory part of the file path.
        dir_name = os.path.dirname(abs_file_path)

        # Create the directory and any parent directories if they don't exist.
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # Open the file in write mode ("w") and write the content.
        # This will create the file if it doesn't exist or overwrite it if it does.
        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"