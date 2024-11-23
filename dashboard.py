# import streamlit as st
# import pywhatkit
# import datetime
# import json
# import re
# from datetime import timedelta




# def validate_phone_number(phone_number):
#     """Validate Indian phone number format."""
#     pattern = r'^\+91[6-9]\d{9}$'
#     return bool(re.match(pattern, phone_number))

# def schedule_whatsapp_notification(phone_number, message, scheduled_time):
#     """Schedule a WhatsApp notification."""
#     try:
#         hour = scheduled_time.hour
#         minute = scheduled_time.minute
        
#         if validate_phone_number(phone_number):
#             pywhatkit.sendwhatmsg(
#                 phone_number,
#                 message,
#                 hour,
#                 minute,
#                 wait_time=20,
#                 tab_close=True
#             )
#             return True
#         else:
#             st.error("Invalid phone number format")
#             return False
#     except Exception as e:
#         st.error(f"Error scheduling notification: {str(e)}")
#         return False

# def save_notification_settings(settings):
#     """Save notification preferences to session state."""
#     if 'notification_settings' not in st.session_state:
#         st.session_state.notification_settings = {}
#     st.session_state.notification_settings.update(settings)

# def show_dashboard(username):
#     st.title("👋 Welcome to KidsCare Pro")
    
#     # Notification Settings
#     with st.sidebar:
#         st.subheader("📱 Notification Settings")
#         phone_number = st.text_input(
#             "WhatsApp Number (with +91)",
#             value=st.session_state.get('phone_number', ''),
#             key=''
#         )
        
#         st.subheader("Enable Notifications For:")
#         notification_settings = {
#             'checkup_reminder': st.toggle('Checkup Reminders', value=True),
#             'vaccination_reminder': st.toggle('Vaccination Alerts', value=True),
#             'doctor_visit_reminder': st.toggle('Doctor Visit Reminders', value=True),
#             'growth_updates': st.toggle('Growth Measurement Updates', value=False)
#         }
        
#         if st.button("Save Notification Preferences"):
#             if phone_number:
#                 save_notification_settings({
#                     'phone_number': phone_number,
#                     **notification_settings
#                 })
#                 st.success("Notification preferences saved!")
#             else:
#                 st.error("Please enter a phone number")

#     # Dashboard Layout
#     col1, col2, col3 = st.columns(3)
    
#     # Last Check-up Card
#     with col1:
#         st.info("Last Check-up\n\n2 weeks ago")
#         if st.session_state.get('notification_settings', {}).get('checkup_reminder'):
#             if st.button("Schedule Next Checkup Reminder"):
#                 next_reminder = datetime.datetime.now() + timedelta(weeks=2)
#                 message = "🏥 Reminder: It's time for your child's regular checkup!"
#                 if schedule_whatsapp_notification(phone_number, message, next_reminder):
#                     st.success("Checkup reminder scheduled!")

#     # Vaccination Card
#     with col2:
#         st.success("Upcoming Vaccination\n\nMMR Booster")
#         if st.session_state.get('notification_settings', {}).get('vaccination_reminder'):
#             if st.button("Set Vaccination Reminder"):
#                 next_reminder = datetime.datetime.now() + timedelta(days=1)
#                 message = "💉 Reminder: MMR Booster vaccination is due tomorrow!"
#                 if schedule_whatsapp_notification(phone_number, message, next_reminder):
#                     st.success("Vaccination reminder scheduled!")

#     # Doctor Visit Card
#     with col3:
#         st.warning("Next Doctor Visit\n\nIn 3 days")
#         if st.session_state.get('notification_settings', {}).get('doctor_visit_reminder'):
#             if st.button("Set Visit Reminder"):
#                 next_reminder = datetime.datetime.now() + timedelta(days=2)
#                 message = "👨‍⚕️ Reminder: Doctor's appointment tomorrow!"
#                 if schedule_whatsapp_notification(phone_number, message, next_reminder):
#                     st.success("Doctor visit reminder scheduled!")

#     # Recent Activity Timeline
#     st.subheader("Recent Activity")
#     activities = [
#         {"date": "2024-03-20", "event": "Height measurement updated"},
#         {"date": "2024-03-18", "event": "Completed vaccination"},
#         {"date": "2024-03-15", "event": "Doctor's appointment"},
#     ]

