import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center;  color:#B5C0D0; margin-bottom: 20px;'>Pneumonia Detection</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: justify; margin-bottom: 30px;'>Pneumonia is an inflammatory condition of the lung primarily affecting the microscopic air sacs known as alveoli. It is often caused by infection with bacteria, viruses, or other microorganisms, although it can also result from non-infectious causes such as chemical irritants or aspiration of food or liquids. Symptoms of pneumonia include fever, chills, cough, difficulty breathing, and chest pain. Diagnosis typically involves medical imaging, such as chest X-rays or computed tomography (CT) scans, as well as laboratory tests such as blood cultures and sputum analysis.</p>
    """, unsafe_allow_html=True)
    
    st.image("bgs/4.png", caption="Pneumonia Image")

    st.markdown("""
    <div style='background-color: #f0f0f0; padding: 10px 10px 10px 40px; border-radius: 5px;'>
        <h3 style='color: #333;'>Causes of Pneumonia:</h3>
        <ul style='list-style-type: square; padding-left: 20px; color: black;'>
            <li>Infection with bacteria</li>
            <li>Viral infections</li>
            <li>Fungal infections</li>
            <li>Inhalation of irritants or chemicals</li>
            <li>Aspiration of food, liquids, or vomit into the lungs</li>
            <li>Complications from other respiratory illnesses</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
