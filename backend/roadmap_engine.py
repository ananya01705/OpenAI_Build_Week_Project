# ---------------------------------------------
# DEFAULT ROADMAPS
# ---------------------------------------------


AI_ENGINEER = {

    "30 Days":[

        "Learn Python",
        "Git & GitHub",
        "Practice Problem Solving"

    ],

    "60 Days":[

        "Learn SQL",
        "Build One Project",
        "Participate in Hackathons"

    ],

    "90 Days":[

        "Build AI Projects",
        "Learn APIs",
        "Improve Portfolio"

    ],

    "6 Months":[

        "Apply for Internships",
        "Build Industry Projects"

    ],

    "1 Year":[

        "Become Internship Ready",
        "Prepare for Placments"

    ]

}



DATA_SCIENCE = {

    "30 Days":[

        "Python",

        "NumPy",

        "Pandas"

    ],

    "60 Days":[

        "Statistics",

        "SQL",

        "Projects"

    ],

    "90 Days":[

        "Machine Learning",

        "Visualization"

    ],

    "6 Months":[

        "Internships",

        "Hackathons"

    ],

    "1 Year":[

        "Career Ready"

    ]

}




# ------------------------------------------------
# SELECT ROADMAP
# ------------------------------------------------


def get_roadmap(user_data):


    goal = user_data["goal"]


    if goal == "AI Engineer":

        return AI_ENGINEER


    if goal == "Data Scientist":

        return DATA_SCIENCE


    # DEFAULT ROADMAP


    return AI_ENGINEER




# ------------------------------------------------
# EXPECTED IMPROVEMENT
# ------------------------------------------------


def expected_growth():

    return {


        "30 Days":8,

        "60 Days":16,

        "90 Days":25,

        "6 Months":40,

        "1 Year":60

    }




# ------------------------------------------------
# DIFFICULTY
# ------------------------------------------------


def roadmap_difficulty():

    return {

        "30 Days":"Easy",

        "60 Days":"Medium",

        "90 Days":"Medium",

        "6 Months":"High",

        "1 Year":"High"

    }




# ------------------------------------------------
# FUTURE IMPACT
# ------------------------------------------------


def future_impact():

    return {

        "30 Days":"Moderate",

        "60 Days":"High",

        "90 Days":"High",

        "6 Months":"Very High",

        "1 Year":"Excellent"

    }




# ------------------------------------------------
# GENERATE COMPLETE ROADMAP
# ------------------------------------------------


def generate_roadmap(user_data):


    roadmap = get_roadmap(

        user_data

    )


    growth = expected_growth()

    difficulty = roadmap_difficulty()

    impact = future_impact()


    complete_roadmap = {}


    for stage in roadmap:


        complete_roadmap[stage] = {

            "tasks":

            roadmap[stage],


            "growth":

            growth[stage],


            "difficulty":

            difficulty[stage],


            "impact":

            impact[stage]

        }


    return complete_roadmap