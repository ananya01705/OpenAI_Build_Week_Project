import streamlit as st


# --------------------------------------------------
# ROADMAP DATA
# --------------------------------------------------


def get_roadmap():

    """
    Dummy roadmap for MVP.

    Later this will be generated
    dynamically using OpenAI.
    """

    roadmap = {

        "30 Days":[

            "Learn Python Fundamentals",
            "Complete Git & GitHub Basics",
            "Solve 25 Coding Problems",
            "Create a LinkedIn Profile"

        ],


        "60 Days":[

            "Learn SQL",
            "Build One Mini Project",
            "Participate in One Hackathon",
            "Improve Problem Solving"

        ],


        "90 Days":[

            "Build Two Portfolio Projects",
            "Learn APIs and FastAPI",
            "Upload Projects to GitHub",
            "Begin Internship Preparation"

        ],


        "6 Months":[

            "Master Data Structures",
            "Participate in Multiple Hackathons",
            "Build Industry-Level Projects",
            "Create Your Portfolio Website"

        ],


        "1 Year":[

            "Become Internship Ready",
            "Prepare for Placements",
            "Build an Impressive Resume",
            "Become Career Ready"

        ]

    }


    return roadmap




# --------------------------------------------------
# PROGRESS SCORE
# --------------------------------------------------


def progress_tracker():

    st.subheader(

        "Career Growth Tracker"

    )


    st.progress(0.91)

    st.write(

        "Predicted Career Growth : 91%"

    )



# --------------------------------------------------
# ROADMAP CARD
# --------------------------------------------------


def roadmap_card(title, items):

    with st.expander(title):

        for item in items:

            st.write(

                f"• {item}"

            )



# --------------------------------------------------
# AI MILESTONES
# --------------------------------------------------


def milestone_section():

    st.subheader(

        "AI Suggested Milestones"

    )


    col1, col2 = st.columns(2)


    with col1:

        st.success(

            """
            Skill Milestone

            Complete 3 projects
            within 90 days.
            """

        )


        st.info(

            """
            Career Milestone

            Participate in
            at least 3 hackathons.
            """

        )


    with col2:


        st.success(

            """
            Internship Milestone

            Become internship
            ready within 6 months.
            """

        )


        st.info(

            """
            Future Milestone

            Increase your success
            probability to 95%.
            """

        )



# --------------------------------------------------
# FUTURE TIMELINE
# --------------------------------------------------


def future_timeline():

    st.subheader(

        "Future Success Timeline"

    )


    st.markdown(

        """
        ```
                 TODAY
                    |
                    |
              Learn Skills
                    |
                    |
                Projects
                    |
                    |
               Hackathons
                    |
                    |
               Internships
                    |
                    |
              Career Growth
                    |
                    |
               Placement Ready
                    |
                    |
                  SUCCESS
        ```
        """

    )




# --------------------------------------------------
# ROADMAP SECTION
# --------------------------------------------------


def roadmap_section():

    st.title(

        "🗺️ Personalized Roadmap"

    )


    st.write(

        "PATHFINDER AI creates "
        "personalized timelines to "
        "maximize your future success."

    )


    st.divider()


    progress_tracker()


    st.divider()


    roadmap = get_roadmap()


    st.subheader(

        "Your Success Roadmap"

    )


    roadmap_card(

        "30 Days",

        roadmap["30 Days"]

    )


    roadmap_card(

        "60 Days",

        roadmap["60 Days"]

    )


    roadmap_card(

        "90 Days",

        roadmap["90 Days"]

    )


    roadmap_card(

        "6 Months",

        roadmap["6 Months"]

    )


    roadmap_card(

        "1 Year",

        roadmap["1 Year"]

    )


    st.divider()


    milestone_section()


    st.divider()


    future_timeline()


    st.divider()


    st.info(

        """
        PATHFINDER AI predicts that
        consistently completing these
        milestones significantly improves:

        • Success Probability

        • Internship Readiness

        • Career Growth

        • Skill Development

        • Future Opportunities
        """

    )