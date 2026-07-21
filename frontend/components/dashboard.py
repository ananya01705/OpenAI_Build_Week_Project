import streamlit as st


# --------------------------------------------------
# SCORE CALCULATIONS
# --------------------------------------------------

def calculate_scores():

    # Get user data safely
    data = st.session_state.get("user_data", {})

    # If user hasn't filled Goal Analysis
    if not data:

        return {

            "success": 0,
            "career": 0,
            "skills": 0,
            "internship": 0,
            "future": 0

        }

    # Safe retrievals

    cgpa = data.get("cgpa", 0)
    projects = data.get("projects", 0)
    internships = data.get("internships", 0)
    hackathons = data.get("hackathons", 0)
    skills = data.get("skills", [])

    # --------------------------------------------------
    # SCORE CALCULATIONS
    # --------------------------------------------------

    success_score = min(

        int(

            (cgpa * 6)
            + (projects * 3)
            + (internships * 7)
            + (hackathons * 2)

        ),

        100

    )


    career_score = min(

        int(

            (cgpa * 7)
            + (projects * 2)

        ),

        100

    )


    skill_score = min(

        int(

            len(skills) * 8

        ),

        100

    )


    internship_score = min(

        int(

            (projects * 10)
            + (internships * 20)
            + (hackathons * 4)

        ),

        100

    )


    future_score = min(

        int(

            (

                success_score +
                career_score +
                skill_score

            ) / 3

        ),

        100

    )


    return {

        "success": success_score,
        "career": career_score,
        "skills": skill_score,
        "internship": internship_score,
        "future": future_score

    }


# --------------------------------------------------
# PROGRESS BAR
# --------------------------------------------------

def score_progress(title, value):

    st.write(f"**{title}**")

    st.progress(value / 100)

    st.write(f"{value}%")



# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

def dashboard_section():

    st.title("📊 AI Decision Dashboard")

    st.write(

        "PATHFINDER AI evaluates your profile "
        "and predicts your future readiness."

    )

    st.divider()

    # ---------------------------------------------

    # Check whether Goal Analysis is completed

    if not st.session_state.get("user_data", {}):

        st.warning(

            """
            Please complete the Goal Analysis section first.

            Once completed, PATHFINDER AI will generate:

            • Success Probability Scores

            • Future Simulations

            • Personalized Roadmaps

            • AI Recommendations

            • Decision Intelligence Analysis
            """

        )

        return


    # ---------------------------------------------

    scores = calculate_scores()


    # ---------------------------------------------
    # METRIC CARDS
    # ---------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Success Score",
            f"{scores['success']}%"

        )


    with col2:

        st.metric(

            "Career Readiness",
            f"{scores['career']}%"

        )


    with col3:

        st.metric(

            "Future Stability",
            f"{scores['future']}%"

        )


    col4, col5 = st.columns(2)


    with col4:

        st.metric(

            "Skill Strength",
            f"{scores['skills']}%"

        )


    with col5:

        st.metric(

            "Internship Readiness",
            f"{scores['internship']}%"

        )


    st.divider()


    # ---------------------------------------------
    # AI READINESS ANALYSIS
    # ---------------------------------------------

    st.subheader("AI Readiness Analysis")


    score_progress(

        "Success Probability",

        scores["success"]

    )


    score_progress(

        "Career Readiness",

        scores["career"]

    )


    score_progress(

        "Skill Strength",

        scores["skills"]

    )


    score_progress(

        "Internship Readiness",

        scores["internship"]

    )


    score_progress(

        "Future Stability",

        scores["future"]

    )


    st.divider()


    # ---------------------------------------------
    # AI INSIGHTS
    # ---------------------------------------------

    st.subheader("AI Insights")


    if scores["success"] >= 85:

        st.success(

            """
            Excellent progress!

            You are on track to achieve
            your goals if you continue
            improving consistently.
            """

        )


    elif scores["success"] >= 70:

        st.warning(

            """
            Good foundation!

            Improving your projects,
            skills and practical experience
            will significantly increase
            your success probability.
            """

        )


    else:

        st.error(

            """
            PATHFINDER AI recommends
            focusing on:

            • Skill Development

            • Building Projects

            • Participating in Hackathons

            • Applying for Internships
            """

        )


    st.divider()


    # ---------------------------------------------
    # PROFILE SUMMARY
    # ---------------------------------------------

    st.subheader("Profile Summary")


    data = st.session_state.get("user_data", {})


    st.write(

        f"**Goal :** {data.get('goal','Not Provided')}"

    )


    st.write(

        f"**Timeline :** {data.get('timeline','Not Provided')}"

    )


    st.write(

        f"**Current CGPA :** {data.get('cgpa',0)}"

    )


    st.write(

        f"**Projects Completed :** {data.get('projects',0)}"

    )


    st.write(

        f"**Hackathons :** {data.get('hackathons',0)}"

    )


    st.write(

        f"**Internships :** {data.get('internships',0)}"

    )


    st.write(

        f"**Skills Added :** {len(data.get('skills',[]))}"

    )