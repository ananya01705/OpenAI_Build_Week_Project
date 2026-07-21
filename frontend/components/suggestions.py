import streamlit as st


# ---------------------------------------------------
# CURRENT SUCCESS SCORE
# ---------------------------------------------------


def get_current_score():

    """
    Later this will come from the
    scoring engine.
    """

    if "user_data" not in st.session_state:

        return 75

    data = st.session_state["user_data"]

    score = 50

    score += int(data["cgpa"] * 3)

    score += data["projects"] * 3

    score += data["hackathons"] * 2

    score += data["internships"] * 4

    score += len(data["skills"])

    return min(score,100)



# ---------------------------------------------------
# WHAT IF ANALYSIS
# ---------------------------------------------------


def what_if_predictions():


    current_score = get_current_score()


    improvements = [


        {

            "title":"Improve CGPA",

            "current":"7.5",

            "target":"8.5",

            "increase":11

        },


        {

            "title":"Complete Two Projects",

            "current":"1",

            "target":"3",

            "increase":7

        },


        {

            "title":"Participate in Hackathons",

            "current":"0",

            "target":"3",

            "increase":6

        },


        {

            "title":"Learn Industry Skills",

            "current":"Basic",

            "target":"Advanced",

            "increase":5

        }


    ]


    final_score = current_score

    for item in improvements:

        final_score += item["increase"]


    final_score = min(final_score,100)


    return current_score, improvements, final_score




# ---------------------------------------------------
# IMPROVEMENT CARD
# ---------------------------------------------------


def improvement_card(item):


    st.success(

        f"""

        ACTION

        {item["title"]}


        ----------------------


        CURRENT

        {item["current"]}


        TARGET

        {item["target"]}


        EXPECTED IMPROVEMENT

        +{item["increase"]}%


        """

    )




# ---------------------------------------------------
# SUCCESS METER
# ---------------------------------------------------


def success_meter(score):

    st.progress(score/100)

    st.write(

        f"Projected Success Score : {score}%"

    )




# ---------------------------------------------------
# MAIN SECTION
# ---------------------------------------------------


def suggestions_section():

    st.title(

        "🧠 AI Decision Intelligence Engine"

    )


    st.write(

        "PATHFINDER AI performs "
        "What-if Analysis to determine "
        "how your future changes when "
        "you improve different aspects "
        "of your profile."

    )


    st.divider()


    # ---------------------------------------


    current_score, improvements, final_score = what_if_predictions()


    # ---------------------------------------


    st.subheader(

        "Current Success Probability"

    )


    success_meter(

        current_score

    )


    st.divider()


    # ---------------------------------------


    st.subheader(

        "AI What-if Simulations"

    )


    col1, col2 = st.columns(2)


    with col1:

        improvement_card(

            improvements[0]

        )


        improvement_card(

            improvements[1]

        )


    with col2:

        improvement_card(

            improvements[2]

        )


        improvement_card(

            improvements[3]

        )


    st.divider()


    # ---------------------------------------


    st.subheader(

        "Projected Future"

    )


    st.write(

        f"""
        Current Score :

        {current_score}%

        """
    )


    st.write(

        "↓"

    )


    st.write(

        f"""
        Future Score :

        {final_score}%
        """

    )


    success_meter(

        final_score

    )


    st.divider()


    # ---------------------------------------


    st.subheader(

        "AI Insights"

    )


    st.info(

        f"""

        PATHFINDER AI predicts that
        implementing all suggested
        improvements may increase your
        predicted success probability by

        {final_score-current_score}%.


        Your most impactful improvements are:


        • Improving Academic Performance

        • Building Industry Projects

        • Participating in Hackathons

        • Developing Technical Skills


        """

    )


    st.divider()


    # ---------------------------------------


    st.subheader(

        "Decision Intelligence Summary"

    )


    st.success(

        f"""

        CURRENT SUCCESS SCORE

        {current_score}%


        --------------------------


        PROJECTED SCORE

        {final_score}%


        --------------------------


        OVERALL IMPROVEMENT

        +{final_score-current_score}%


        --------------------------


        PATHFINDER AI predicts that
        consistently following your
        personalized roadmap will
        significantly improve your
        future opportunities.


        """

    )