"""
This script removes the import line "from openapi_generated.pinterest_client.model.bool_none_type import BoolNoneType"
from all Python files in the 'openapi_generated' directory and its subdirectories. This is to fix the error:
"ModuleNotFoundError: No module named 'openapi_generated.pinterest_client.model.bool_none_type'"
"""
import os

directory = '../openapi_generated'
line_to_remove = "from openapi_generated.pinterest_client.model.bool_none_type import BoolNoneType"

print("Starting the script to remove the specified import line from all Python files in the 'openapi_generated' directory...")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(file_path, 'w', encoding='utf-8') as f:
                for line in lines:
                    if line.strip() != line_to_remove:
                        f.write(line)
                    else:
                        print(f"Removed line from: {file_path}")

print("Script completed. The specified import line has been removed from all Python files in the 'openapi_generated' directory.")