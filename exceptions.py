"""
Custom Exceptions for Supply Chain Tracking
-------------------------------------------
"""

class ShipmentNotFoundError(Exception):
    """Raised when a shipment is not found in the tracker."""
    pass

class InvalidStatusError(Exception):
    """Raised when an invalid status is provided."""
    pass
