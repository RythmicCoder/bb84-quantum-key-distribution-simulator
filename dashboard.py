import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bb84_simulation import run_bb84

st.set_page_config(layout="wide")

st.title("BB84 Quantum Key Distribution Visual Simulator")

st.write(
"This simulator demonstrates the complete BB84 protocol including Alice, Eve, and Bob interactions."
)


visual_photons = st.slider(
    "Number of Photons",
    5,
    50,
    10
)

attack_probability = st.slider(
    "Eavesdropping Probability",
    0.0,
    0.5,
    0.1
)

analysis_photons = 1000
analysis = run_bb84(analysis_photons, attack_probability)

qber = analysis[-2]
skr = analysis[-1]

st.header("Security Result")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("QBER", round(qber,4))

with col2:
    st.metric("Secret Key Rate", round(skr,4))

with col3:
    st.metric("Security Threshold", "0.11")

if qber < 0.11:
    st.success("Channel Secure")
else:
    st.error("Channel Insecure (Eavesdropping Detected)")


st.header("Attack Impact Analysis")

attack_vals = np.linspace(0,0.5,20)

qbers=[]
skrs=[]

for p in attack_vals:

    result = run_bb84(2000,p)

    qbers.append(result[-2])
    skrs.append(result[-1])


col1, col2 = st.columns(2)

with col1:

    fig1, ax1 = plt.subplots(figsize=(5,3))

    ax1.plot(attack_vals,qbers,label="QBER")
    ax1.axhline(y=0.11,color="red",linestyle="--",label="Security Threshold")

    ax1.set_xlabel("Attack Probability")
    ax1.set_ylabel("QBER")
    ax1.set_title("Attack Probability vs QBER")

    ax1.legend()

    st.pyplot(fig1)


with col2:

    fig2,ax2 = plt.subplots(figsize=(5,3))

    ax2.plot(attack_vals,skrs,color="green")

    ax2.set_xlabel("Attack Probability")
    ax2.set_ylabel("Secret Key Rate")
    ax2.set_title("Attack Probability vs SKR")

    st.pyplot(fig2)


if st.button("View Protocol Explanation"):

    (
        alice_bits,
        alice_bases,
        eve_attack,
        eve_bases,
        bob_bases,
        bob_results,
        matching,
        alice_key,
        bob_key,
        _,
        _
    ) = run_bb84(visual_photons, attack_probability)

    st.header("Protocol Explanation")

    st.subheader("Step 1: Alice Generates Random Bits")

    df1 = pd.DataFrame({
        "Photon": range(1, visual_photons+1),
        "Alice Bit": alice_bits
    })

    st.table(df1)


    st.subheader("Step 2: Alice Chooses Random Bases")

    df2 = pd.DataFrame({
        "Photon": range(1, visual_photons+1),
        "Alice Bit": alice_bits,
        "Alice Basis": alice_bases
    })

    st.table(df2)


    st.subheader("Step 3: Photon Polarization Encoding")

    polarization = []

    for bit,basis in zip(alice_bits,alice_bases):

        if basis == "+":
            polarization.append("Vertical" if bit else "Horizontal")
        else:
            polarization.append("135°" if bit else "45°")

    df3 = pd.DataFrame({
        "Photon":range(1,visual_photons+1),
        "Bit":alice_bits,
        "Basis":alice_bases,
        "Polarization":polarization
    })

    st.table(df3)


    st.subheader("Step 4: Eve Intercepts Photons")

    df4 = pd.DataFrame({
        "Photon":range(1,visual_photons+1),
        "Eve Attack":eve_attack,
        "Eve Basis":eve_bases
    })

    st.table(df4)


    st.subheader("Step 5: Bob Measures Photons")

    df5 = pd.DataFrame({
        "Photon":range(1,visual_photons+1),
        "Bob Basis":bob_bases,
        "Bob Result":bob_results
    })

    st.table(df5)


    st.subheader("Step 6: Basis Comparison")

    df6 = pd.DataFrame({
        "Photon":range(1,visual_photons+1),
        "Alice Basis":alice_bases,
        "Bob Basis":bob_bases,
        "Same Basis":matching
    })

    st.table(df6)


    st.subheader("Step 7: Raw Key Formation")

    raw_df = pd.DataFrame({
        "Alice Key":alice_key,
        "Bob Key":bob_key
    })

    st.table(raw_df)