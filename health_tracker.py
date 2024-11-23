import streamlit as st

def health():  
    st.header("Daily Health Tracker")
    
    with st.form("health_tracker_form"):
        date = st.date_input("Date")
        
        col1, col2 = st.columns(2)
        with col1:
            temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)
            sleep_hours = st.number_input("Sleep Duration (hours)", min_value=0, max_value=24)
            
        with col2:
            mood = st.select_slider("Mood", options=["😢", "😐", "🙂", "😊", "😄"])
            appetite = st.select_slider("Appetite", options=["Poor", "Fair", "Good", "Excellent"])
        
        symptoms = st.multiselect(
            "Any Symptoms?",
            ["None", "Fever", "Cough", "Runny Nose", "Stomach Ache", "Headache", "Other"]
        )
        
        notes = st.text_area("Additional Notes")
        
        if st.form_submit_button("Save Entry"):
            entry_data = {
                "ID": str(uuid.uuid4()),
                "Date": str(date),
                "Temperature": temperature,
                "SleepHours": sleep_hours,
                "Mood": mood,
                "Appetite": appetite,
                "Symptoms": symptoms,
                "Notes": notes,
                "Username": st.session_state.get('username', ''),
                "Type": "health_track"
            }
            
            table.put_item(Item=entry_data)
            st.success("Health entry saved successfully!")