import streamlit as st

# -----------------------------------------------------
# PAGE CONFIGURATION (MUST BE FIRST STREAMLIT COMMAND)
# -----------------------------------------------------

st.set_page_config(
    page_title="PATHFINDER AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# IMPORTS
# -----------------------------------------------------

from streamlit_option_menu import option_menu

# Components
from components.goal_form import goal_form
from components.dashboard import dashboard_section
from components.future_simulator import future_simulator
from components.roadmap import roadmap_section
from components.graphs import probability_graphs
from components.suggestions import suggestions_section

# Styling
from styles import load_css


# -----------------------------------------------------
# LOAD CSS
# -----------------------------------------------------

load_css()


# -----------------------------------------------------
# SESSION STATES
# -----------------------------------------------------

if "user_data" not in st.session_state:
    st.session_state["user_data"] = {}

if "ai_result" not in st.session_state:
    st.session_state["ai_result"] = None

if "analysis" not in st.session_state:
    st.session_state["analysis"] = {}

if "roadmap" not in st.session_state:
    st.session_state["roadmap"] = {}

if "predictions" not in st.session_state:
    st.session_state["predictions"] = []


# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------

with st.sidebar:

    st.title("🚀 PATHFINDER AI")

    st.markdown(
        """
        ### Predict • Plan • Progress

        Your AI-powered Decision Intelligence Platform.
        """
    )

    selected = option_menu(

        menu_title="Navigation",

        options=[

            "Dashboard",
            "Goal Analysis",
            "Future Simulator",
            "Roadmap",
            "AI Decision Engine",
            "About"

        ],

        icons=[

            "speedometer2",
            "bullseye",
            "diagram-3",
            "calendar-week",
            "robot",
            "info-circle"

        ],

        default_index=0

    )


# -----------------------------------------------------
# HERO SECTION
# -----------------------------------------------------

st.markdown(
    """
    <h1 style='text-align:center;'>
    PATHFINDER AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center;color:grey;'>
    Google Maps For Your Future
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()


# -----------------------------------------------------
# DASHBOARD
# -----------------------------------------------------

if selected == "Dashboard":

    dashboard_section()


# -----------------------------------------------------
# GOAL ANALYSIS
# -----------------------------------------------------

elif selected == "Goal Analysis":

    st.subheader("🎯 Goal Analysis")

    st.write(
        """
        Enter your academic profile, goals,
        achievements and interests.

        PATHFINDER AI will generate
        personalized future trajectories,
        success probabilities and adaptive
        roadmaps based on your inputs.
        """
    )

    goal_form()


# -----------------------------------------------------
# FUTURE SIMULATOR
# -----------------------------------------------------

elif selected == "Future Simulator":

    st.subheader("🔮 Future Simulator")

    future_simulator()

    st.divider()

    probability_graphs()


# -----------------------------------------------------
# ROADMAP
# -----------------------------------------------------

elif selected == "Roadmap":

    st.subheader("🗺️ Personalized Roadmap")

    roadmap_section()


# -----------------------------------------------------
# AI DECISION ENGINE
# -----------------------------------------------------

elif selected == "AI Decision Engine":

    st.subheader("🧠 AI Decision Intelligence Engine")

    st.write(
        """
        PATHFINDER AI performs What-if Analysis
        to predict how your future changes when
        different decisions are made.
        """
    )

    suggestions_section()


# -----------------------------------------------------
# ABOUT PAGE
# -----------------------------------------------------

elif selected == "About":

    st.subheader("About PATHFINDER AI")

    st.info(
        """
        PATHFINDER AI is an AI-powered
        Decision Intelligence Platform
        designed for students.

        It predicts multiple future trajectories,
        estimates success probabilities and
        generates personalized roadmaps that
        continuously evolve with user progress.
        """
    )

    st.divider()

    st.markdown(
        """
        ### Core Features

        - Predict Multiple Future Paths
        - Success Probability Estimation
        - Adaptive Roadmap Generation
        - Future Simulations
        - What-if Analysis
        - AI Decision Intelligence
        - Personalized Recommendations
        - Opportunity Analysis
        """
    )

    st.divider()

    st.markdown(
        """
        ### AI Workflow

        ```
        User Profile
                ↓
          Goal Analysis
                ↓
            OpenAI API
                ↓
        Decision Intelligence
                ↓
         Future Predictions
                ↓
        Success Probabilities
                ↓
          Adaptive Roadmaps
                ↓
           What-if Analysis
                ↓
         Personalized Guidance
                ↓
                 User
        ```
        """
    )


# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.divider()

st.markdown(
    """
    <div style='text-align:center;color:grey;'>

    <h4>PATHFINDER AI</h4>

    Predict • Plan • Progress

    <br>

    AI-powered Decision Intelligence Platform

    </div>
    """,
    unsafe_allow_html=True
)