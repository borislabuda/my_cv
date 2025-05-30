import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path
import pandas as pd


# Set up the page configuration
st.set_page_config(page_title='CV Boris Labuda' ,layout="wide",page_icon='👧🏻')
st.markdown("""
    <style>
        .fixed-banner {
            position: fixed;
            top: 60px;
            left: 0;
            right: 0;
            height: 150px;
            background-color: #e3613e;
            color: white;
            font-size: 18px;
            font-weight: normal;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            align-items: center;
            justify-content: left;
            padding: 20px;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .content {
            margin-top: 70px;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        .big-font {
            font-size: 65px !important;
            font-weight: normal;
            line-height: 0.5;
            color: white;
        }
        .tight-font {
            font-weight: normal;
            padding: 0px;
            font-size: 25px !important;
            margin: 0px;
            line-height: 0.5;
        }
        body {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
            color: #333;
        }
        hd1 {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
            color: #2E8B57;
        }
        hd2 {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
        }
        hd3 {
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        .custom-title {
            font-size: 36px;
            color: navy;
            font-weight: bold;
        }
        html, body, [class*="css"]  {
             line-height: 1;
        }
        ul.modern-list {
        list-style: none;
        padding: 0;
        font-size: 15px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        ul.modern-list li {
            background: white;
            margin: 8px 0;
            padding: 10px 14px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
        }
        ul.modern-list li:hover {
            background: #e0e4ea;
            transform: translateX(4px);
        }
        p.modern-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 16px;
        color: #333;
        line-height: 1.6;
        margin-bottom: 1em;
        max-width: 700px;
        text-align: justify;
        }
        .contact-style a {
            all: unset;
            cursor: pointer;
            font-weight: 500;
            color: white;
        }
        .contact-style a:hover {
            color: salmon;
            text-decoration: underline;
        }
        .vis-timeline {
            font-family: 'Segoe UI', sans-serif !important;
            font-size: 14px;
        }
    </style>
    </style>
""", unsafe_allow_html=True)


CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
RESUME_FILE = CURRENT_DIR / "resume.pdf"


#Header
st.markdown("""<div class="fixed-banner">
            <p class='big-font'>Ing. Boris Labuda</p><br/>
            <p class='tight-font'>Process automation senior developer</p><br/>
            <p class="contact-style">
                📍 Martin, SK |
                📧 <a href="mailto:blabuda@gmail.com">blabuda@gmail.com</a> |
                🔗 <a href="https://linkedin.com/in/boris-labuda-498a5273" target="_blank">LinkedIn</a>
            </p>
            </div>""",unsafe_allow_html=True)


# Contact Information
st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown("<p></p>",unsafe_allow_html=True)
st.header("🧑‍💼 Profile")

hc1,hc2,hc3 = st.columns([1,1,1])
with hc1:
    st.markdown(""" <div style="background-color: #efefef; padding: 20px; border-radius: 12px;"><p class='modern-text'>I'm a <span style="color: #e3613e;">Process Automation Senior Developer</span> with over 20 years of experience at ECCO Shoes, blending hands-on technical skills with a deep understanding of business operations. 
                My career spans <em>RPA development, IT management, SAP support, and custom software solutions.</em></p></div>
""",unsafe_allow_html=True)
with hc2:
    st.markdown("""<div style="background-color: #f5f5f5; padding: 20px; border-radius: 12px;"><p class='modern-text'>Currently, I design and implement scalable automation solutions using Blue Prism, including a custom-built scheduling and reporting platform that cut license costs by 50%. 
                I work closely with business stakeholders to identify automation opportunities and mentor junior developers on RPA best practices.
                I have a solid background in .NET WPF and ASP.NET development, and recently expanded my skill set through Python training — now using Python to extend and integrate automations with APIs and data pipelines. 
                My ability to adapt and modernize legacy systems with current technologies adds real value in hybrid environments.</p>
    </div>
    """,unsafe_allow_html=True)
with hc3:
    st.markdown("""<div style="background-color: #e1e1e1; padding: 20px; border-radius: 12px;"><p class='modern-text'>Previously, I led ECCO Slovakia’s IT team, managing infrastructure, vendor relations, and user support for 200+ employees. 
                My earlier roles in SAP PP/WM support and production planning gave me a practical foundation in manufacturing and supply chain systems.
            💡 I’m passionate about streamlining processes, bridging technical and business teams, and delivering long-term, maintainable solutions.
                </p>
                </div>
""",unsafe_allow_html=True)
# with open(RESUME_FILE, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.download_button(label="📥 Download Resume", data=PDFbyte, file_name="Boris_Labuda_Resume.pdf", mime="application/pdf")

#timeline
with st.container():

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500,)

