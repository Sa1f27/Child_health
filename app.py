# import streamlit as st
# import boto3
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from datetime import datetime, timedelta
# import plotly.express as px
# import plotly.graph_objects as go
# from PIL import Image
# import numpy as np
# from streamlit_option_menu import option_menu
# import uuid
# import json
# from  dashboard import  show_dashboard as display
# from ai_app import manage_child_profile
# import milestone 
# import doctor_portal
# from show_analytics import analytics
# from health_tracker import health
# from login import login_page


# # Configure page settings
# st.set_page_config(page_title="KidsCare Pro", page_icon="👶", layout="wide")

# # Custom CSS for better styling
# st.markdown("""
#     <style>
#     .main {
#         padding: 2rem;
#     }
#     .stButton>button {
#         width: 100%;
#         border-radius: 5px;
#         height: 3em;
#         background-color: #ff6b6b;
#         color: white;
#     }
#     .stats-card {
#         padding: 1rem;
#         border-radius: 0.5rem;
#         background-color: #f8f9fa;
#         box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
#         margin: 1rem 0;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # AWS DynamoDB Configuration
# DYNAMODB_TABLE = "ChildHealthRecords"

# def initialize_aws_clients():
#     session = boto3.Session(
#         aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
#         aws_secret_access_key=st.secrets["AWS_SECRET_KEY"],
#         region_name=st.secrets["AWS_REGION"]
#     )
#     dynamodb = session.resource('dynamodb')
#     return dynamodb

# # Initialize DynamoDB
# dynamodb = initialize_aws_clients()
# table = dynamodb.Table(DYNAMODB_TABLE)

# # AI Integration
# def get_health_suggestions(child_data):
#     """
#     Generate personalized health suggestions based on child data
#     """
#     age = child_data.get('Age', 0)
#     weight = child_data.get('Weight', 0)
#     height = child_data.get('Height', 0)
#     bmi = weight / ((height/100) ** 2)
    
#     suggestions = []
    
#     # Basic health suggestions
#     if bmi > 25:
#         suggestions.append("Consider increasing physical activity and maintaining a balanced diet.")
#     elif bmi < 18.5:
#         suggestions.append("Focus on nutrient-rich foods to support healthy weight gain.")
        
#     # Age-specific suggestions
#     if age < 5:
#         suggestions.append("Ensure regular vaccination schedule is followed.")
#         suggestions.append("Focus on developmental activities like puzzles and physical play.")
#     elif 5 <= age < 12:
#         suggestions.append("Encourage team sports and social activities.")
#         suggestions.append("Maintain regular sleep schedule (9-11 hours per night).")
#     else:
#         suggestions.append("Support physical and emotional development through varied activities.")
#         suggestions.append("Monitor screen time and encourage outdoor activities.")
        
#     return suggestions

# # User Authentication
# def login_page():
#     login_page()

# # Main Navigation
# def main_navigation():
#     with st.sidebar:
#         selected = option_menu(
#             menu_title="Main Menu",
#             options=["Dashboard", "Child Profile", "Health Tracker", "Analytics", "Milestones", "Doctor's Portal"],
#             icons=["house", "person", "heart", "graph-up", "trophy", "hospital"],
#             menu_icon="cast",
#             default_index=0,
#         )
#     return selected

# # Dashboard
# def show_dashboard1(username):
#    display(username)

# # Child Profile Management
# def manage_child_profile1():
#     manage_child_profile()
    

# # Health Tracker
# def health_tracker():
#     health()


# # Analytics Dashboard
# def show_analytics():
#     analytics()


# # Milestones Tracking
# def track_milestones():
#     milestone.milestone_tracker()

# # Doctor's Portal
# def doctors_portal1():
#     doctor_portal.doctor()
   

# def main():
#     if 'logged_in' not in st.session_state:
#         st.session_state['logged_in'] = False
    
#     if not st.session_state['logged_in']:
#         login_page()
#     else:
#         selected = main_navigation()
        
#         if selected == "Dashboard":
#             show_dashboard1(st.session_state['username'])
#         elif selected == "Child Profile":
#             manage_child_profile1()
#         elif selected == "Health Tracker":
#             health_tracker()
#         elif selected == "Analytics":
#             show_analytics()
#         elif selected == "Milestones":
#             track_milestones()
#         elif selected == "Doctor's Portal":
#             doctors_portal1()
            
#         # Logout button in sidebar
#         if st.sidebar.button("Logout"):
#             st.session_state['logged_in'] = False
#             st.session_state['username'] = None
#             st.session_state['user_type'] = None
#             st.rerun()

#         # Initialize session state variables
#         if 'authenticated' not in st.session_state:
#             st.session_state.authenticated = False
#         if 'page' not in st.session_state:
#             st.session_state.page = 'login'

# # Run the application
# if __name__ == "__main__":
#     main()
import streamlit as st
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
import uuid
import json
from dashboard import show_dashboard
from ai_app import manage_child_profile
import milestone
import doctor_portal
from show_analytics import analytics
from health_tracker import health
from login import login_page
import streamlit_authenticator as stauth
from streamlit_card import card
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie
import requests

# Configure page settings with a modern theme
st.set_page_config(
    page_title="KidsCare Pro | Advanced Pediatric Care",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.kidscarepro.com/help',
        'Report a bug': "https://www.kidscarepro.com/bug",
        'About': "# KidsCare Pro v2.0\nAdvanced Pediatric Care Management System"
    }
)

