import streamlit as st

# Function to calculate efficiency and copper losses
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    CUL = (K * IL)**2 * (Rse + Ra)
    Eff = ((K * V * IL) - CL - CUL) / (K * V * IL) * 100
    return Eff, CUL

# Web application title
st.title('2305A21L28 - PS11')

# Input fields
V = st.number_input('Voltage (V)', value=230)
CL = st.number_input('Core Losses (CL) in watts', value=100)
IL = st.number_input('Full Load Current (IL) in Amps', value=15.00)
K = st.number_input('Loading on motor (K)', value=1.0)
Rse = st.number_input('Series field resistance (Rse)', value=0.20)
Ra = st.number_input('Armature Resistance (Ra)', value=0.10)

# Calculate efficiency and copper losses
if st.button('Calculate'):
    Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
    st.write(f'Efficiency (Eff): {Eff:.2f}%')
    st.write(f'Copper Losses (CUL): {CUL:.2f} watts')
