import streamlit as st


# -----------------------------------------------------
# LOAD CSS
# -----------------------------------------------------

def load_css():

    st.markdown(
        """
        <style>

        /*================================================*/
        /* MAIN APPLICATION                               */
        /*================================================*/

        .stApp{

            background:
            linear-gradient(
            135deg,
            #050816,
            #0F172A,
            #111827);

            color:white;

        }


        /*================================================*/
        /* SIDEBAR                                        */
        /*================================================*/

        section[data-testid="stSidebar"]{

            background:
            linear-gradient(
            180deg,
            #020617,
            #111827
            );

            border-right:
            1px solid #374151;

        }


        /*================================================*/
        /* HEADINGS                                       */
        /*================================================*/

        h1{

            color:white;
            font-weight:800;
            letter-spacing:1px;

        }


        h2{

            color:white;
            font-weight:700;

        }


        h3{

            color:white;
            font-weight:700;

        }


        h4{

            color:#D1D5DB;

        }



        /*================================================*/
        /* METRIC CARDS                                   */
        /*================================================*/

        div[data-testid="metric-container"]{


            background:
            rgba(17,24,39,0.8);

            backdrop-filter:blur(18px);

            padding:25px;

            border-radius:20px;

            border:
            1px solid #374151;

            box-shadow:

            0 0 20px
            rgba(59,130,246,0.25);

            transition:0.3s;


        }


        div[data-testid="metric-container"]:hover{


            transform:
            translateY(-5px);

            box-shadow:

            0 0 28px
            rgba(59,130,246,0.45);


        }



        /*================================================*/
        /* BUTTONS                                        */
        /*================================================*/


        .stButton>button{


            width:100%;

            background:
            linear-gradient(
            90deg,
            #2563EB,
            #3B82F6
            );

            color:white;

            border:none;

            border-radius:15px;

            padding:15px;

            font-size:18px;

            font-weight:bold;

            transition:0.3s;


        }



        .stButton>button:hover{


            transform:scale(1.03);

            box-shadow:

            0 0 18px
            rgba(37,99,235,0.7);


        }



        /*================================================*/
        /* INPUT BOXES                                    */
        /*================================================*/


        .stTextInput input{


            background-color:#111827;

            color:white;

            border-radius:15px;

            border:
            1px solid #374151;


        }


        .stNumberInput input{


            background-color:#111827;

            color:white;

            border-radius:15px;


        }


        textarea{


            background-color:
            #111827 !important;

            color:white !important;


        }



        /*================================================*/
        /* SELECT BOXES                                   */
        /*================================================*/


        .stSelectbox div{


            border-radius:15px;


        }



        /*================================================*/
        /* SLIDERS                                        */
        /*================================================*/


        .stSlider{


            color:white;


        }



        /*================================================*/
        /* CUSTOM CARDS                                   */
        /*================================================*/


        .custom-card{


            background:
            rgba(17,24,39,0.8);

            backdrop-filter:
            blur(15px);

            padding:25px;

            border-radius:25px;

            border:
            1px solid #374151;

            margin-bottom:20px;

            box-shadow:

            0 0 18px
            rgba(37,99,235,0.2);


        }



        /*================================================*/
        /* FUTURE SIMULATOR CARDS                          */
        /*================================================*/


        .future-card{


            background:
            rgba(17,24,39,0.9);

            padding:30px;

            border-radius:25px;

            text-align:center;

            margin-bottom:20px;

            border:
            1px solid #374151;

            box-shadow:

            0 0 22px
            rgba(37,99,235,0.25);

            transition:0.3s;


        }



        .future-card:hover{


            transform:
            scale(1.02);


        }



        /*================================================*/
        /* ROADMAP BOXES                                  */
        /*================================================*/


        .roadmap-box{


            background:
            rgba(17,24,39,0.85);

            padding:25px;

            border-radius:20px;

            border-left:
            6px solid #3B82F6;

            margin-bottom:20px;

            box-shadow:

            0 0 15px
            rgba(37,99,235,0.2);


        }



        /*================================================*/
        /* SUCCESS BOXES                                  */
        /*================================================*/


        .success-box{


            background:
            rgba(5,46,22,0.9);

            padding:25px;

            border-radius:20px;

            color:white;

            border-left:
            6px solid #22C55E;

            margin-bottom:20px;


        }



        /*================================================*/
        /* WARNING BOXES                                  */
        /*================================================*/


        .warning-box{


            background:
            rgba(63,29,29,0.9);

            padding:25px;

            border-radius:20px;

            color:white;

            border-left:
            6px solid orange;

            margin-bottom:20px;


        }



        /*================================================*/
        /* PROGRESS BAR                                   */
        /*================================================*/


        .stProgress>div>div>div{


            background:
            linear-gradient(
            90deg,
            #2563EB,
            #38BDF8
            );


        }



        /*================================================*/
        /* DIVIDER                                        */
        /*================================================*/


        hr{

            border-color:#374151;

        }



        /*================================================*/
        /* GLOW EFFECT                                    */
        /*================================================*/


        .glow{


            animation:
            glow-animation
            2s infinite alternate;


        }


        @keyframes glow-animation{


            from{

                box-shadow:

                0 0 12px
                rgba(37,99,235,0.4);

            }


            to{


                box-shadow:

                0 0 30px
                rgba(37,99,235,0.8);

            }

        }



        /*================================================*/
        /* SCROLL BAR                                     */
        /*================================================*/


        ::-webkit-scrollbar{

            width:10px;

        }


        ::-webkit-scrollbar-thumb{


            background:#374151;

            border-radius:20px;

        }



        /*================================================*/
        /* HIDE STREAMLIT FOOTER                           */
        /*================================================*/


        footer{

            visibility:hidden;

        }


        #MainMenu{

            visibility:hidden;

        }



        </style>
        """,

        unsafe_allow_html=True

    )