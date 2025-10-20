"""
Utility functions
-----------------
Helpers for validation, ID generation, etc.
"""

import uuid

def generate_shipment_id():
    """
    Generate a unique shipment ID.
    Hint: Use uuid.uuid4().hex[:6]
    """
    # IMPLEMENTATION: Use uuid to generate a short, unique ID
    return uuid.uuid4().hex[:6].upper()
