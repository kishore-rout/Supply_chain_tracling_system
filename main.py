# main.py
"""
Main entry point for Supply Chain Tracking System
-------------------------------------------------
Provides a menu-driven interface to manage shipments.
"""

from shipment import Shipment
from tracker import Tracker
from utils import generate_shipment_id
from report import generate_shipment_report, export_to_file 
from exceptions import ShipmentNotFoundError, InvalidStatusError

def create_shipment_menu(tracker):
    """Handles the creation and addition of a new shipment."""
    try:
        # Generate ID automatically
        shipment_id = generate_shipment_id() 
        print(f"\n--- Creating New Shipment (ID: {shipment_id}) ---")
        
        origin = input("Enter Origin Location: ").strip()
        destination = input("Enter Destination Location: ").strip()
        
        if not origin or not destination:
            print(" Error: Origin and Destination must be provided.")
            return

        new_shipment = Shipment(shipment_id, origin, destination)
        tracker.add_shipment(new_shipment)
        print(f" Success! Shipment {shipment_id} created (Origin: {origin}, Destination: {destination}).")

    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def update_status_menu(tracker):
    """Handles updating the status of an existing shipment."""
    print("\n--- Update Shipment Status ---")
    shipment_id = input("Enter Shipment ID to update: ").strip()
    status = input("Enter New Status (e.g., 'in_transit', 'delivered'): ").strip()
    
    try:
        # The tracker method calls the shipment's update_status, which manages history
        tracker.update_shipment_status(shipment_id, status)
        # Note: update_status already prints a success message.
        
    except ShipmentNotFoundError as e:
        print(f" Error: {e}")
    except InvalidStatusError as e:
        print(f" Error: {e}")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def view_details_menu(tracker):
    """Handles viewing the detailed report and history of a single shipment."""
    print("\n--- View Shipment Details & History ---")
    shipment_id = input("Enter Shipment ID to view details: ").strip()
    
    try:
        # Get the Shipment object
        shipment = tracker.get_shipment_by_id(shipment_id)
        
        # Use the generate_shipment_report function from report.py
        report = generate_shipment_report(shipment)
        print("\n" + report)
        
    except ShipmentNotFoundError as e:
        print(f" Error: {e}")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def generate_report_menu(tracker):
    """
    Handles generating the system-wide summary and printing it to the console.
    File export logic has been removed as requested.
    """
    print("\n--- Generate System Summary Report ---")
    
    # Generate the summary report from the Tracker
    summary_report = tracker.generate_report()
    
    # Print the report to the console
    print("\n" + summary_report)

    # NO FILE EXPORT PROMPT OR CALL

def main():
    """
    Main function to run the Supply Chain Tracking System loop.
    """
    tracker = Tracker()
    print(" Supply Chain Tracking System Initialized.")
    
    while True:
        print("\n==================================")
        print("Supply Chain Tracking Menu")
        print("1. Create New Shipment")
        print("2. Update Shipment Status")
        print("3. View Shipment Details & History")
        print("4. Generate System Summary Report")
        print("5. Exit")
        print("==================================")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            create_shipment_menu(tracker)
        elif choice == '2':
            update_status_menu(tracker)
        elif choice == '3':
            view_details_menu(tracker)
        elif choice == '4':
            generate_report_menu(tracker)
        elif choice == '5':
            print("Exiting system. Goodbye! ")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()