#     # Display activities with notification options
#     for activity in activities:
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             st.markdown(f"**{activity['date']}**: {activity['event']}")
#         with col2:
#             if activity['event'].startswith("Height") and st.session_state.get('notification_settings', {}).get('growth_updates'):
#                 if st.button("Share Update", key=f"share_{activity['date']}"):
#                     message = f"📊 Growth Update: New height measurement recorded on {activity['date']}"
#                     if schedule_whatsapp_notification(phone_number, message, datetime.datetime.now() + timedelta(minutes=2)):
#                         st.success("Update will be shared!")

# if __name__ == "__main__":
#     show_dashboard()


# import streamlit as st
# import pywhatkit
# import datetime
# import json
# import re
# from datetime import timedelta, time

# def validate_phone_number(phone_number):
#     """Validate Indian phone number format."""
#     pattern = r'^\+91[6-9]\d{9}$'
#     return bool(re.match(pattern, phone_number))

# def schedule_whatsapp_notification(sender_phone, recipient_phone, message, scheduled_time):
#     """Schedule a WhatsApp notification."""
#     try:
#         hour = scheduled_time.hour
#         minute = scheduled_time.minute
        
#         # Validate both phone numbers
#         if not validate_phone_number(sender_phone):
#             st.error("Invalid sender phone number format")
#             return False
#         if not validate_phone_number(recipient_phone):
#             st.error("Invalid recipient phone number format")
#             return False
            
#         # Configure PyWhatKit with sender's phone
#         pywhatkit.phone_config(sender_phone)
        
#         # Send message
#         pywhatkit.sendwhatmsg(
#             recipient_phone,
#             message,
#             hour,
#             minute,
#             wait_time=20,
#             tab_close=True
#         )
#         return True
#     except Exception as e:
#         st.error(f"Error scheduling notification: {str(e)}")
#         return False

# def save_notification_settings(settings):
#     """Save notification preferences to session state."""
#     if 'notification_settings' not in st.session_state:
#         st.session_state.notification_settings = {}
#     st.session_state.notification_settings.update(settings)

# def show_dashboard(username):
#     st.title("👋 Welcome to KidsCare Pro")
    
#     # Notification Settings
#     with st.sidebar:
#         st.subheader("📱 Phone Configuration")
        
#         # Phone Numbers Configuration Section
#         with st.expander("Phone Numbers", expanded=True):
#             sender_phone = st.text_input(
#                 "Your WhatsApp Number (with +91)",
#                 value=st.session_state.get('sender_phone', ''),
#                 key='sender_phone_input',
#                 help="This is the phone number you'll use to send notifications from"
#             )
            
#             recipient_phone = st.text_input(
#                 "Recipient's WhatsApp Number (with +91)",
#                 value=st.session_state.get('recipient_phone', ''),
#                 key='recipient_phone_input',
#                 help="This is the phone number that will receive notifications"
#             )
            
#             # Validate phone numbers as they're entered
#             if sender_phone and not validate_phone_number(sender_phone):
#                 st.error("Invalid sender phone number format. Use +91 followed by 10 digits")
#             if recipient_phone and not validate_phone_number(recipient_phone):
#                 st.error("Invalid recipient phone number format. Use +91 followed by 10 digits")
        
#         st.subheader("Configure Notifications:")
        
#         # Create expandable sections for each notification type
#         with st.expander("Checkup Reminders"):
#             checkup_enabled = st.toggle('Enable', value=True)
#             checkup_time = st.time_input(
#                 "Preferred reminder time",
#                 value=datetime.time(9, 0),
#                 key='checkup_time'
#             )
#             checkup_days_before = st.number_input(
#                 "Days before checkup to send reminder",
#                 min_value=1,
#                 max_value=7,
#                 value=2,
#                 key='checkup_days'
#             )

#         with st.expander("Vaccination Alerts"):
#             vaccination_enabled = st.toggle('Enable', value=True)
#             vaccination_time = st.time_input(
#                 "Preferred reminder time",
#                 value=datetime.time(10, 0),
#                 key='vaccination_time'
#             )
#             vaccination_days_before = st.number_input(
#                 "Days before vaccination to send reminder",
#                 min_value=1,
#                 max_value=7,
#                 value=2,
#                 key='vaccination_days'
#             )

