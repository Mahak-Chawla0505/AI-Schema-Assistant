import re

def sanitize_table_name(name: str) -> str:
    """
    Converts a user-provided table name into a safe SQL identifier.
    - Replaces spaces and hyphens with underscores
    - Removes special characters
    - Ensures it starts with a letter or underscore
    """
    name = name.strip().lower()
    name = re.sub(r"[^\w\s]", "", name)         # Remove special characters
    name = re.sub(r"[\s\-]+", "_", name)        # Replace spaces/hyphens with underscores
    if not re.match(r"^[a-zA-Z_]", name):
        name = f"t_{name}"                      # Prefix if it starts with a digit
    return name