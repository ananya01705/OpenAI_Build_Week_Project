import streamlit as st
import time


# ---------------------------------------------
# FUTURE PREDICTIONS
# ---------------------------------------------


def get_future_predictions():

    """
    Dummy outputs for MVP.

    Later these will come from:
        OpenAI API
            +
      Prediction Engine.
    """

    predictions = [

        {

            "title":"Future A",

            "career":"AI Engineer",

            "score":91,

            "timeline":"1 Year",

            "difficulty":"Medium"

        },


        {

            "title":"Future B",

            "career":"Data Scientist",

            "score":86,

            "timeline":"1 Year",

            "difficulty":"Medium"

        },


        {

            "title":"Future C",

            "career":"AI Researcher",

            "score":78,

            "timeline":"2 Years",

            "difficulty":"High"

        },


        {

            "title":"Future D",

            "career":"Startup Founder",

            "score":71,

            "timeline":"3 Years",

            "difficulty":"High"

        }


    ]


    return predictions




# ---------------------------------------------
# PROBABILITY COLORS
# ---------------------------------------------


def get_status(score):

    if score >= 85:

        return "Excellent"

    elif score >= 75:

        return "Very Good"

    elif score >= 65:

        return "Good"

    else:

        return "Moderate"




# ---------------------------------------------
# FUTURE CARDS
# ---------------------------------------------


def future_card(prediction):


    st.markdown(

        f"""
        ### {prediction["title"]}

        **Career Path**

        > {prediction["career"]}


        **Success Probability**

        > {prediction["score"]}%


        **Timeline**

        > {prediction["timeline"]}


        **Difficulty**

        > {prediction["difficulty"]}


        **Prediction**

        > {get_status(prediction["score"])}


        """
    )


    st.progress(

        prediction["score"]/100

    )





# ---------------------------------------------
# TIMELINE SIMULATION
# ---------------------------------------------


def future_timeline():


    st.subheader("Future Timeline Simulation")


    st.markdown(

        """
        ```
        TODAY
           |
           |
        Learn Skills
           |
           |
        Build Projects
           |
           |
        Participate in Hackathons
           |
           |
        Internship Preparation
           |
           |
        Placement Ready
           |
           |
          SUCCESS
        ```
        """

    )




# ---------------------------------------------
# MAIN SECTION
# ---------------------------------------------


def future_simulator():

    st.title("🚀 Future Prediction Engine")


    st.write(

        "PATHFINDER AI predicts multiple "
        "possible futures based upon "
        "your goals and achievements."

    )


    st.divider()


    # -------------------------------------

    generate = st.button(

        "Generate Future Predictions"

    )


    if generate:


        with st.spinner(

            "Predicting your future..."

        ):

            time.sleep(2)


        predictions = get_future_predictions()


        # ---------------------------------

        col1, col2 = st.columns(2)


        with col1:

            future_card(

                predictions[0]

            )


        with col2:

            future_card(

                predictions[1]

            )


        st.divider()


        col3, col4 = st.columns(2)


        with col3:

            future_card(

                predictions[2]

            )


        with col4:

            future_card(

                predictions[3]

            )


        st.divider()


        # ---------------------------------

        st.subheader(

            "AI Decision Intelligence"

        )


        best_future = max(

            predictions,

            key=lambda x:x["score"]

        )


        st.success(

            f"""
            PATHFINDER AI predicts that
            your most promising future is:

            {best_future["career"]}

            with a predicted success
            probability of

            {best_future["score"]}%.
            """
        )


        st.divider()


        future_timeline()


        st.divider()


        st.info(

            """
            These predictions are generated
            by evaluating:

            • Academic Performance

            • Skills

            • Projects

            • Internships

            • Timeline Goals

            • Career Interests

            • Practical Experience
            """

        )