import re
import os

def extract_emails(input_file: str, output_file: str):
    # Standard regex pattern for email validation
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    
    # Edge Case Handling: File existence check
    if not os.path.exists(input_file):
        print(f"System Error: Input file '{input_file}' does not exist.")
        return

    try:
        with open(input_file, "r") as infile:
            content = infile.read()
            
        # Find all matches based on the compiled regex
        emails = email_pattern.findall(content)
        
        # Deduplicate emails using a set, then sort them
        unique_emails = sorted(list(set(emails)))
        
        with open(output_file, "w") as outfile:
            for email in unique_emails:
                outfile.write(f"{email}\n")
                
        print(f"Task Complete. Extracted {len(unique_emails)} unique emails to {output_file}.")
        
    except IOError as e:
        print(f"I/O Error occurred: {e}")

if __name__ == "__main__":
    # To test this, you must create a 'sample_text.txt' file in the same directory.
    with open("sample_text.txt", "w") as f:
        f.write("Contact us at support@example.com or sales@example.com. Invalid: test@test.")
        
    extract_emails("sample_text.txt", "extracted_emails.txt")
