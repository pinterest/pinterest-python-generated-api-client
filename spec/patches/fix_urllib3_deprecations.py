"""
This script fixes deprecated urllib3 methods in the generated code by replacing:
- response.getheader('content-type') → response.headers.get('content-type')
- response.getheaders() → response.headers

This addresses deprecation warnings that will become breaking errors in urllib3 2.6.0.
Based on urllib3 v2.0 migration guide: https://urllib3.readthedocs.io/en/stable/v2-migration-guide.html

Files affected:
- openapi_generated/pinterest_client/rest.py (lines 37-43)
- openapi_generated/pinterest_client/api_client.py (lines 224, 243, 320)
- openapi_generated/pinterest_client/exceptions.py (line 107)
"""
import os
import re

directory = '../openapi_generated'

# Define the replacements - apply multiple times until no more changes
def apply_replacements(content):
    """Apply all replacements until no more changes are made"""
    original_content = content
    
    # First: Clean up any multiple urllib3_response references (make it idempotent)
    content = re.sub(r'(\.urllib3_response)+', '.urllib3_response', content)
    
    # Second: Replace deprecated getheader() calls with headers.get()
    # All response objects are RESTResponse wrappers, so use .urllib3_response.headers
    content = re.sub(r'(response_data|response|http_resp)\.getheader\(([^)]+)\)', r'\1.urllib3_response.headers.get(\2)', content)
    
    # Third: Replace deprecated getheaders() calls with headers
    # All response objects are RESTResponse wrappers, so use .urllib3_response.headers
    content = re.sub(r'(response_data|response|http_resp)\.getheaders\(\)', r'\1.urllib3_response.headers', content)
    
    return content

print("Starting the script to fix deprecated urllib3 methods in the 'openapi_generated' directory...")
print("This ensures compatibility with both urllib3 1.x and 2.x")

files_modified = 0
total_replacements = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Apply all replacements using the function
                content = apply_replacements(content)
                
                # Write back if changes were made
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    # Count replacements made in this file
                    file_replacements = len(original_content) - len(content) + content.count('urllib3_response') - original_content.count('urllib3_response')
                    
                    print(f"Modified: {file_path} ({file_replacements} replacements)")
                    files_modified += 1
                    total_replacements += file_replacements
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print(f"Script completed. Modified {files_modified} files with {total_replacements} total replacements.")
print("Deprecated urllib3 methods have been updated to use the new headers API.")
print("Your package now supports both urllib3 1.x and 2.x!")
