# Supply Chain Tracking System



supply\_chain\_tracking/

│── main.py               # Entry point (menu-driven program)

│── shipment.py           # Shipment class

│── tracker.py            # Tracker class to manage multiple shipments

│── report.py             # Reporting and history

│── exceptions.py         # Custom exceptions

│── utils.py              # Helper utilities

│── data/                 

│   └── sample\_data.json  # Optional dataset

│── README.md             # Project details + instructions





\## Domain

Logistics \& Supply Chain



\## Problem Statement

Create a system to track shipments across supply chain stages.  

Each shipment should have:

\- A unique ID

\- Current status

\- History of updates



\## Learning Goals

\- Understand object-oriented programming (OOP)

\- Work with multiple classes (`Shipment`, `Tracker`)

\- Implement history tracking with timestamps

\- Practice file handling \& reporting

\- Handle custom exceptions



\## proess for supplaychain tracking system.

1\. Implement the \*\*Shipment class\*\* (ID, status, history).

2\. Implement the \*\*Tracker class\*\* (manage multiple shipments).

3\. Build a menu in `main.py` to:

&nbsp;  - Add shipments

&nbsp;  - Update statuses

&nbsp;  - View history

&nbsp;  - Generate reports

4\. Use `utils.py` for ID generation.

5\. Add error handling with custom exceptions.




\- Validate status (only allow: "Created", "Dispatched", "In Transit", "Delivered")




