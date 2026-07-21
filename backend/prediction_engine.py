import streamlit as st


# ----------------------------------------------------
# DEFAULT OUTPUTS
# ----------------------------------------------------


DEFAULT_PREDICTIONS = [

    {
        "title":"AI Engineer",
        "score":91,
        "timeline":"1 Year",
        "difficulty":"Medium"
    },

    {
        "title":"Data Scientist",
        "score":86,
        "timeline":"1 Year",
        "difficulty":"Medium"
    },

    {
        "title":"AI Researcher",
        "score":79,
        "timeline":"2 Years",
        "difficulty":"High"
    },

    {
        "title":"Startup Founder",
        "score":73,
        "timeline":"3 Years",
        "difficulty":"High"
    }

]



# ----------------------------------------------------
# SCORE CALCULATOR
# ----------------------------------------------------


def calculate_base_score(user_data):

    """
    Calculates an initial score.

    Later OpenAI outputs will be used
    to enhance these values.
    """

    score = 40


    score += int(user_data["cgpa"]*3)

    score += len(
        user_data["skills"]
    )

    score += (

        user_data["projects"]*3

    )


    score += (

        user_data["internships"]*5

    )


    score += (

        user_data["hackathons"]*2

    )


    return min(score,100)




# ----------------------------------------------------
# CAREER READINESS
# ----------------------------------------------------


def career_readiness(user_data):


    score = (

        int(user_data["cgpa"]*6)

        +

        len(user_data["skills"])*2

        +

        user_data["projects"]*3

    )


    return min(score,100)




# ----------------------------------------------------
# FUTURE STABILITY
# ----------------------------------------------------


def future_stability(user_data):


    score = (

        user_data["projects"]*4

        +

        user_data["internships"]*5

        +

        len(user_data["skills"])*3

        +

        int(user_data["cgpa"]*5)

    )


    return min(score,100)




# ----------------------------------------------------
# INTERNSHIP READINESS
# ----------------------------------------------------


def internship_readiness(user_data):


    score = (

        user_data["projects"]*10

        +

        user_data["internships"]*20

        +

        user_data["hackathons"]*4

        +

        len(user_data["skills"])

    )


    return min(score,100)




# ----------------------------------------------------
# DECISION CONFIDENCE SCORE
# ----------------------------------------------------


def decision_confidence(user_data):


    score = (

        calculate_base_score(
            user_data
        )

        +

        career_readiness(
            user_data
        )

    )//2


    return min(score,100)




# ----------------------------------------------------
# FUTURE PREDICTION ENGINE
# ----------------------------------------------------


def generate_future_predictions(user_data):

    """
    MVP VERSION

    OpenAI will dynamically replace
    these outputs later.
    """

    predictions = []


    base_score = calculate_base_score(

        user_data

    )


    adjustment = base_score//10


    for future in DEFAULT_PREDICTIONS:


        score = future["score"]


        score += adjustment


        score = min(score,100)


        predictions.append(

            {

                "title":
                future["title"],

                "score":
                score,

                "timeline":
                future["timeline"],

                "difficulty":
                future["difficulty"]

            }

        )


    return predictions




# ----------------------------------------------------
# OVERALL ANALYSIS
# ----------------------------------------------------


def overall_analysis(user_data):


    data = {


        "success_score":

        calculate_base_score(

            user_data

        ),


        "career_readiness":

        career_readiness(

            user_data

        ),


        "future_stability":

        future_stability(

            user_data

        ),


        "internship_readiness":

        internship_readiness(

            user_data

        ),


        "decision_confidence":

        decision_confidence(

            user_data

        ),


        "future_predictions":

        generate_future_predictions(

            user_data

        )

    }


    return data




# ----------------------------------------------------
# SESSION STORAGE
# ----------------------------------------------------


def save_analysis(user_data):


    analysis = overall_analysis(

        user_data

    )


    st.session_state[

        "analysis"

    ] = analysis


    return analysis




# ----------------------------------------------------
# FETCH ANALYSIS
# ----------------------------------------------------


def get_analysis():


    if "analysis" in st.session_state:

        return st.session_state[

            "analysis"

        ]


    return None