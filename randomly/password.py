import random
import string
from typing import Optional


def generate_password(
    chars: int,
    punctuation: bool,
    invalid_chars: Optional[list] = None
) -> str:
    """Create a string of random characters

    Args:
        chars: number of characters in return string
        punctuation: whether to use punctuation characters
        invalid_chars: list of characters not to use

    Returns:
        str: A string of random characters
    """
    valid_chars = string.ascii_letters + string.digits

    # Only include punctuation characters if specified.
    if punctuation:
        valid_chars += string.punctuation

    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # creates a list of characters randomly chosen and then turns them into a string
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
