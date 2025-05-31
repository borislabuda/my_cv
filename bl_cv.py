import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path
import pandas as pd
import os
from cv_css import cv_css


# Set up the page configuration
st.set_page_config(page_title='CV Boris Labuda' ,layout="wide",page_icon='👧🏻')
st.markdown(cv_css, unsafe_allow_html=True)


CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
RESUME_FILE = CURRENT_DIR / "resume.pdf"


#Header
st.markdown("""<div class="fixed-banner">
            <p class='big-font'>Boris Labuda</p>
            <p class='tight-font' style='line-height: 0.2; color: gainsboro;'>Experience summary</p><br/><br/>
            <p class="contact-style">
                📍 <a href="#">Martin, SK</a><br/>
                📧 <a href="mailto:blabuda@gmail.com">blabuda@gmail.com</a><br/>
                📍 <a href="#">Martin, SK</a><br/>
                📧 <a href="mailto:blabuda@gmail.com">blabuda@gmail.com</a><br/>
                🔗 <a href="https://linkedin.com/in/boris-labuda-498a5273" target="_blank">LinkedIn</a>
            </p>
            </div>""",unsafe_allow_html=True)


# Contact Information
st.markdown('<div class="content">', unsafe_allow_html=True)
st.markdown("<p></p>",unsafe_allow_html=True)
st.markdown("<p style='font-size: 26px;'><em>Shortly about me  ...</em></p><br/></div>",unsafe_allow_html=True) 
st.markdown("<div class='step-container'>",unsafe_allow_html=True)
hc1,hc2,hc3 = st.columns([1,1,1])
with hc1:
    st.markdown(""" <div class='step'><p class='modern-text'>I have dedicated my professional career to ECCO Shoes, 
                where over the past 23 years I’ve combined my technical expertise with a deep understanding of business operations. 
                My experience encompasses a broad range of areas, including <span style="color: #e3613e;">RPA development, IT management, SAP support, production processes</span> and supporting them with suitable software solutions.</p>
                 <div class="timeline-circle">1</div>
                 </div>
""",unsafe_allow_html=True)
    st.markdown("""<div class='step'><p class='modern-text'><span style="color: #e3613e;">Currently, I design and implement scalable automation solutions using Blue Prism</span>.
                I work closely with business stakeholders to identify automation opportunities and mentor junior developers on RPA best practices. <br/>Throughtout this time <span style="color: #e3613e;">I have developed custom scheduling and reporting Blue Prism solution, which enabled our team to save significant time and resources
                on BP operations</span> by introducing dynamic scheduling and resource assignment.
                I have background in .NET WPF and ASP.NET development, and recently expanding my skill set through Python to extend and integrate automations with APIs and data pipelines. 
                My ability to adapt and modernize legacy systems with current technologies can add real value in hybrid environments.</p>
                 <div class="timeline-circle">2</div>
                </div>
    """,unsafe_allow_html=True)
with hc2:
    st.markdown("""<div class='step'><p class='modern-text'><span style="color: #e3613e;">Previously, I led ECCO Slovakia’s IT team for 9 years</span>, managing infrastructure, vendor relations, and user support for 200+ employees. 
                My earlier roles in SAP PP/WM support and production planning gave me a practical foundation in manufacturing and supply chain systems.
            💡 I’m passionate about streamlining processes, bridging technical and business teams, and delivering long-term, maintainable solutions.
                </p>
                <div class="timeline-circle">3</div>
                </div>
""",unsafe_allow_html=True)
    st.markdown("""<div class='step'><p class='modern-text'>I am a married father of two living in Martin, Slovakia.
                In my free time I'm spending quality time with my family, I enjoy hiking in the beautiful Slovak mountains, and I love exploring new technologies. To relax, I often read books, watch a good movie, or play video games with my kids.
                </p>
                <div class="timeline-circle">4</div>
                </div>
""",unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# with open(RESUME_FILE, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.download_button(label="📥 Download Resume", data=PDFbyte, file_name="Boris_Labuda_Resume.pdf", mime="application/pdf")
st.divider()
# Timeline
#timeline
with st.container():
    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500,)
    #st.write("Current dir contents:", os.listdir())
    #st.write("Current dir contents:", os.listdir())
