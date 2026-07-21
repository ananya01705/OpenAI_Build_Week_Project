import os
import json

from openai import OpenAI


# ------------------------------------------
# INITIALIZATION
# ------------------------------------------


client = OpenAI(

    api_key=os.getenv(
        "OPENAI_API_KEY"
    )

)


# ------------------------------------------
# SYSTEM PROMPT
# ------------------------------------------


SYSTEM_PROMPT = """

You are PATHFINDER AI.

You are NOT a chatbot.

You are an AI Decision Intelligence Engine.

Your objective is to:

1. Analyze student goals.
2. Predict multiple future paths.
3. Estimate success probabilities.
4. Generate personalized roadmaps.
5. Suggest improvements.
6. Perform What-if Analysis.


Always return structured outputs.


"""



# ------------------------------------------
# PROMPT CREATOR
# ------------------------------------------


def create_prompt(user_data):


    prompt = f"""


Analyze the following student profile.


Name:
{user_data['name']}


Academic Year:
{user_data['year']}


CGPA:
{user_data['cgpa']}


Goal:
{user_data['goal']}


Timeline:
{user_data['timeline']}


Skills:
{user_data['skills']}


Interests:
{user_data['interests']}


Projects:
{user_data['projects']}


Internships:
{user_data['internships']}


Hackathons:
{user_data['hackathons']}


Description:
{user_data['description']}



Perform the following tasks:


1. Predict FOUR possible futures.

For each future provide:

- title
- success probability
- timeline
- difficulty level


--------------------------------


2. Generate:

- success score
- career readiness score
- internship readiness score
- future stability score


--------------------------------


3. Generate:

30 day roadmap

60 day roadmap

90 day roadmap

6 month roadmap

1 year roadmap


--------------------------------


4. Perform What-if Analysis.


Examples:

CGPA improvement

Project completion

Hackathons

Industry skills


--------------------------------


Return ONLY valid JSON.

Do NOT include markdown.

"""


    return prompt




# ------------------------------------------
# OPENAI CALL
# ------------------------------------------


def generate_prediction(user_data):


    prompt = create_prompt(

        user_data

    )


    response = client.responses.create(

        model="gpt-5",

        instructions=SYSTEM_PROMPT,

        input=prompt,

        max_output_tokens=2000

    )


    output = response.output_text


    return output




# ------------------------------------------
# JSON PARSER
# ------------------------------------------


def parse_response(response):


    try:

        data = json.loads(

            response

        )

        return data


    except Exception:


        return {

            "error":

            "Unable to parse response."

        }




# ------------------------------------------
# MAIN FUNCTION
# ------------------------------------------


def pathfinder_engine(user_data):


    response = generate_prediction(

        user_data

    )


    data = parse_response(

        response

    )


    return data