#         with st.expander("Doctor Visit Reminders"):
#             doctor_visit_enabled = st.toggle('Enable', value=True)
#             doctor_visit_time = st.time_input(
#                 "Preferred reminder time",
#                 value=datetime.time(11, 0),
#                 key='doctor_visit_time'
#             )
#             doctor_visit_days_before = st.number_input(
#                 "Days before visit to send reminder",
#                 min_value=1,
#                 max_value=7,
#                 value=1,
#                 key='doctor_visit_days'
#             )

#         with st.expander("Growth Measurement Updates"):
#             growth_enabled = st.toggle('Enable', value=False)
#             growth_time = st.time_input(
#                 "Preferred update time",
#                 value=datetime.time(17, 0),
#                 key='growth_time'
#             )
        
#         notification_settings = {
#             'sender_phone': sender_phone,
#             'recipient_phone': recipient_phone,
#             'checkup_reminder': {
#                 'enabled': checkup_enabled,
#                 'time': checkup_time,
#                 'days_before': checkup_days_before
#             },
#             'vaccination_reminder': {
#                 'enabled': vaccination_enabled,
#                 'time': vaccination_time,
#                 'days_before': vaccination_days_before
#             },
#             'doctor_visit_reminder': {
#                 'enabled': doctor_visit_enabled,
#                 'time': doctor_visit_time,
#                 'days_before': doctor_visit_days_before
#             },
#             'growth_updates': {
#                 'enabled': growth_enabled,
#                 'time': growth_time
#             }
#         }
        
#         if st.button("Save Notification Preferences"):
#             if sender_phone and recipient_phone:
#                 if validate_phone_number(sender_phone) and validate_phone_number(recipient_phone):
#                     save_notification_settings(notification_settings)
#                     st.success("Notification preferences saved!")
#                 else:
#                     st.error("Please check phone number formats")
#             else:
#                 st.error("Please enter both sender and recipient phone numbers")

#     # Dashboard Layout
#     col1, col2, col3 = st.columns(3)
    
#     # Last Check-up Card
#     with col1:
#         st.info("Last Check-up\n\n2 weeks ago")
#         if st.session_state.get('notification_settings', {}).get('checkup_reminder', {}).get('enabled', False):
#             if st.button("Schedule Next Checkup Reminder"):
#                 settings = st.session_state.notification_settings['checkup_reminder']
#                 sender = st.session_state.notification_settings.get('sender_phone')
#                 recipient = st.session_state.notification_settings.get('recipient_phone')
#                 next_date = datetime.datetime.now() + timedelta(weeks=2)
#                 reminder_date = next_date - timedelta(days=settings['days_before'])
#                 reminder_datetime = datetime.datetime.combine(reminder_date.date(), settings['time'])
#                 message = "🏥 Reminder: It's time for your child's regular checkup!"
#                 if schedule_whatsapp_notification(sender, recipient, message, reminder_datetime):
#                     st.success(f"Checkup reminder scheduled for {reminder_datetime.strftime('%Y-%m-%d %H:%M')}")

#     # Vaccination Card
#     with col2:
#         st.success("Upcoming Vaccination\n\nMMR Booster")
#         if st.session_state.get('notification_settings', {}).get('vaccination_reminder', {}).get('enabled', False):
#             if st.button("Set Vaccination Reminder"):
#                 settings = st.session_state.notification_settings['vaccination_reminder']
#                 sender = st.session_state.notification_settings.get('sender_phone')
#                 recipient = st.session_state.notification_settings.get('recipient_phone')
#                 next_date = datetime.datetime.now() + timedelta(days=7)  # Example: vaccination in 7 days
#                 reminder_date = next_date - timedelta(days=settings['days_before'])
#                 reminder_datetime = datetime.datetime.combine(reminder_date.date(), settings['time'])
#                 message = "💉 Reminder: MMR Booster vaccination is due soon!"
#                 if schedule_whatsapp_notification(sender, recipient, message, reminder_datetime):
#                     st.success(f"Vaccination reminder scheduled for {reminder_datetime.strftime('%Y-%m-%d %H:%M')}")

