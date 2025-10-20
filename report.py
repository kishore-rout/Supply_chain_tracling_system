"""
Report utilities
----------------
Generate and export reports for shipments.
"""
from shipment import Shipment # Required for type hinting/checking

def generate_shipment_report(shipment):
    """
    Generate detailed report for one shipment.
    """
    if not isinstance(shipment, Shipment):
        raise TypeError("Input must be a Shipment object.")
        
    report = [f"--- Shipment Details: {shipment.shipment_id} ---"]
    report.append(f"Origin: {shipment.origin}")
    report.append(f"Destination: {shipment.destination}")
    report.append(f"Current Status: {shipment.current_status}")
    report.append("\nHistory:")
    
    # Format the history list
    for status, timestamp in shipment.get_history():
        report.append(f"  - {timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {status}")
        
    return "\n".join(report)

def export_to_file(data, filename="report.txt"):
    """
    Export report data (string) to a file.
    Hint: Use open(filename, "w") as f
    """
    if not isinstance(data, str):
        raise TypeError("Data to export must be a single string.")
        
    try:
        with open(filename, "w") as f:
            f.write(data)
        print(f"\nReport successfully exported to: {filename}")
    except IOError as e:
        print(f"Error exporting report to file: {e}")
