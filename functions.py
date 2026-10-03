"""Reusable utility functions for the CIT 105 Week 2 assignment."""

from __future__ import annotations

import math
import re
from typing import Any
from urllib.parse import urlparse

DEFAULT_TRUNCATE_LIMIT = 20


def celsius_to_fahrenheit(c):
    """Convert a temperature in Celsius to Fahrenheit.

    Parameters:
        c (int | float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        TypeError: If the input is not numeric.
    """
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("celsius_to_fahrenheit() requires a numeric value.")
    return (c * 9 / 5) + 32


def line_total(price, qty):
    """Calculate the total cost for a quantity of items.

    Parameters:
        price (int | float): Unit price.
        qty (int | float): Quantity to purchase.

    Returns:
        float: The total price.

    Raises:
        TypeError: If price or quantity is not numeric.
        ValueError: If quantity is negative.
    """
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("line_total() price must be numeric.")
    if isinstance(qty, bool) or not isinstance(qty, (int, float)):
        raise TypeError("line_total() quantity must be numeric.")
    if qty < 0:
        raise ValueError("line_total() quantity cannot be negative.")
    return price * qty


def initials(full_name):
    """Return the uppercase initials from a person's full name.

    Parameters:
        full_name (str): A full name with one or more words.

    Returns:
        str: The initials as a single uppercase string.

    Raises:
        TypeError: If the name is not a string.
        ValueError: If the name is empty or whitespace only.
    """
    if not isinstance(full_name, str):
        raise TypeError("initials() requires a string input.")
    cleaned = " ".join(full_name.split())
    if not cleaned:
        raise ValueError("initials() input cannot be empty.")
    initials_list = [part[0].upper() for part in cleaned.split() if part]
    return "".join(initials_list)


def is_valid_url(text):
    """Return True if the text is a valid HTTP or HTTPS URL.

    Parameters:
        text (str): Candidate URL.

    Returns:
        bool: True if the value is a valid URL, otherwise False.
    """
    if not isinstance(text, str):
        return False
    cleaned = text.strip()
    if not cleaned:
        return False
    parsed = urlparse(cleaned)
    schemes = {"http", "https"}
    return parsed.scheme.lower() in schemes and bool(parsed.netloc)


def truncate(text, limit=DEFAULT_TRUNCATE_LIMIT):
    """Shorten text with an ellipsis when truncation is needed.

    The ellipsis counts toward the limit, so the final returned string will not
    exceed the provided limit.

    Parameters:
        text (str): Original content.
        limit (int): Maximum number of characters allowed in the return value.

    Returns:
        str: The original text or a shortened version.

    Raises:
        TypeError: If text is not a string or limit is not an integer.
        ValueError: If the limit is less than or equal to zero.
    """
    if not isinstance(text, str):
        raise TypeError("truncate() text must be a string.")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("truncate() limit must be an integer.")
    if limit <= 0:
        raise ValueError("truncate() limit must be greater than zero.")

    if len(text) <= limit:
        return text

    ellipsis = "..."
    if limit <= len(ellipsis):
        return ellipsis[:limit]

    return text[: limit - len(ellipsis)] + ellipsis


def safe_filename(text):
    """Convert arbitrary text into a filename-safe string.

    The output contains no spaces, forward slashes, backslashes, single quotes,
    or double quotes. Empty or blank values become "untitled".

    Parameters:
        text (str): Source text for the filename.

    Returns:
        str: A safe filename without unsafe characters.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("safe_filename() requires a string input.")

    clean = text.strip()
    if not clean:
        return "untitled"

    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", clean)
    safe = safe.strip("._-")
    safe = re.sub(r"_+", "_", safe)
    return safe or "untitled"


__all__ = [
    "DEFAULT_TRUNCATE_LIMIT",
    "celsius_to_fahrenheit",
    "line_total",
    "initials",
    "is_valid_url",
    "truncate",
    "safe_filename",
]
