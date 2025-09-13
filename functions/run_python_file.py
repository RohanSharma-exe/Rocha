import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    """
    Executes a Python file in a specified working directory with a timeout.

    Args:
        working_directory (str): The directory where the command will be executed.
        file_path (str): The path to the Python file, relative to the working directory.
        args (list, optional): A list of string arguments to pass to the script. Defaults to [].

    Returns:
        str: The captured stdout, stderr, and exit code, or an error message.
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security check: Ensure the file is within the working directory.
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Validation check: Ensure the file exists.
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    # Validation check: Ensure the file is a Python file.
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # Construct the command to be executed.
        command = ["python", abs_file_path] + args

        # Execute the command using subprocess.run.
        completed_process = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=30  # 30-second timeout
        )

        # Prepare the output string.
        output_parts = []
        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout.strip()}")

        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr.strip()}")

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except subprocess.TimeoutExpired:
        return f"Error: Execution of '{file_path}' timed out after 30 seconds."
    except Exception as e:
        return f"Error executing Python file: {e}"