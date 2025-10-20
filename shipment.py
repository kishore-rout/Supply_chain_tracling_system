"""
Shipment class
--------------
Represents a single shipment in the supply chain.
Attributes:
- shipment_id
- current_status
- history (list of updates)
"""
from datetime import datetime
from exceptions import InvalidStatusError

class Shipment:
    def __init__(self, shipment_id, origin, destination):
        """
        Initialize shipment with ID, origin, destination.
        Hint: Store history as a list of tuples (status, timestamp).
        """
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        initial_status = "created"
        self.current_status = initial_status
        self.history = [(initial_status, datetime.now())]

    def update_status(self, status):
        """
        Update the shipment status and append it to history.
        Hint: Use datetime.now() for timestamp.
        """
        if not isinstance(status, str):
            raise InvalidStatusError("Status must be string type.")
        
        self.current_status = status
        timestamp = datetime.now()
        
        self.history.append((self.current_status, timestamp))
        print(f"Status updated successfully to: {status}")
        
    def get_history(self):
        """
        Return the history of the shipment.
        """
        return self.history