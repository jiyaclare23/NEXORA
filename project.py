import streamlit as st
import random

st.set_page_config(
    page_title="OT-SHIELD",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ OT-SHIELD")
st.subheader("Industrial IoT Cybersecurity Monitoring System")

st.write("### Industrial Sensor Monitoring")

attack = st.button("🚨 Simulate Cyber Attack")

if attack:
    temperature = 148.0
    pressure = 16.4
    rpm = 3400
    voltage = 270.0
    current = 10.5
else:
    temperature = round(random.uniform(65, 85), 2)
    pressure = round(random.uniform(4.5, 6.0), 2)
    rpm = random.randint(1300, 1600)
    voltage = round(random.uniform(225, 235), 2)
    current = round(random.uniform(3.5, 5.0), 2)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Temperature", f"{temperature} °C")
col2.metric("Pressure", f"{pressure} bar")
col3.metric("Motor RPM", rpm)
col4.metric("Voltage", f"{voltage} V")
col5.metric("Current", f"{current} A")

if attack:
    st.error("CYBER ATTACK DETECTED!")
    st.write("### Detected Problems")
    st.write("⚠️ Abnormally high temperature")
    st.write("⚠️ Abnormally high pressure")
    st.write("⚠️ Abnormally high motor speed")
    st.write("⚠️ Abnormally high voltage")
    st.write("⚠️ Abnormally high current")
    st.error("Threat Severity: CRITICAL")
    st.write("### Recommended Actions")
    st.write("1. Investigate the affected device.")
    st.write("2. Verify sensor readings.")
    st.write("3. Isolate the simulated device.")
    st.write("### Incident Details")
    st.write("Incident ID: OT-001")
    st.write("Affected Device: Motor Controller 01")
    st.write("Location: Production Unit A")
    st.write("Attack Type: Multi-Parameter Manipulation")
    st.write("Status: Under Investigation")
    st.write("---")
st.header("Incident History")

if attack:
    st.warning("One simulated incident recorded.")

    st.table({
        "Incident ID": ["OT-001"],
        "Affected Device": ["Motor Controller 01"],
        "Attack Type": ["Multi-Parameter Manipulation"],
        "Severity": ["CRITICAL"],
        "Status": ["Under Investigation"]
    })
else:
    st.info("No incidents detected in the current run.")
   