from Crypto.PublicKey import RSA
import base64

def parse_base64_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove leading/trailing whitespaces and newlines
    lines = [line.strip() for line in lines]

    # Find start and end markers
    start_marker = '-----BEGIN'
    end_marker = '-----END'

    # Find the index of the start marker
    start_index = next((i for i, line in enumerate(lines) if start_marker in line), None)
    if start_index is None:
        raise ValueError("Start marker not found")

    # Find the index of the end marker
    end_index = next((i for i, line in enumerate(lines) if end_marker in line), None)
    if end_index is None:
        raise ValueError("End marker not found")

    # Extract base64-encoded data
    base64_data = ''.join(lines[start_index+1:end_index])

    return base64_data

# Example usage:
file_path = "privacy_enhanced_mail.pem"
base64_data = parse_base64_from_file(file_path)

# Decode base64 data
decoded_data = base64.b64decode(base64_data)
key=RSA.import_key(decoded_data)

print(key.d)
