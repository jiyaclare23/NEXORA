<img width="905" height="427" alt="image" src="https://github.com/user-attachments/assets/795403ff-2740-4fce-a8bd-bc7f9768561c" /># NEXORA

Team ID: [OPCO040]

1. Problem Statement

Operational Technology (OT) systems are widely used in industrial environments to monitor and control critical equipment. Cyberattacks or abnormal sensor readings can affect the safe operation of industrial devices, potentially leading to equipment damage, production downtime, and operational risks.

Traditional monitoring systems may not provide a clear, centralized view of suspicious activity, incident severity, and recommended response actions. Therefore, a simple and effective monitoring solution is needed to identify simulated anomalies, highlight potential cyber threats, and help operators understand incidents quickly.

2. Solution Title

OT CyberShield: Industrial Anomaly Detection and Incident Monitoring System

3. Solution Description

OT CyberShield is a Streamlit-based dashboard designed to simulate and monitor potential cybersecurity incidents in Operational Technology environments. The system identifies simulated abnormal current readings and potential multi-parameter manipulation attacks, then displays relevant threat alerts and severity levels. It provides recommended actions, incident details, affected device information, and incident history in a structured dashboard. The solution helps users understand potential industrial cyber threats and supports faster incident investigation through a simple, centralized interface.

Key Features

- Simulated OT sensor monitoring and abnormal current detection.
- Potential cyberattack and anomaly alert display.
- Threat severity classification, including critical alerts.
- Recommended actions for investigating and isolating affected devices.
- Incident details, including incident ID, affected device, attack type, severity, and status.
- Incident history displayed in a table.
- Interactive dashboard for monitoring simulated incidents.

4. Architecture Diagram
<https://github.com/jiyaclare23/NEXORA.git/arc.jpeg>
 
Workflow

1. Input and Simulation: Simulated sensor readings and industrial device parameters are provided to the application.
2. Anomaly Detection: The application evaluates the simulated readings against configured conditions.
3. Threat Identification: Potential abnormal activity is identified and categorized.
4. Severity Assessment: The dashboard displays the relevant alert and threat severity.
5. Recommended Actions: Suggested investigation, verification, and isolation steps are presented to the operator.
6. Incident Dashboard: Incident details and history are displayed in tables using Streamlit.

Note: The current implementation is a simulation and should not be considered a validated industrial intrusion detection system.

5. Technology Stack

- Frontend: Streamlit web interface
- Backend: Python
- Database: Not currently implemented; incident information is simulated and displayed in the application.
- Data Processing: Python-based condition checks and simulated sensor readings
- Visualization: Streamlit alerts, tables, and dashboard components
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub

6. Quick Start Guide

Prerequisites

- Python 3.10 or a compatible version
- pip (Python package installer)
- Visual Studio Code or another Python-compatible editor
- Git (optional, for version control)

Installation and Execution

Clone the repository:

git clone <https://github.com/jiyaclare23/NEXORA.git>
cd <https://github.com/jiyaclare23/NEXORA.git/project.py>

Create and activate a virtual environment (recommended):

Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install the required dependency:

pip install streamlit

If the project contains a "requirements.txt" file, install all dependencies using:

pip install -r requirements.txt

Run the application:

streamlit run project.py

Replace "project.py" with the actual Python filename if your main application file has a different name.

After the application starts, open the local URL displayed in the terminal, usually:

http://localhost:8501

7. Output Screenshots

"Output Screenshot" (https://github.com/jiyaclare23/NEXORA.git/op.png)
(https://github.com/jiyaclare23/NEXORA.git/op2.png)


Output Description

The dashboard presents simulated industrial cybersecurity monitoring results in a structured and user-friendly format. It displays abnormal current alerts, threat severity, recommended actions, incident details, and incident history.

The incident table includes fields such as:

- Incident ID
- Affected Device
- Attack Type
- Severity
- Status

For example, a simulated incident may identify Motor Controller 01 as the affected device, classify the event as Multi-Parameter Manipulation, assign CRITICAL severity, and show the status as Under Investigation.

The example incident represents simulated data and does not indicate a confirmed real-world cyberattack.

8. Future Scope

- Integrate real-time sensor data from industrial monitoring devices or authorized OT test environments.
- Implement machine learning-based anomaly detection for identifying more complex attack patterns.
- Add persistent incident storage using SQLite, PostgreSQL, or another suitable database.
- Introduce incident filtering, search, timestamps, and downloadable incident reports.
- Add role-based access control and secure authentication.
- Implement configurable alert thresholds and notification mechanisms.
- Test and validate detection accuracy using representative datasets and controlled simulations.
- Integrate with established security monitoring platforms or SIEM systems where appropriate.

9. Team Contributions

Krishna Pradha 
Project planning, problem identification, and industrial sensor simulation
Jiya Clare Gigi
Python programming, anomaly detection, and threat severity analysis
John Francy
Streamlit dashboard development, incident details, and incident history
Sebin Johny
Recommended response actions, testing, documentation, and Telegram notification integration


10. Tools Used

- Python – Core programming language for the project logic.
- Streamlit – To build the interactive web dashboard.
- Visual Studio Code (VS Code) – Code editor used for development.
- GitHub – To store and share the project source code and documentation.
- Web Browser – To run and view the Streamlit dashboard.

---

Disclaimer: OT CyberShield is a hackathon prototype intended for demonstration and educational purposes. Its simulated alerts and detection logic must be validated before any use in real industrial environments.
