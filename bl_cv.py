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
            <p class='tight-font' style='line-height: 0.2; color: gainsboro;'>Experience summary</p>
            </div>""",unsafe_allow_html=True)

with st.expander('Contact info', expanded=True):
    st.markdown('''<p class="contact-style">
                📍 <a href="#">Martin, SK</a>
                📧 <a href="mailto:blabuda@gmail.com">blabuda@gmail.com</a><br/>
                🔗 <a href="https://linkedin.com/in/boris-labuda-498a5273" target="_blank">LinkedIn</a>
                    <img src="https://github.com/favicon.ico" alt="GitHub" style="width: 16px; height: 16px; vertical-align: middle;"/> <a href="https://github.com/borislabuda" target="_blank">GitHub</a>
                </p>''', unsafe_allow_html=True)
    with open('bl_cv.pdf', "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="📥 Download Resume", data=PDFbyte, file_name="Boris_Labuda_Resume.pdf", mime="application/pdf")
#================================================================================================
# ----- EXPERIENCE -----
df_exp = pd.read_csv('data/experience.csv',header=0,sep=';')
def render_experience(title: str, company: str, period: str, expanded: bool):
    """
    Render a single work experience block with an expandable list of items.

    Args:
        title (str): Job title/category.
        company (str): Company name.
        period (str): Employment period.
    """
    # Filter experience items by category (job title)
    exp_list = df_exp[df_exp['category'] == title]['item'].tolist()

    # Display job title and company with styling
    st.markdown(
        f"<div style='color: #e3613e' class='step'>{title} | {company}</div>",
        unsafe_allow_html=True
    )
    st.caption(period)

    # Create an expander for the list of experience items
    with st.expander("Show details",expanded=expanded):
        styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in exp_list) + "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)

ch1,ch2,ch3 = st.columns([1,0.1,1])

with ch1:
    #experience markup
    st.markdown("<h2 class='hd1'> 📑 Work Experience</h2>", unsafe_allow_html=True)
    render_experience("Process Automation Senior Developer", "Ecco Shoes", "Oct 2019 – Present",expanded=True)
    render_experience("IT Manager", "Ecco Slovakia", "Jun 2010 – Sep 2019",expanded=True)
    render_experience("SAP / IT Specialist", "Ecco Slovakia", "Jun 2006 – Aug 2010",expanded=True)
    render_experience("SAP PP - Master Data Specialist", "Ecco Slovakia", "Oct 2004 – Jun 2006",expanded=False)
    render_experience("Production Planner", "Ecco Slovakia", "Nov 2002 – Oct 2004",expanded=False)
#===============================================================================================
with ch2: # separator column
    st.markdown(
        """
        <div></div>
        """,
        unsafe_allow_html=True
    )
#===============================================================================================
with ch3:
    
    # ==================== Projects Section ====================
    st.markdown(
        """
        <div style="height: 100%; width: 1px; background-color: #ccc; margin: auto;"></div>
        """,
        unsafe_allow_html=True
    )
    # Load projects data
    df_prj = pd.read_csv('data/projects.csv', header=0, sep=';')

    # Section title
    st.markdown("<h2 class='hd1'> 🚩 Projects</h2>", unsafe_allow_html=True)

    # Get unique project areas for selection
    project_areas = df_prj['area'].unique().tolist()

    # Multiselect widget for project areas
    sel_proj_areas = st.multiselect(
        label='Pick project areas:',
        options=project_areas,
    )

    # Function to render projects list with custom HTML styling
    def render_proj(df: pd.DataFrame, title: str):
        st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
        styled_list = "<ul class='modern-list'>"
        for _, row in df.iterrows():
            styled_list += (
                f"<li class='skill-badge'>"
                f"<span style='color: #e3613e; font-size:10px; font-weight:bold'>"
                f"{row['area']}/{row['project']}</span><br/> {row['description']}</li><br/>"
            )
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
        st.divider()

    # If any project areas are selected, filter and render projects
    if sel_proj_areas:
        filtered_projects = df_prj[df_prj['area'].isin(sel_proj_areas)].reset_index(drop=True)
        render_proj(filtered_projects, title="Selected Projects")

    # ==================== Skills Section ====================
    st.markdown("<h2 class='hd1'> 💡 Skills</h2>", unsafe_allow_html=True)

    # Load skills CSV relative to this script location
    base_path = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_path, 'data/skills.csv')
    df_skills = pd.read_csv(csv_path, header=0, sep=';')

    # Remove rows where 'Area' is NaN
    df_skills.dropna(subset=['Area'], inplace=True)

    # Unique skill areas for selection
    areas = df_skills['Area'].unique().tolist()

    # Multiselect widget for skill areas
    selected_areas = st.multiselect(
        label='Pick skill areas:',
        options=areas,
    )

    # Function to render skills list with custom HTML styling
    def render_skills(df: pd.DataFrame, title: str):
        st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)
        styled_list = "<ul class='modern-list'>"
        for _, row in df.iterrows():
            styled_list += (
                f"<li class='skill-badge'>"
                f"<span style='color: #e3613e; font-size:10px; font-weight:bold'>"
                f"{row['Category']}</span> {row['Skill']}</li>"
            )
        styled_list += "</ul>"
        st.markdown(styled_list, unsafe_allow_html=True)
        st.divider()

    # If any skill areas are selected, filter and render skills; else show prompt
    if selected_areas:
        filtered_skills = df_skills[df_skills['Area'].isin(selected_areas)].reset_index(drop=True)
        render_skills(filtered_skills, title="Selected Skills")
    else:
        st.write("Please select at least one skill area to display.")
    #=============================================================================================
   # ==================== Education Section ====================
    st.markdown("<h2 class='hd1'> 📚 Education</h2>", unsafe_allow_html=True)

    def render_section(title, items):
        """
        Renders an education section with a title and a styled bullet list.

        Args:
            title (str): The heading/title of the section.
            items (list[str]): List of strings to display as list items.
        """
        # Section title with custom styling
        st.markdown(f"<h3 style='color: #e3613e'>{title}</h3>", unsafe_allow_html=True)

        # Build a styled unordered list from the items
        styled_list = "<ul class='modern-list'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"

        # Render the list as markdown with HTML enabled
        st.markdown(styled_list, unsafe_allow_html=True)

    # Define the content for each education subsection
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

    # Create three equal-width columns for side-by-side layout
    edu1, edu2, edu3 = st.columns(3)

    # Render each education subsection in its respective column
    with edu1:
        render_section("Certification", lst_cert)

    with edu2:
        render_section("University degree", lst_college)

    with edu3:
        render_section("Secondary school", lst_mid)



st.divider()

# Timeline
with st.container():
    # load data
    with open('data/example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500,)
    #st.write("Current dir contents:", os.listdir())
    #st.write("Current dir contents:", os.listdir())
st.divider()

    
       