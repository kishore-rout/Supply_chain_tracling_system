"""
Tracker class
-------------
Responsible for managing multiple shipments.
Methods:
- add_shipment
- get_shipment_by_id
- update_shipment_status
- generate_report
"""

from exceptions import ShipmentNotFoundError
# Import both Shipment and InvalidStatusError (for thorough error handling)
from shipment import Shipment 
from exceptions import InvalidStatusError 

class Tracker:
    def __init__(self):
        """
        Initialize tracker with a dictionary of shipments.
        Hint: Key = shipment_id, Value = Shipment object
        """
        # Initialize an empty dictionary to hold shipments
        self.shipments = {}
        
    def add_shipment(self, shipment):
        """Add a new shipment to the tracker."""
        if not isinstance(shipment, Shipment):
            raise ValueError("Can only add Shipment objects to the Tracker.")
        self.shipments[shipment.shipment_id] = shipment
        print(f"Shipment {shipment.shipment_id} added.")

    def get_shipment_by_id(self, shipment_id):
        """Return a shipment if it exists, else raise an exception."""
        if shipment_id not in self.shipments:
            raise ShipmentNotFoundError(f"Shipment ID '{shipment_id}' not found.")
        return self.shipments[shipment_id]

    def update_shipment_status(self, shipment_id, status):
        """Update status of a specific shipment."""
        
        # This will raise ShipmentNotFoundError if ID is invalid
        shipment = self.get_shipment_by_id(shipment_id)
        
        # This will also handle the InvalidStatusError check
        shipment.update_status(status)
        
    def generate_report(self):
        """
        Generate a summary of all shipments.
        Hint: Loop over dictionary and format details.
        """
        if not self.shipments:
            return "No shipments to report."
            
        report_lines = ["--- Shipment Summary Report ---"]
        
        for shipment_id, shipment in self.shipments.items():
            line = f"ID: {shipment_id:<6} | Origin: {shipment.origin:<6} | Destination: {shipment.destination:<6} | Status: {shipment.current_status}"
            report_lines.append(line)
            
        return "\n".join(report_lines)

tracker = Tracker()

shipment1 = Shipment("101", "BBSR", "CTC")
shipment2 = Shipment("102", "BBSR", "PURI")

tracker.add_shipment(shipment1)
tracker.add_shipment(shipment2)

print(f"\nRetrieved Object: {tracker.get_shipment_by_id('101')}") 

print("\n--- Updating Status ---")
tracker.update_shipment_status("101", "in_transit")
tracker.update_shipment_status("102", "out_for_delivery")

print("\n--- Final Report ---")
print(tracker.generate_report())