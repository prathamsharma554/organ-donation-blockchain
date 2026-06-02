# 🔗 Secure Organ Donation Registry Using Blockchain

A decentralized, transparent, and tamper-proof medical registry application built using **Python**, **Cryptography (SHA-256)**, **Streamlit**, and **Matplotlib**. This system ensures that organ donation pledges are recorded immutably, eliminating data tampering and maintaining transparency.

## 🚀 Key Features
- **Custom Blockchain Architecture:** Implemented a secure cryptographic ledger using SHA-256 hashing to chain blocks sequentially.
- **Dual Portal Framework:**
  - **User Portal:** Allows donors to self-register their organ donation pledges directly into the blockchain node network.
  - **Central Authority Admin Panel:** Protected by a secure checkpoint (`pune123`) for health authorities to monitor the master ledger.
- **Live Analytics Dashboard:** Integrated real-time data metrics and visualization bar charts using Matplotlib to monitor organ availability statistics.
- **Data Persistence:** Utilized Streamlit session state architecture to maintain continuous ledger blocks during active sessions.

## 🛠️ Tech Stack & Concepts
- **Language:** Python
- **Frontend / Interface:** Streamlit (Web Framework)
- **Security & Data Integrity:** Hashlib (SHA-256), JSON (Data Serialization)
- **Data Analytics:** NumPy, Matplotlib (Data Visualization)
- **Core Concepts:** Decentralized Ledgers, Cryptographic Hashing, Genesis Block Generation, Immutable Smart Records.

## ⚙️ Project Structure
```text
Organ-Donation-Blockchain/
│
├── app.py          # Main application core logic and Streamlit layout
└── README.md       # Project documentation and architectural overview
```

## 💻 How to Run Locally
1. Clone or download this repository.
2. Open the terminal inside the project directory.
3. Install the required dependencies:
   ```bash
   pip install streamlit matplotlib numpy
   ```
4. Run the local development server:
   ```bash
   streamlit run app.py
   ```