#     # Doctor Visit Card
#     with col3:
#         st.warning("Next Doctor Visit\n\nIn 3 days")
#         if st.session_state.get('notification_settings', {}).get('doctor_visit_reminder', {}).get('enabled', False):
#             if st.button("Set Visit Reminder"):
#                 settings = st.session_state.notification_settings['doctor_visit_reminder']
#                 sender = st.session_state.notification_settings.get('sender_phone')
#                 recipient = st.session_state.notification_settings.get('recipient_phone')
#                 next_date = datetime.datetime.now() + timedelta(days=3)
#                 reminder_date = next_date - timedelta(days=settings['days_before'])
#                 reminder_datetime = datetime.datetime.combine(reminder_date.date(), settings['time'])
#                 message = "👨‍⚕️ Reminder: Doctor's appointment coming up!"
#                 if schedule_whatsapp_notification(sender, recipient, message, reminder_datetime):
#                     st.success(f"Doctor visit reminder scheduled for {reminder_datetime.strftime('%Y-%m-%d %H:%M')}")

#     # Recent Activity Timeline
#     st.subheader("Recent Activity")
#     activities = [
#         {"date": "2024-03-20", "event": "Height measurement updated"},
#         {"date": "2024-03-18", "event": "Completed vaccination"},
#         {"date": "2024-03-15", "event": "Doctor's appointment"},
#     ]

#     # Display activities with notification options
#     for activity in activities:
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             st.markdown(f"**{activity['date']}**: {activity['event']}")
#         with col2:
#             if (activity['event'].startswith("Height") and 
#                 st.session_state.get('notification_settings', {}).get('growth_updates', {}).get('enabled', False)):
#                 if st.button("Share Update", key=f"share_{activity['date']}"):
#                     settings = st.session_state.notification_settings['growth_updates']
#                     sender = st.session_state.notification_settings.get('sender_phone')
#                     recipient = st.session_state.notification_settings.get('recipient_phone')
#                     reminder_datetime = datetime.datetime.combine(
#                         datetime.datetime.now().date(),
#                         settings['time']
#                     )
#                     message = f"📊 Growth Update: New height measurement recorded on {activity['date']}"
#                     if schedule_whatsapp_notification(sender, recipient, message, reminder_datetime):
#                         st.success(f"Update will be shared at {reminder_datetime.strftime('%H:%M')}")

# if __name__ == "__main__":
#     show_dashboard('username')




import streamlit as st
import pywhatkit
import datetime
import json
import re
from datetime import timedelta, time

def validate_phone_number(phone_number):
    """Validate Indian phone number format."""
    pattern = r'^\+91[6-9]\d{9}$'
    return bool(re.match(pattern, phone_number))

def schedule_whatsapp_notification(sender_phone, recipient_phone, message, scheduled_date, scheduled_time):
    """Schedule a WhatsApp notification."""
    try:
        # Combine date and time
        scheduled_datetime = datetime.datetime.combine(scheduled_date, scheduled_time)
        
        # Check if scheduled time is in the past
        if scheduled_datetime <= datetime.datetime.now():
            st.error("Cannot schedule notifications in the past")
            return False
        
        # Validate both phone numbers
        if not validate_phone_number(sender_phone):
            st.error("Invalid sender phone number format")
            return False
        if not validate_phone_number(recipient_phone):
            st.error("Invalid recipient phone number format")
            return False
            
        # Configure PyWhatKit with sender's phone
        
        
        # Send message
        pywhatkit.sendwhatmsg(
            recipient_phone,
            message,
            scheduled_time.hour,
            scheduled_time.minute,
            wait_time=20,
            tab_close=True
        )
        return True
    except Exception as e:
        st.error(f"Error scheduling notification: {str(e)}")
        return False

def save_notification_settings(settings):
    """Save notification preferences to session state."""
    if 'notification_settings' not in st.session_state:
        st.session_state.notification_settings = {}
    st.session_state.notification_settings.update(settings)

def show_notification_scheduler(sender_phone, recipient_phone, notification_type):
    """Show the notification scheduler UI for a given notification type."""
    col1, col2 = st.columns(2)
    
    with col1:
        scheduled_date = st.date_input(
            "Select Date",
            value=datetime.datetime.now().date() + timedelta(days=1),
            min_value=datetime.datetime.now().date(),
            key=f'date_{notification_type}'
        )
    
    with col2:
        scheduled_time = st.time_input(
            "Select Time",
            value=datetime.time(9, 0),
            key=f'time_{notification_type}'
        )
    
    custom_message = st.text_area(
        "Custom Message (optional)",
        key=f'message_{notification_type}'
    )
    
    return scheduled_date, scheduled_time, custom_message

