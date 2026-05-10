
# """
# Main Streamlit frontend.
# """

# import shutil
# import sqlite3
# import sys

# from pathlib import Path

# import streamlit as st


# # Add project root to Python path
# ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# sys.path.append(str(ROOT_DIR))


# from app.extractor.extractor import PPTExtractor


# # Folders
# RAW_FOLDER = ROOT_DIR / "templates/raw"

# RAW_FOLDER.mkdir(
#     parents=True,
#     exist_ok=True
# )


# # Database
# DB_PATH = ROOT_DIR / "ppt_engine.db"


# st.set_page_config(
#     page_title="Chat PPT",
#     layout="wide"
# )

# st.title("ChaT_PPT")


# # -----------------------------------
# # Knowledge Base Reset
# # -----------------------------------

# st.sidebar.header("Knowledge Base")


# wipe_db = st.sidebar.toggle(
#     "Start Fresh Knowledge Base"
# )


# if wipe_db:

#     if DB_PATH.exists():

#         DB_PATH.unlink()

#         st.sidebar.success(
#             "Old database deleted."
#         )

#     # Clear raw folder
#     if RAW_FOLDER.exists():

#         shutil.rmtree(RAW_FOLDER)

#         RAW_FOLDER.mkdir(
#             parents=True,
#             exist_ok=True
#         )

#     st.sidebar.success(
#         "Knowledge base reset completed."
#     )


# # -----------------------------------
# # Template Metadata
# # -----------------------------------

# st.header("Upload Template")

# template_category = st.selectbox(
#     "Template Category",
#     [
#         "Timeline",
#         "Roadmap",
#         "KPI Dashboard",
#         "Org Chart",
#         "Process Flow",
#         "SWOT",
#         "Comparison",
#         "Team Structure",
#         "Business Strategy",
#         "Financial",
#         "Marketing",
#         "Technology",
#         "Project Management",
#         "Sales",
#         "Infographic"
#     ]
# )


# template_usage = st.text_input(
#     "Template Purpose / Context",
#     placeholder=(
#         "Example: "
#         "Quarterly sales review deck "
#         "for enterprise clients"
#     )
# )


# uploaded_file = st.file_uploader(
#     "Upload PPTX Template",
#     type=["pptx"]
# )


# # -----------------------------------
# # Extraction
# # -----------------------------------

# if uploaded_file:

#     save_path = RAW_FOLDER / uploaded_file.name

#     with open(save_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.success(
#         f"Template saved: {uploaded_file.name}"
#     )

#     st.info(
#         f"Category: {template_category}"
#     )

#     st.info(
#         f"Purpose: {template_usage}"
#     )

#     if st.button("Start Extraction"):

#         progress_bar = st.progress(0)

#         status_text = st.empty()

#         extractor = PPTExtractor(
#             str(save_path)
#         )

#         extracted_data = extractor.extract(
#             progress_bar=progress_bar,
#             status_text=status_text
#         )

#         progress_bar.progress(100)

#         status_text.success(
#             "Extraction completed successfully."
#         )

#         st.success(
#             (
#                 f"Slides Extracted: "
#                 f"{len(extracted_data)}"
#             )
#         )

#         st.json(
#             extracted_data[:1]
#         )

"""
Main Streamlit frontend.
"""

import shutil
import sys

from pathlib import Path

import streamlit as st


# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(ROOT_DIR))


from app.extractor.extractor import PPTExtractor


# =========================================================
# FOLDERS
# =========================================================

RAW_FOLDER = ROOT_DIR / "templates/raw"

RAW_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


# =========================================================
# DATABASE
# =========================================================

DB_PATH = ROOT_DIR / "ppt_engine.db"


# =========================================================
# STREAMLIT CONFIG
# =========================================================

st.set_page_config(
    page_title="Chat PPT",
    layout="wide"
)

st.title("ChaT_PPT")


# =========================================================
# TABS
# =========================================================

tab1, tab2 = st.tabs(
    [
        "Knowledge Base Setup",
        "PPT Generation Studio"
    ]
)


# =========================================================
# TAB 1
# KNOWLEDGE BASE SETUP
# =========================================================

with tab1:

    st.header("Knowledge Base Management")

    # -----------------------------------
    # Knowledge Base Reset
    # -----------------------------------

    wipe_db = st.toggle(
        "Start Fresh Knowledge Base"
    )


    if wipe_db:

        if DB_PATH.exists():

            DB_PATH.unlink()

            st.success(
                "Old database deleted."
            )

        # Remove raw templates
        if RAW_FOLDER.exists():

            shutil.rmtree(RAW_FOLDER)

            RAW_FOLDER.mkdir(
                parents=True,
                exist_ok=True
            )

        st.success(
            "Knowledge base reset completed."
        )

    # -----------------------------------
    # Template Upload
    # -----------------------------------

    st.header("Upload Template")


    template_category = st.selectbox(
        "Template Category",
        [
            "Timeline",
            "Roadmap",
            "KPI Dashboard",
            "Org Chart",
            "Process Flow",
            "SWOT",
            "Comparison",
            "Team Structure",
            "Business Strategy",
            "Financial",
            "Marketing",
            "Technology",
            "Project Management",
            "Sales",
            "Infographic"
        ]
    )


    template_usage = st.text_input(
        "Template Purpose / Context",
        placeholder=(
            "Example: "
            "Quarterly sales review deck "
            "for enterprise clients"
        )
    )


    uploaded_file = st.file_uploader(
        "Upload PPTX Template",
        type=["pptx"]
    )


    # -----------------------------------
    # Extraction
    # -----------------------------------

    if uploaded_file:

        save_path = RAW_FOLDER / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(
            f"Template saved: {uploaded_file.name}"
        )

        st.info(
            f"Category: {template_category}"
        )

        st.info(
            f"Purpose: {template_usage}"
        )

        if st.button("Start Extraction"):

            progress_bar = st.progress(0)

            status_text = st.empty()

            extractor = PPTExtractor(
                str(save_path)
            )

            extracted_data = extractor.extract(
                progress_bar=progress_bar,
                status_text=status_text
            )

            progress_bar.progress(100)

            status_text.success(
                "Extraction completed successfully."
            )

            st.success(
                (
                    f"Slides Extracted: "
                    f"{len(extracted_data)}"
                )
            )

            st.json(
                extracted_data[:1]
            )


# =========================================================
# TAB 2
# PPT GENERATION STUDIO
# =========================================================

with tab2:

    st.header("PPT Generation Studio")

    st.info(
        (
            "This section will handle:\n\n"
            "- Structured data input\n"
            "- Chat with PPT engine\n"
            "- AI-assisted slide generation\n"
            "- Editable PPT creation\n"
            "- Layout selection\n"
            "- Chart recommendations\n"
            "- Final PPT export"
        )
    )

    user_prompt = st.text_area(
        "Describe Your Presentation",
        height=200,
        placeholder=(
            "Explain what type of presentation "
            "you want to generate"
        )
    )

    if st.button("Generate Presentation"):

        st.warning(
            (
                "Presentation generation pipeline "
                "is not implemented yet."
            )
        )