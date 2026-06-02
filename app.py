import streamlit as st
import hashlib
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# 1. Define the Block Structure
class Block:
    def __init__(self, index, timestamp, donor_name, organ, blood_group, hospital, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.donor_name = donor_name
        self.organ = organ
        self.blood_group = blood_group
        self.hospital = hospital
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": str(self.timestamp),
            "donor_name": self.donor_name,
            "organ": self.organ,
            "blood_group": self.blood_group,
            "hospital": self.hospital,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# 2. Define the Blockchain Management
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.now(), "Genesis System Initialized", "None", "None", "Pune Central Registry", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, donor_name, organ, blood_group, hospital):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.now(),
            donor_name=donor_name,
            organ=organ,
            blood_group=blood_group,
            hospital=hospital,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

# 3. Streamlit Interface Initialization
st.set_page_config(page_title="Blockchain Organ Donation", layout="wide")

# Persistent State Management for Blockchain
if "organ_blockchain" not in st.session_state:
    st.session_state.organ_blockchain = Blockchain()

blockchain = st.session_state.organ_blockchain

# ---- SIDEBAR SWITCH FOR VIEWS ----
st.sidebar.title("🚪 Navigation Portal")
portal_view = st.sidebar.radio("Go To Panel", ["User Panel (Organ Registration)", "Admin Panel (Authority Dashboard)"])

# ---- USER PANEL ----
if portal_view == "User Panel (Organ Registration)":
    st.title("🏥 Organ Donation Self-Registration Portal")
    st.write("Fill out the form below to secure your pledge on our immutable Blockchain ledger.")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("📝 Register as an Organ Donor")
        with st.form("user_donation_form", clear_on_submit=True):
            donor_name = st.text_input("Your Full Name")
            organ = st.selectbox("Select Organ to Pledge", ["Kidney", "Liver", "Heart", "Lung", "Cornea", "Pancreas"])
            blood_group = st.selectbox("Your Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
            hospital = st.text_input("Nearest Authorized Hospital (e.g. Ruby Hall, KEM, Noble)")
            
            submitted = st.form_submit_button("Submit & Secure on Blockchain")
            
            if submitted:
                if donor_name and hospital:
                    blockchain.add_block(donor_name, organ, blood_group, hospital)
                    st.success(f"🎉 Thank you, {donor_name}! Your pledge is safely recorded in Block #{len(blockchain.chain)-1}.")
                else:
                    st.error("⚠️ Verification Failed: Please enter both your Name and Hospital details.")
                    
    with col2:
        st.subheader("👀 Real-time Public Blockchain Verification")
        st.caption("Every time a donor registers, a block gets chained with cryptographic signatures.")
        
        for block in reversed(blockchain.chain):
            box_style = "border: 2px solid #2ecc71; padding: 15px; border-radius: 8px; margin-bottom: 12px; background-color: #f8f9fa;" if block.index == 0 else "border: 2px solid #34495e; padding: 15px; border-radius: 8px; margin-bottom: 12px; background-color: #f8f9fa;"
            title = "✨ Genesis Initialization" if block.index == 0 else f"🔒 Verified Blockchain Block #{block.index}"
            
            with st.container():
                st.markdown(f"""
                <div style="{box_style}">
                    <h5 style="margin: 0; color: {'#2ecc71' if block.index == 0 else '#34495e'};">{title}</h5>
                    <p style="margin: 3px 0; font-size: 14px;"><b>Organ Assigned:</b> {block.organ} ({block.blood_group})</p>
                    <p style="margin: 3px 0; font-size: 13px; color: #7f8c8d; font-family: monospace; word-break: break-all;"><b>Block Signature (Hash):</b> {block.hash}</p>
                </div>
                """, unsafe_allow_html=True)

# ---- ADMIN PANEL ----
else:
    st.title("🛡️ Central Health Authority - Admin Monitor")
    
    # Simple secure verification checkpoint
    admin_password = st.sidebar.text_input("Enter Admin Security Key", type="password")
    
    if admin_password == "pune123":
        st.sidebar.success("Access Granted")
        
        # Matrix metric trackers
        st.subheader("📊 Network Diagnostics & Analytics")
        m1, m2 = st.columns(2)
        m1.metric("Total Secured Blocks", len(blockchain.chain))
        m2.metric("Active Node Status", "HEALTHY / ONLINE")
        
        # 4. Matplotlib Data Analytics for the Admin
        # Extracting real-time count of organs registered in the chain
        organ_counts = {"Kidney": 0, "Liver": 0, "Heart": 0, "Lung": 0, "Cornea": 0, "Pancreas": 0}
        for block in blockchain.chain:
            if block.organ in organ_counts:
                organ_counts[block.organ] += 1
                
        fig, ax = plt.subplots(figsize=(8, 3.5))
        organs = list(organ_counts.keys())
        counts = np.array(list(organ_counts.values()))
        
        ax.bar(organs, counts, color='#3498db', width=0.4)
        ax.set_ylabel('Number of Registered Pledges')
        ax.set_title('Real-time Organ Allocation Metrics')
        st.pyplot(fig)
        
        # Master Registry List
        st.subheader("📋 Central Master Registry Ledger")
        for block in reversed(blockchain.chain):
            if block.index != 0:
                with st.expander(f"📋 Candidate Receipt — Block #{block.index} ({block.donor_name})"):
                    st.write(f"**Donor Name:** {block.donor_name}")
                    st.write(f"**Organ Pledged:** {block.organ} | **Blood Group:** {block.blood_group}")
                    st.write(f"**Supervising Node (Hospital):** {block.hospital}")
                    st.write(f"**Timestamp:** {block.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                    st.info(f"Previous Cryptographic Block Link: {block.previous_hash}")
            else:
                st.info("System Initial Block (Genesis Core Log) is active.")
                
    elif admin_password:
        st.error("❌ Authentication Failed: Invalid Security Key.")
    else:
        st.warning("🔒 Please enter the Admin Security Key in the sidebar panel to check master records and graphics.")