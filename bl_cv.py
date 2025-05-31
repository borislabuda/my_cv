import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path
import pandas as pd
import os
from PIL import Image
import base64
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
                🔗 <a href="https://linkedin.com/in/boris-labuda-498a5273" target="_blank">LinkedIn</a>
            </p>
            </div>""",unsafe_allow_html=True)


# Contact Information
st.markdown('<div class="content">', unsafe_allow_html=True)
st.markdown("<p></p>",unsafe_allow_html=True)
st.markdown("<div class='step-container'>",unsafe_allow_html=True)
# ----- EXPERIENCE -----

df_exp = pd.read_csv('experience.csv',header=0,sep=';')
def render_experience(title, company, period):
    exp_list = df_exp[df_exp['category'] == title]['item'].tolist()
    st.markdown(f"<div style='color: #e3613e' class='step'>{title} | {company}<div>", unsafe_allow_html=True)
    st.caption(f"{period}")
    styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in exp_list) + "</ul>"
    st.markdown(styled_list, unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)
ch1,ch2 = st.columns(2)

ch1,ch2 = st.columns([1,1])
# --- Roles ---
with ch1:
    #experience markup
    st.markdown("<h2 class='hd1'> 💼 Work Experience</h2>", unsafe_allow_html=True)
    render_experience("Process Automation Senior Developer", "Ecco Shoes", "Oct 2019 – Present")
    render_experience("IT Manager", "Ecco Slovakia", "Jun 2010 – Sep 2019",)
    render_experience("SAP / IT Specialist", "Ecco Slovakia", "Jun 2006 – Aug 2010",)
    render_experience("SAP PP - Master Data Specialist", "Ecco Slovakia", "Oct 2004 – Jun 2006",)
    render_experience("Production Planner", "Ecco Slovakia", "Nov 2002 – Oct 2004",)
   

with ch2:
   
     #projects markup
    df_prj = pd.read_csv('projects.csv',header=0,sep=';')
    st.markdown("<h2 class='hd1'> 💼 Projects</h2>", unsafe_allow_html=True)
    project_areas = df_prj['area'].unique().tolist()
    sel_proj_areas = st.multiselect(label='Pick project areas:', options=project_areas, default=project_areas, )
    
    if sel_proj_areas:
        def render_proj(df: pd.DataFrame, title: str):
                st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
                styled_list = "<ul class='modern-list'>"
                for row in df.iterrows():
                    styled_list+= f"<li class='skill-badge'><span style='color: #e3613e; font-size:10px; font-weight:bold'>{row[1]['area']}/{row[1]['project']}</span><br/> {row[1]['description']}</li><br/>"
                styled_list+="</ul>"
                st.markdown(styled_list, unsafe_allow_html=True)
                st.divider()
            
        fil_proj_df = df_prj[df_prj['area'].isin(sel_proj_areas)]
        fil_proj_df.reset_index(drop=True).style.format(na_rep='-')
        render_proj(fil_proj_df, title="Selected Projects")
     # Skills
        st.markdown("<h2 class='hd1'> 💡 Skills</h2>",unsafe_allow_html=True)
        skills_areas = ['App Development', 'IT specialist/managment','Process Automation', 'SAP Specialist']
        # Load your skills CSV
        base_path = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_path, 'skills.csv')
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

        st.markdown("<h2 class='hd1'> 📚 Education</h2>", unsafe_allow_html=True)

        def render_section(title, items):
            st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
            styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
            st.markdown(styled_list, unsafe_allow_html=True)

        # Data lists
        lst_cert = [
            "Blue Prism Developer Certification",
            "2020"
        ]

        lst_college = [
            "Engineer degree, Operations and economics of railway transport",
            "University of Žilina, Slovakia",
            "09/1997 – 06/2002"
        ]

        lst_mid = [
            "Gymnasium V. P. Tóth, Martin",
            "Graduation, general studies",
            "09/1993 – 06/1997"
        ]

        # Render sections
        edu1,edu2,edu3 = st.columns([1,1,1])
        with edu1:
            render_section("Certification", lst_cert)
        with edu2:
            render_section("University degree", lst_college)
        with edu3:
            render_section("Secondary school", lst_mid)

st.markdown("</div>", unsafe_allow_html=True)

# with open(RESUME_FILE, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.download_button(label="📥 Download Resume", data=PDFbyte, file_name="Boris_Labuda_Resume.pdf", mime="application/pdf")

st.divider()

# Timeline
with st.container():
    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500,)
    #st.write("Current dir contents:", os.listdir())
    #st.write("Current dir contents:", os.listdir())
st.divider()

    
       