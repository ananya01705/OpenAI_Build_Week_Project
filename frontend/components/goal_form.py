import streamlit as st
import time


# --------------------------------------------------
# GOAL ANALYSIS FORM
# --------------------------------------------------

def goal_form():

    st.title("🎯 Goal Analysis")

    st.write(
        """
        Tell PATHFINDER AI about yourself.

        Our AI Decision Intelligence Engine will
        analyze your profile and predict multiple
        future trajectories based on your goals,
        skills and achievements.
        """
    )

    st.divider()

    # --------------------------------------------------
    # BASIC DETAILS
    # --------------------------------------------------

    name = st.text_input("Your Name")

    year = st.selectbox(

        "Current Academic Year",

        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]

    )


    cgpa = st.slider(

        "Current CGPA",

        0.0,
        10.0,
        8.0,
        0.1

    )


    # --------------------------------------------------
    # CAREER GOALS
    # --------------------------------------------------

    goal = st.selectbox(

        "Select Your Primary Goal",

        [

            "AI Engineer",
            "Data Scientist",
            "Software Developer",
            "Research",
            "Higher Studies",
            "Startup Founder",
            "Placement Preparation",
            "Product Manager",
            "Cyber Security",
            "Cloud Engineer"

        ]

    )


    # --------------------------------------------------
    # TIMELINE
    # --------------------------------------------------

    timeline = st.selectbox(

        "Target Timeline",

        [

            "6 Months",
            "1 Year",
            "2 Years",
            "3 Years"

        ]

    )


    # --------------------------------------------------
    # SKILLS
    # --------------------------------------------------

    skills = st.multiselect(

        "Select Your Current Skills",

        [

            "Python",
            "C",
            "C++",
            "Java",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Git & Github",
            "Data Structures",
            "Web Development",
            "Cloud Computing",
            "Docker",
            "FastAPI",
            "Streamlit",
            "React",
            "Prompt Engineering",
            "UI/UX",
            "Public Speaking",
            "Leadership"

        ]

    )


    # --------------------------------------------------
    # INTERESTS
    # --------------------------------------------------

    interests = st.multiselect(

        "Areas of Interest",

        [

            "Artificial Intelligence",
            "Data Science",
            "Hackathons",
            "Competitive Programming",
            "Research",
            "Startups",
            "Open Source",
            "App Development",
            "Cyber Security",
            "Blockchain",
            "Cloud Computing",
            "Robotics",
            "Space Technology",
            "Entrepreneurship"

        ]

    )


    # --------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------

    projects = st.slider(

        "Projects Completed",

        0,
        20,
        2

    )


    internships = st.slider(

        "Internships Completed",

        0,
        10,
        0

    )


    hackathons = st.slider(

        "Hackathons Participated",

        0,
        20,
        0

    )


    # --------------------------------------------------
    # DESCRIPTION
    # --------------------------------------------------

    description = st.text_area(

        "Tell us about your Dream Career",

        placeholder="""
Example:

I want to become an AI Engineer within
one year. I am interested in Data Science,
Hackathons and Research and wish to
improve my internship opportunities.
"""

    )


    st.divider()


    # --------------------------------------------------
    # GENERATE BUTTON
    # --------------------------------------------------

    generate = st.button(

        "🚀 Generate Future Prediction"

    )


    # --------------------------------------------------
    # GENERATE ANALYSIS
    # --------------------------------------------------

    if generate:


        # Basic Validation

        if name.strip() == "":

            st.error(

                "Please enter your name."

            )

            return


        if len(skills) == 0:

            st.warning(

                "Adding skills improves the "
                "accuracy of future predictions."

            )


        # Store User Data

        user_data = {

            "name": name,
            "year": year,
            "cgpa": cgpa,
            "goal": goal,
            "timeline": timeline,
            "skills": skills,
            "interests": interests,
            "projects": projects,
            "internships": internships,
            "hackathons": hackathons,
            "description": description

        }


        st.session_state["user_data"] = user_data


        # ------------------------------------------
        # FUTURE OPENAI INTEGRATION
        # ------------------------------------------

        with st.spinner(

            "PATHFINDER AI is analyzing your profile..."

        ):

            time.sleep(2)


        # Placeholder for OpenAI output

        st.session_state["ai_result"] = {

            "status": "READY"

        }


        # ------------------------------------------
        # SUCCESS MESSAGE
        # ------------------------------------------

        st.success(

            """
            Profile analysis completed successfully!

            Dashboard unlocked.
            Future Simulator unlocked.
            Roadmap unlocked.
            AI Decision Engine unlocked.
            """

        )


        st.balloons()


        # ------------------------------------------
        # PROFILE SUMMARY
        # ------------------------------------------

        st.subheader("Generated Profile")

        st.write(

            f"**Name :** {name}"

        )

        st.write(

            f"**Goal :** {goal}"

        )

        st.write(

            f"**Timeline :** {timeline}"

        )

        st.write(

            f"**CGPA :** {cgpa}"

        )

        st.write(

            f"**Projects :** {projects}"

        )

        st.write(

            f"**Internships :** {internships}"

        )

        st.write(

            f"**Hackathons :** {hackathons}"

        )

        st.write(

            f"**Skills Added :** {len(skills)}"

        )


        st.info(

            """
            PATHFINDER AI has successfully
            generated your profile.

            Proceed to:

            • Dashboard

            • Future Simulator

            • Roadmap

            • AI Decision Engine

            to explore your predictions.
            """

        )