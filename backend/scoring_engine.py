# ---------------------------------------------
# SUCCESS SCORE
# ---------------------------------------------


def success_score(data):


    score = 45


    score += int(

        data["cgpa"]*3

    )


    score += (

        data["projects"]*4

    )


    score += (

        data["internships"]*5

    )


    score += (

        data["hackathons"]*3

    )


    score += len(

        data["skills"]

    )


    return min(score,100)




# ---------------------------------------------
# CAREER READINESS
# ---------------------------------------------


def career_readiness(data):


    score = (

        int(data["cgpa"]*5)

        +

        data["projects"]*5

        +

        len(data["skills"])*2

    )


    return min(score,100)




# ---------------------------------------------
# FUTURE STABILITY
# ---------------------------------------------


def future_stability(data):


    score = (

        int(data["cgpa"]*4)

        +

        data["projects"]*5

        +

        data["internships"]*8

        +

        len(data["skills"])*2

    )


    return min(score,100)




# ---------------------------------------------
# DECISION CONFIDENCE
# ---------------------------------------------


def decision_confidence(data):


    score = (

        success_score(data)

        +

        career_readiness(data)

        +

        future_stability(data)

    )//3


    return min(score,100)




# ---------------------------------------------
# INTERNSHIP READINESS
# ---------------------------------------------


def internship_readiness(data):


    score = (

        data["projects"]*10

        +

        data["internships"]*20

        +

        data["hackathons"]*4

        +

        len(data["skills"])

    )


    return min(score,100)




# ---------------------------------------------
# COMPLETE ANALYSIS
# ---------------------------------------------


def complete_analysis(data):


    return {

        "success_probability":

        success_score(data),


        "career_readiness":

        career_readiness(data),


        "future_stability":

        future_stability(data),


        "decision_confidence":

        decision_confidence(data),


        "internship_readiness":

        internship_readiness(data)

    }