def show_dashboard(username):
    st.title("👋 Welcome to KidsCare Pro")
    
    # Notification Settings
    with st.sidebar:
        st.subheader("📱 Phone Configuration")
        
        # Phone Numbers Configuration Section
        with st.expander("Phone Numbers", expanded=True):
            sender_phone = st.text_input(
                "Your WhatsApp Number (with +91)",
                value=st.session_state.get('sender_phone', ''),
                key='sender_phone_input',
                help="This is the phone number you'll use to send notifications from"
            )
            
            recipient_phone = st.text_input(
                "Recipient's WhatsApp Number (with +91)",
                value=st.session_state.get('recipient_phone', ''),
                key='recipient_phone_input',
                help="This is the phone number that will receive notifications"
            )
            
            # Validate phone numbers as they're entered
            if sender_phone and not validate_phone_number(sender_phone):
                st.error("Invalid sender phone number format. Use +91 followed by 10 digits")
            if recipient_phone and not validate_phone_number(recipient_phone):
                st.error("Invalid recipient phone number format. Use +91 followed by 10 digits")

    # Dashboard Layout
    col1, col2, col3 = st.columns(3)
    
    # Last Check-up Card
    with col1:
        st.info("Last Check-up\n\n2 weeks ago")
        with st.expander("Schedule Checkup Reminder"):
            scheduled_date, scheduled_time, custom_message = show_notification_scheduler(
                sender_phone, recipient_phone, "checkup"
            )
            default_message = "🏥 Reminder: It's time for your child's regular checkup!"
            message = custom_message if custom_message else default_message
            
            if st.button("Schedule Checkup Reminder"):
                if schedule_whatsapp_notification(
                    sender_phone, 
                    recipient_phone, 
                    message, 
                    scheduled_date, 
                    scheduled_time
                ):
                    st.success(f"Checkup reminder scheduled for {scheduled_date} at {scheduled_time}")

    # Vaccination Card
    with col2:
        st.success("Upcoming Vaccination\n\nMMR Booster")
        with st.expander("Schedule Vaccination Reminder"):
            scheduled_date, scheduled_time, custom_message = show_notification_scheduler(
                sender_phone, recipient_phone, "vaccination"
            )
            default_message = "💉 Reminder: MMR Booster vaccination is due!"
            message = custom_message if custom_message else default_message
            
            if st.button("Schedule Vaccination Reminder"):
                if schedule_whatsapp_notification(
                    sender_phone, 
                    recipient_phone, 
                    message, 
                    scheduled_date, 
                    scheduled_time
                ):
                    st.success(f"Vaccination reminder scheduled for {scheduled_date} at {scheduled_time}")

    # Doctor Visit Card
    with col3:
        st.warning("Next Doctor Visit\n\nIn 3 days")
        with st.expander("Schedule Visit Reminder"):
            scheduled_date, scheduled_time, custom_message = show_notification_scheduler(
                sender_phone, recipient_phone, "doctor_visit"
            )
            default_message = "👨‍⚕️ Reminder: Doctor's appointment!"
            message = custom_message if custom_message else default_message
            
            if st.button("Schedule Visit Reminder"):
                if schedule_whatsapp_notification(
                    sender_phone, 
                    recipient_phone, 
                    message, 
                    scheduled_date, 
                    scheduled_time
                ):
                    st.success(f"Doctor visit reminder scheduled for {scheduled_date} at {scheduled_time}")

    # Recent Activity Timeline
    st.subheader("Recent Activity")
    activities = [
        {"date": "2024-03-20", "event": "Height measurement updated"},
        {"date": "2024-03-18", "event": "Completed vaccination"},
        {"date": "2024-03-15", "event": "Doctor's appointment"},
    ]

    # Display activities with notification options
    for activity in activities:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{activity['date']}**: {activity['event']}")
        with col2:
            if activity['event'].startswith("Height"):
                with st.expander("Share Update"):
                    scheduled_date, scheduled_time, custom_message = show_notification_scheduler(
                        sender_phone, recipient_phone, f"growth_{activity['date']}"
                    )
                    default_message = f"📊 Growth Update: New height measurement recorded on {activity['date']}"
                    message = custom_message if custom_message else default_message
                    
                    if st.button("Share Update", key=f"share_{activity['date']}"):
                        if schedule_whatsapp_notification(
                            sender_phone, 
                            recipient_phone, 
                            message, 
                            scheduled_date, 
                            scheduled_time
                        ):
                            st.success(f"Update will be shared on {scheduled_date} at {scheduled_time}")