st.divider()
with st.container():
    
    col1,col2,col3 = st.columns(3)
    with col1:
        # Skills
        st.markdown("<h2 class='hd1'> 💼 Skills</h2>",unsafe_allow_html=True)
        st.divider()
        skills_areas = ['App Development', 'IT specialist/managment','Process Automation', 'SAP Specialist']
        # Load your skills CSV
        df_skills = pd.read_csv('skills.csv',header=0,sep=';')  # Adjust the path to your CSV file
        df_skills.dropna(subset='Area', inplace=True)  # Remove rows where 'Area' is NaN
        areas = df_skills['Area'].unique().tolist()
        selected_areas = st.multiselect(label='Pick skill areas:',
                                        options=areas,
                                        )
        if selected_areas:
            
            filtered_df = df_skills[df_skills['Area'].isin(selected_areas)]
            st.dataframe(
        filtered_df.reset_index(drop=True).style.format(na_rep='-')
    )
        else:
            st.write("Please select at least one skill area to display.")

    #=============================================================================================
    with col2:
        # ----- EXPERIENCE -----
        st.markdown("<h2 class='hd1'> 💼 Work Experience</h2>",unsafe_allow_html=True)
        st.divider()
        # region -----------Automation developer | Ecco Shoes-------------------
        st.markdown("<h3 style='color: #e3613e'>Process automation senior developer | Ecco Shoes",unsafe_allow_html=True)
        st.caption("Oct 2019 – Present")
        lst_automation = [
            "Development of automated solutions in Blue Prism.",
            "Management of Blue Prism infrastructure.",
            "Development of custom Blue Prism scheduler and reporting app / license cost savings of 50%.",
            "Collaboration with business stakeholders to identify automation opportunities.",
            "Mentoring junior developers in RPA best practices."
        ]
        styled_list = "<ul class='modern-list'>"
        styled_list += "".join([f"<li>{skill}</li>" for skill in lst_automation])
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
      # end region ---------------------------------------------------------------------------------
      # region ------------------IT manager | Ecco Slovakia-------------------
        st.markdown("<h3 style='color: #e3613e'>IT manager| Ecco Slovakia</h3>",unsafe_allow_html=True)
        st.caption("Jun 2010 – Sep 2019")
        lst_itman = [
            "Led a team of 4 IT specialists.",
            "IT infrastructure management.",
            "Support for 200+ users.",
            "Budget management.",
            "Projects management.",
            "User cecurity management.",
            "Vendor and asset management.",
            "Local app development / VB.NET WinForms, ASP.NET, WPF."
        ]
        styled_list = "<ul class='modern-list'>"
        styled_list += "".join([f"<li>{skill}</li>" for skill in lst_itman])
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
        st.markdown("""
        """)     
        # endregion----------------------------------------------------------------------------------
        # region ------------------SAP / IT specialist | Ecco Slovakia-------------------
        st.markdown("<h3 style='color: #e3613e'>SAP / IT specialist | Ecco Slovakia</h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>Jun 2006 – Aug 2010</p>",unsafe_allow_html=True)
        lst_itspec = [
            "SAP PP and WM user support.",
            "SAP PP and WM master data maintenance.",
            "General IT user support."
        ]
        styled_list = "<ul class='modern-list'>"
        styled_list += "".join([f"<li>{skill}</li>" for skill in lst_itspec])
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
        # endregion----------------------------------------------------------------------------------
        # region ------------------SAP PP - master data specialist | Ecco Slovakia-------------------
        st.markdown("<h3 style='color: #e3613e'>SAP PP - master data specialist  | Ecco Slovakia</h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>Oct 2004 – Jun 2006</p>",unsafe_allow_html=True)
        lst_md = [
            "SAP PP master data maintenance.",
            "SAP PP user support."
        ]
        styled_list = "<ul class='modern-list'>"
        styled_list += "".join([f"<li>{skill}</li>" for skill in lst_md])
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
        # endregion----------------------------------------------------------------------------------
        #------------------Production planner  | Ecco Slovakia-------------------
        st.markdown("<h3 style='color: #e3613e'>Production planner  | Ecco Slovakia</h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>Nov 2002 – Oct 2004</p>",unsafe_allow_html=True)
        lst_plan = [
            "Planning shoe production schedule.",
            "Reporting and production follow-up."
        ]
        styled_list = "<ul class='modern-list'>"
        styled_list += "".join([f"<li>{skill}</li>" for skill in lst_plan])
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
    #=============================================================================================
    with col3:
        st.markdown("<h2 class='hd1'> 📚 Education</h2>",unsafe_allow_html=True)
        st.divider()
        # Škola 1 – Vysoká škola
        
        lst_college = [
            "Inžiniersky titul, Prevádzka a ekonomika železničnej dopravy",
            "Žilinská univerzita v Žiline",
            "09/1997 – 06/2002"
        ]
        
        lst_mid = [
            "Gymnázium V. P. Tótha, Martin",
            "Maturita, všeobecné štúdium",
            "09/1993 – 06/1997"
        ]
        
        styled_list_college = "<ul class='modern-list'>"        
        #certifikácia
        lst_cert = [
            "Blue Prism Developer Certification",
            "2020"
        ]
        
        st.markdown("<h3 style='color: #e3613e'>Certifikácia</h3>",unsafe_allow_html=True)
        styled_list_cert = "<ul class='modern-list'>"
        styled_list_cert += "".join([f"<li>{cert}</li>" for cert in lst_cert])
        styled_list_cert += "</ul>"
        st.markdown(styled_list_cert, unsafe_allow_html=True)
        st.divider()
        st.markdown("<h3 style='color: #e3613e'>Vysoká škola</h3>",unsafe_allow_html=True)
        styled_list_college = "<ul class='modern-list'>"
        styled_list_college += "".join([f"<li>{item}</li>" for item in lst_college])
        styled_list_college += "</ul>"
        st.markdown(styled_list_college, unsafe_allow_html=True)
        st.divider()
        st.markdown("<h3 style='color: #e3613e'>Stredná škola</h3>",unsafe_allow_html=True)
        styled_list_mid = "<ul class='modern-list'>"
        styled_list_mid += "".join([f"<li>{item}</li>" for item in lst_mid])
        styled_list_mid += "</ul>"
        st.markdown(styled_list_mid, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)