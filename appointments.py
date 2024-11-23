import streamlit as st
import uuid
from datetime import datetime, timedelta
import boto3

# Initialize AWS DynamoDB client
def initialize_aws_clients():
    session = boto3.Session(
        aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
        aws_secret_access_key=st.secrets["AWS_SECRET_KEY"],
        region_name=st.secrets["AWS_REGION"]
    )
    dynamodb = session.resource('dynamodb')
    return dynamodb

# Book Appointment Functionality
def book_appointment():
    st.header("Book Appointment")
    
    with st.form("appointment_form"):
        # Collect basic details
        st.subheader("Child Details")
        child_name = st.text_input("Child's Name", placeholder="Enter child's full name")
        child_age = st.number_input("Child's Age (in years)", min_value=0, max_value=18, step=1)
        parent_contact = st.text_input("Parent's Contact Number", placeholder="Enter a valid phone number")
        
        # Appointment details
        st.subheader("Appointment Details")
        appointment_date = st.date_input(
            "Select Appointment Date", 
            min_value=datetime.today().date(), 
            max_value=(datetime.today() + timedelta(days=30)).date()
        )
        appointment_time = st.time_input("Select Appointment Time")
        
        purpose = st.selectbox(
            "Purpose of Visit", 
            ["General Check-up", "Vaccination", "Follow-up", "Health Concern", "Other"]
        )
        
        additional_notes = st.text_area("Additional Notes (Optional)", placeholder="Enter any additional details")
        
        # Form submission
        if st.form_submit_button("Book Appointment"):
            # Validate the inputs
            if not child_name or not parent_contact:
                st.error("Please fill in all the required fields!")
                return
            
            # Generate unique appointment ID
            appointment_id = str(uuid.uuid4())
            
            # Prepare data
            appointment_data = {
                "AppointmentID": appointment_id,
                "ChildName": child_name,
                "ChildAge": child_age,
                "ParentContact": parent_contact,
                "AppointmentDate": str(appointment_date),
                "AppointmentTime": appointment_time.strftime("%H:%M"),
                "Purpose": purpose,
                "AdditionalNotes": additional_notes,
                "CreatedAt": str(datetime.now()),
            }
            
            # Save to DynamoDB
            try:
                dynamodb = initialize_aws_clients()
                table = dynamodb.Table(st.secrets["APPOINTMENTS_TABLE"])  # Replace with your table name
                table.put_item(Item=appointment_data)
                st.success("Appointment booked successfully!")
                st.info(f"Your appointment ID is: {appointment_id}. Please save it for reference.")
            except Exception as e:
                st.error(f"Error booking appointment: {e}")

# Main Streamlit App
if __name__ == "__main__":
    st.title("Child Pediatrician Application")
    
    # Navigation
    pages = ["Home", "Book Appointment", "Child Profile Management"]
    choice = st.sidebar.selectbox("Navigate", pages)
    
    if choice == "Home":
        st.write("Welcome to the Child Pediatrician App!")
    elif choice == "Book Appointment":
        book_appointment()
    elif choice == "Child Profile Management":
        manage_child_profile()

