import re

def solve(caption: str) -> str:
    # Remove non-alphabetic characters except spaces
    cleaned_caption = re.sub(r'[^a-zA-Z ]', '', caption)
    
    # Split the caption into words
    words = cleaned_caption.split()
    
    # Create camelCase string
    if not words:
        return "#"
    
    # Start with the first word in lowercase
    tag = [words[0].lower()]
    
    # Capitalize the first letter of each subsequent word
    for word in words[1:]:
        tag.append(word.capitalize())
    
    # Join all parts into a single string and prefix with '#'
    camel_case_tag = '#' + ''.join(tag)
    
    # Truncate to a maximum of 100 characters
    return camel_case_tag[:100]