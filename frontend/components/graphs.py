import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# --------------------------------------------------
# FUTURE PATH COMPARISON
# --------------------------------------------------


def future_probability_chart():

    data = pd.DataFrame({

        "Career":[

            "AI Engineer",
            "Data Scientist",
            "AI Researcher",
            "Startup Founder"

        ],

        "Success Score":[

            91,
            86,
            78,
            71

        ]

    })


    fig = px.bar(

        data,

        x="Career",

        y="Success Score",

        title="Future Success Probabilities"

    )


    fig.update_layout(

        template="plotly_dark",
        height=500

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



# --------------------------------------------------
# CAREER READINESS RADAR CHART
# --------------------------------------------------


def readiness_chart():

    categories = [

        "Skills",
        "Projects",
        "Internships",
        "CGPA",
        "Leadership",
        "Career Readiness"

    ]


    values = [

        88,
        82,
        75,
        90,
        80,
        86

    ]


    fig = go.Figure()


    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill='toself',

            name="Readiness"

        )

    )


    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0,100]

            )

        ),

        template="plotly_dark",

        height=500,

        title="AI Career Readiness Analysis"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



# --------------------------------------------------
# FUTURE TIMELINE GROWTH
# --------------------------------------------------


def growth_projection_chart():

    timeline = pd.DataFrame({

        "Stage":[

            "Today",
            "30 Days",
            "60 Days",
            "90 Days",
            "6 Months",
            "1 Year"

        ],

        "Growth Score":[

            40,
            55,
            68,
            79,
            88,
            96

        ]

    })


    fig = px.line(

        timeline,

        x="Stage",

        y="Growth Score",

        markers=True,

        title="Predicted Growth Projection"

    )


    fig.update_layout(

        template="plotly_dark",

        height=500

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



# --------------------------------------------------
# SKILL DISTRIBUTION
# --------------------------------------------------


def skill_distribution_chart():

    labels = [

        "Technical Skills",
        "Projects",
        "Internships",
        "Hackathons",
        "Soft Skills"

    ]


    values = [

        35,
        20,
        15,
        15,
        15

    ]


    fig = go.Figure(

        data=[

            go.Pie(

                labels=labels,

                values=values,

                hole=0.45

            )

        ]

    )


    fig.update_layout(

        title="Profile Distribution",

        template="plotly_dark",

        height=500

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------


def probability_graphs():

    st.title("📈 Decision Intelligence Visualizer")


    st.write(

        "PATHFINDER AI visualizes your "
        "future possibilities and predicts "
        "your career trajectory."

    )


    st.divider()


    # ------------------------------------

    st.subheader(

        "Future Path Comparison"

    )

    future_probability_chart()


    st.divider()


    # ------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        readiness_chart()


    with col2:

        skill_distribution_chart()


    st.divider()


    # ------------------------------------

    st.subheader(

        "Growth Projection"

    )

    growth_projection_chart()


    st.divider()


    st.info(

        """
        PATHFINDER AI continuously evaluates:

        • Skills

        • Academic Performance

        • Practical Experience

        • Career Goals

        • Timeline Objectives

        • Future Opportunities

        to generate personalized predictions.
        """

    )