st.divider()
with st.container():
    
    col1,col2,col3 = st.columns(3)
    with col1:
        # Skills
        st.markdown("<h2 class='hd1'> 💼 Skills</h2>",unsafe_allow_html=True)
        skills_areas = ['App Development', 'IT specialist/managment','Process Automation', 'SAP Specialist']
        # Load your skills CSV
        base_path = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_path, 'Skills.csv')
        df_skills = pd.read_csv(csv_path,header=0,sep=';')  # Adjust the path to your CSV file
        df_skills.dropna(subset='Area', inplace=True)  # Remove rows where 'Area' is NaN
        areas = df_skills['Area'].unique().tolist()
        selected_areas = st.multiselect(label='Pick skill areas:',
                                        options=areas,
                                        )
        if selected_areas:
            
            def render_skills(df: pd.DataFrame, title: str):
                st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
                styled_list = "<ul class='modern-list'>"
                for row in df.iterrows():
                    styled_list+= f"<li class='skill-badge'><span style='color: #e3613e; font-size:10px; font-weight:bold'>{row[1]['Category']}</span> {row[1]['Skill']}</li>"
                styled_list+="</ul>"
                st.markdown(styled_list, unsafe_allow_html=True)
                st.divider()
            
            filtered_df = df_skills[df_skills['Area'].isin(selected_areas)]
            filtered_df.reset_index(drop=True).style.format(na_rep='-')
            render_skills(filtered_df, title="Selected Skills"
    )
        else:
            st.write("Please select at least one skill area to display.")
    #=============================================================================================
    with col2:
        # ----- EXPERIENCE -----
        st.markdown("<h2 class='hd1'> 💼 Work Experience</h2>", unsafe_allow_html=True)

        def render_experience(title, company, period, items):
            st.markdown(f"<h3 style='color: #e3613e'>{title} | {company}</h3>", unsafe_allow_html=True)
            st.caption(f"{period}")
            styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
            st.markdown(styled_list, unsafe_allow_html=True)

        # --- Roles ---
        render_experience(
            "Process Automation Senior Developer", "Ecco Shoes", "Oct 2019 – Present",
            [
                "Development of automated solutions in Blue Prism.",
                "Management of Blue Prism infrastructure.",
                "Development of custom Blue Prism scheduler and reporting app / license cost savings of 50%.",
                "Collaboration with business stakeholders to identify automation opportunities.",
                "Mentoring junior developers in RPA best practices."
            ]
        )

        render_experience(
            "IT Manager", "Ecco Slovakia", "Jun 2010 – Sep 2019",
            [
                "Led a team of 4 IT specialists.",
                "IT infrastructure management.",
                "Support for 200+ users.",
                "Budget management.",
                "Projects management.",
                "User security management.",
                "Vendor and asset management.",
                "Local app development / VB.NET WinForms, ASP.NET, WPF."
            ]
        )

        render_experience(
            "SAP / IT Specialist", "Ecco Slovakia", "Jun 2006 – Aug 2010",
            [
                "SAP PP and WM user support.",
                "SAP PP and WM master data maintenance.",
                "General IT user support."
            ]
        )

        render_experience(
            "SAP PP - Master Data Specialist", "Ecco Slovakia", "Oct 2004 – Jun 2006",
            [
                "SAP PP master data maintenance.",
                "SAP PP user support."
            ]
        )

        render_experience(
            "Production Planner", "Ecco Slovakia", "Nov 2002 – Oct 2004",
            [
                "Planning shoe production schedule.",
            "Reporting and production follow-up."
        ]
    )
        #=============================================================================================
    with col3:
        st.markdown("<h2 class='hd1'> 📚 Education</h2>", unsafe_allow_html=True)

        def render_section(title, items):
            st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
            styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
            st.markdown(styled_list, unsafe_allow_html=True)
            st.divider()

        # Data lists
        lst_cert = [
            "Blue Prism Developer Certification",
            "2020"
        ]

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

        # Render sections
        render_section("Certifikácia", lst_cert)
        render_section("Vysoká škola", lst_college)
        render_section("Stredná škola", lst_mid)