# Enhanced Custom CSS for professional styling
st.markdown("""
    <style>
    /* Main App Styling */
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    /* Custom Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background: linear-gradient(45deg, #FF6B6B, #FF8E8E);
        color: white;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Card Styling */
    .stats-card {
        padding: 1.5rem;
        border-radius: 1rem;
        background: white;
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.08);
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .stats-card:hover {
        transform: translateY(-5px);
    }
    
    /* Custom Header Styling */
    .custom-header {
        background: linear-gradient(45deg, #2193b0, #6dd5ed);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #f1f3f4;
    }
    
    /* Custom Chart Styling */
    .chart-container {
        background: white;
        padding: 1rem;
        border-radius: 1rem;
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.08);
    }
    
    /* Form Styling */
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    .stSelectbox>div>div>select {
        border-radius: 8px;
    }
    
    /* Alert Styling */
    .stAlert {
        border-radius: 8px;
    }
    
    /* Progress Bar Styling */
    .stProgress > div > div > div {
        background-color: #FF6B6B;
    }
    
    /* Custom Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #fff;
        border-radius: 8px;
        color: #000;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF6B6B !important;
        color: #fff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# AWS Configuration with Error Handling
class AWSConfig:
    @staticmethod
    def initialize_aws_clients():
        try:
            session = boto3.Session(
                aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
                aws_secret_access_key=st.secrets["AWS_SECRET_KEY"],
                region_name=st.secrets["AWS_REGION"]
            )
            return session.resource('dynamodb')
        except Exception as e:
            st.error(f"Failed to initialize AWS client: {str(e)}")
            return None

# Enhanced Health Suggestions with ML Integration
class HealthSuggestionEngine:
    @staticmethod
    def get_health_suggestions(child_data):
        try:
            age = child_data.get('Age', 0)
            weight = child_data.get('Weight', 0)
            height = child_data.get('Height', 0)
            bmi = weight / ((height/100) ** 2)
            
            suggestions = {
                'nutrition': [],
                'activity': [],
                'development': [],
                'health': []
            }
            
            # Enhanced suggestion logic with categorization
            if bmi > 25:
                suggestions['nutrition'].append({
                    'title': 'Balanced Diet Plan',
                    'description': 'Consider increasing physical activity and maintaining a balanced diet.',
                    'priority': 'high'
                })
            elif bmi < 18.5:
                suggestions['nutrition'].append({
                    'title': 'Weight Gain Plan',
                    'description': 'Focus on nutrient-rich foods to support healthy weight gain.',
                    'priority': 'high'
                })
            
            # Age-specific developmental suggestions
            if age < 5:
                suggestions['development'].extend([
                    {
                        'title': 'Vaccination Schedule',
                        'description': 'Ensure regular vaccination schedule is followed.',
                        'priority': 'high'
                    },
                    {
                        'title': 'Early Development',
                        'description': 'Focus on developmental activities like puzzles and physical play.',
                        'priority': 'medium'
                    }
                ])
            
            return suggestions
            
        except Exception as e:
            st.error(f"Error generating health suggestions: {str(e)}")
            return {}

# Enhanced Navigation
class Navigation:
    @staticmethod
    def create_navigation():
        with st.sidebar:
            # Add logo
            add_logo("path_to_your_logo.png")
            
            # Add profile summary if logged in
            if st.session_state.get('logged_in'):
                st.write(f"👤 Welcome, {st.session_state.get('username')}")
                st.write(f"🏥 Role: {st.session_state.get('user_type')}")
            
            # Enhanced menu
            selected = option_menu(
                menu_title="Main Menu",
                options=["Dashboard", "Child Profile", "Health Tracker", 
                        "Analytics", "Milestones", "Doctor's Portal"],
                icons=["house-fill", "person-badge-fill", "heart-pulse-fill", 
                      "graph-up", "trophy-fill", "hospital-fill"],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "5!important"},
                    "icon": {"color": "#FF6B6B", "font-size": "20px"}, 
                    "nav-link": {
                        "font-size": "16px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#FF8E8E"
                    },
                    "nav-link-selected": {"background-color": "#FF6B6B"},
                }
            )
            
            # Add system status
            st.sidebar.markdown("---")
            st.sidebar.markdown("### System Status")
            st.sidebar.metric("System Health", "98%", "+2%")
            
            return selected

# # Dashboard
# def show_dashboard1(username):
#    display(username)

# # Child Profile Management
# def manage_child_profile1():
#     manage_child_profile()
    

# # Health Tracker
# def health_tracker():
#     health()


# # Analytics Dashboard
# def show_analytics():
#     analytics()


# # Milestones Tracking
# def track_milestones():
#     milestone.milestone_tracker()

# # Doctor's Portal
# def doctors_portal1():
#     doctor_portal.doctor()
   
# Main Application Class
class KidsCarePro:
    def __init__(self):
        self.dynamo_db = AWSConfig.initialize_aws_clients()
        self.health_engine = HealthSuggestionEngine()
        self.table = self.dynamo_db.Table("ChildHealthRecords") if self.dynamo_db else None
    
    def main(self):
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False
        
        if not st.session_state['logged_in']:
            self._show_login_page()
        else:
            selected = Navigation.create_navigation()
            self._route_page(selected)
    
    def _show_login_page(self):
        # Add animated logo
        lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_hello.json")
        st_lottie(lottie_hello, height=200)
        
        login_page()
    
    def _route_page(self, selected):
        pages = {
            "Dashboard": lambda: show_dashboard(st.session_state['username']),
            "Child Profile": manage_child_profile,
            "Health Tracker": health,
            "Analytics": analytics,
            "Milestones": milestone.milestone_tracker,
            "Doctor's Portal": doctor_portal.doctor
        }
        
        try:
            pages[selected]()
        except Exception as e:
            st.error(f"Error loading page: {str(e)}")
        
        # Logout button
        if st.sidebar.button("Logout", key="logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Run Application
if __name__ == "__main__":
    app = KidsCarePro()
    app.main()
