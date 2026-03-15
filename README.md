# BB84 Quantum Key Distribution Visual Simulator

An interactive simulator demonstrating the **BB84 Quantum Key Distribution (QKD) protocol**, one of the most important protocols in **quantum cryptography** for secure communication.

This project models the interaction between **Alice (sender), Bob (receiver), and Eve (eavesdropper)** and shows how quantum communication can detect eavesdropping through the **Quantum Bit Error Rate (QBER)**.

The simulator allows users to explore how increasing the **probability of interception** affects the **security of the communication channel**.

---

# 🏆 Achievement

This project secured **1st Place at Quantum Quest 2026**, organized by the **Department of IT in association with CSI@MPSTME at NMIMS**.

The event focused on innovative ideas in **Quantum Computing and Quantum Technologies**.

---

#  Key Concepts Demonstrated

This simulator illustrates important concepts from **Quantum Cryptography**:

- Quantum Key Distribution (QKD)
- BB84 Protocol
- Photon Polarization Encoding
- Random Basis Selection
- Eavesdropping Detection
- Quantum Bit Error Rate (QBER)
- Secret Key Rate (SKR)

---

# ⚛️ BB84 Protocol Overview

The BB84 protocol works through the following steps:

### 1. Alice Generates Random Bits
Alice generates a sequence of random binary bits.

### 2. Alice Chooses Random Bases
Each bit is encoded using a randomly chosen basis:

- Rectilinear (+)
- Diagonal (×)

### 3. Photon Polarization Encoding

Rectilinear Basis (+)

0 → Horizontal  
1 → Vertical  

Diagonal Basis (×)

0 → 45°  
1 → 135°

### 4. Transmission Through Quantum Channel
Alice sends photons to Bob.

### 5. Eve Interception (Optional Attack)
An attacker (Eve) may intercept photons and measure them.

Because Eve does not know the correct basis, her measurement may disturb the photon state.

### 6. Bob Measures Photons
Bob randomly selects bases to measure incoming photons.

### 7. Basis Reconciliation
Alice and Bob publicly compare bases (not the bits).

Only bits with **matching bases** are kept.

### 8. Raw Key Formation
The remaining bits form the **raw key**.

### 9. Security Check Using QBER
Alice and Bob compare a small sample of bits to compute the **Quantum Bit Error Rate (QBER)**.

If QBER exceeds the threshold (~11%), the channel is considered **insecure**.

---

#  Simulator Features

- Interactive **Streamlit Dashboard**
- Adjustable **number of photons**
- Adjustable **eavesdropping probability**
- Visualization of **BB84 protocol steps**
- Tabular representation of:

  - Alice's bits
  - Alice's bases
  - Photon polarization
  - Eve interception
  - Bob measurement
  - Basis comparison
  - Raw key formation

- Automatic calculation of:

  - Quantum Bit Error Rate (QBER)
  - Secret Key Rate (SKR)

- Security decision:

  - Channel Secure
  - Channel Insecure

- Graphs showing:

  - Attack Probability vs QBER
  - Attack Probability vs Secret Key Rate

---

#  Project Structure
dashboard.py
bb84_simulation.py
requirements.txt
README.md
