import streamlit as st
import pandas as pd
import os
from io import BytesIO
from dotenv import load_dotenv
from google import genai

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Excel Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS - MODERN DASHBOARD
# =====================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #f4f7fb;
    }

    [data-testid="stHeader"] {
        background: rgba(244, 247, 251, 0.9);
    }

    [data-testid="stSidebar"] {
        background: #101a32;
    }

    [data-testid="stSidebar"] * {
        color: #eef3ff;
    }

    .hero {
        background: linear-gradient(125deg, #14213d, #2457a7);
        padding: 32px;
        border-radius: 22px;
        margin-bottom: 24px;
        color: white;
        box-shadow: 0 10px 30px rgba(25, 57, 110, 0.15);
    }

    .hero h1 {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin: 0 0 10px 0;
    }

    .hero p {
        color: #dbeafe;
        font-size: 15px;
        margin: 0;
        line-height: 1.7;
    }

    .section-heading {
        color: #172744;
        font-size: 21px;
        font-weight: 750;
        margin: 12px 0 14px 0;
    }

    .small-label {
        font-size: 12px;
        color: #71819a;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .upload-card {
        background: white;
        border: 1px dashed #8ca9d5;
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 18px;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #e5eaf3;
        padding: 18px 20px;
        border-radius: 16px;
        box-shadow: 0 4px 14px rgba(20, 40, 80, 0.035);
    }

    [data-testid="stMetricLabel"] {
        color: #64748b;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #1d4ed8;
        font-weight: 800;
    }

    [data-testid="stTabs"] button {
        font-weight: 600;
    }

    .answer-banner {
        background: #eaf2ff;
        border-left: 4px solid #2563eb;
        padding: 14px 18px;
        border-radius: 8px;
        color: #193b73;
        margin: 10px 0 18px 0;
    }

    .tip-card {
        background: #1b2946;
        padding: 16px;
        border-radius: 14px;
        margin: 12px 0;
        color: #e7efff;
        font-size: 13px;
        line-height: 1.7;
    }

    .tip-card strong {
        color: white;
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #2563eb, #3978ed);
        border: none;
        border-radius: 10px;
        color: white;
        font-weight: 700;
        min-height: 44px;
        transition: 0.2s;
    }

    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(90deg, #1d4ed8, #2563eb);
        box-shadow: 0 5px 14px rgba(37, 99, 235, 0.2);
    }

    div.stButton > button {
        border-radius: 9px;
        font-weight: 600;
    }

    [data-testid="stFileUploader"] {
        background: white;
        border-radius: 12px;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #e5eaf3;
        border-radius: 12px;
        overflow: hidden;
    }

    .footer {
        color: #8794a9;
        text-align: center;
        font-size: 12px;
        padding: 25px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD GEMINI API
# =====================================================

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


@st.cache_resource
def get_gemini_client(api_key):
    return genai.Client(api_key=api_key)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def select_example(question):
    st.session_state["question"] = question


def format_number(value):
    return f"{value:,}"


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    st.markdown("## 📊 Excel AI")
    st.caption("YOUR PERSONAL DATA ANALYST")

    st.divider()

    st.markdown("### ✨ What you can do")
    st.markdown("""
    - 📁 Upload Excel workbooks
    - 📄 Explore individual sheets
    - 📊 View dataset statistics
    - 🔍 Find records and values
    - 🤖 Ask questions using AI
    """)

    st.divider()

    st.markdown("### 💡 Example questions")

    st.markdown("""
    - Who has the highest marks?
    - Calculate the average.
    - Find missing values.
    - Show the top 5 records.
    - Compare departments.
    """)

    st.divider()

    if API_KEY:
        st.success("Gemini API key detected")
    else:
        st.warning("Gemini API key not configured")

    st.caption("AI Excel Agent · Streamlit")


# =====================================================
# HERO HEADER
# =====================================================

st.markdown("""
<div class="hero">
    <div class="small-label" style="color:#bfdbfe;">
        SMART DATA ANALYSIS WORKSPACE
    </div>
    <h1>📊 AI Excel Agent</h1>
    <p>
        Turn your spreadsheets into insights.
        Upload your Excel file, explore your data,
        and ask questions in simple English.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# UPLOAD SECTION
# =====================================================

st.markdown(
    '<div class="section-heading">📁 Upload your workbook</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose an Excel file (.xlsx or .xls)",
    type=["xlsx", "xls"],
    help="Upload a workbook to preview its sheets and analyze its data."
)

if uploaded_file is None:
    st.info("👆 Upload an Excel workbook to get started.")

    st.markdown("### Explore what your AI analyst can answer")

    example_columns = st.columns(3)

    with example_columns[0]:
        with st.container(border=True):
            st.markdown("### 🔎 Find insights")
            st.write("Find the highest, lowest, or average values.")

    with example_columns[1]:
        with st.container(border=True):
            st.markdown("### 📈 Explore data")
            st.write("Inspect columns, missing values, and statistics.")

    with example_columns[2]:
        with st.container(border=True):
            st.markdown("### 🤖 Ask questions")
            st.write("Ask questions about the records in your workbook.")

    st.markdown(
        '<div class="footer">AI Excel Agent · Your data, made easier to understand.</div>',
        unsafe_allow_html=True
    )
    st.stop()

# =====================================================
# READ WORKBOOK
# =====================================================

try:
    file_bytes = uploaded_file.getvalue()
    excel_file = pd.ExcelFile(BytesIO(file_bytes))
    sheets = excel_file.sheet_names

    if not sheets:
        st.error("This workbook does not contain any worksheets.")
        st.stop()

    selected_sheet = st.selectbox(
        "📄 Select worksheet",
        sheets,
        key="selected_sheet"
    )

    df = pd.read_excel(
        BytesIO(file_bytes),
        sheet_name=selected_sheet
    )

    # Remove spaces from column names only for checking emptiness;
    # original column names are retained.
    if df.empty and len(df.columns) == 0:
        st.warning("This worksheet has no data.")
        st.stop()

except Exception as e:
    st.error(f"Could not read this Excel file: {e}")
    st.stop()

# =====================================================
# WORKBOOK INFORMATION
# =====================================================

st.markdown(
    '<div class="section-heading">📌 Workbook overview</div>',
    unsafe_allow_html=True
)

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Total rows", format_number(len(df)))

with metric2:
    st.metric("Total columns", format_number(len(df.columns)))

with metric3:
    st.metric(
        "Missing cells",
        format_number(int(df.isna().sum().sum()))
    )

with metric4:
    st.metric(
        "Duplicate rows",
        format_number(int(df.duplicated().sum()))
    )

st.caption(
    f"📄 Current worksheet: {selected_sheet} · "
    f"📁 File: {uploaded_file.name}"
)

st.divider()

# =====================================================
# TABS
# =====================================================

tab_data, tab_insights, tab_ai = st.tabs([
    "📋 Data Preview",
    "📈 Column Insights",
    "🤖 AI Analyst"
])

# =====================================================
# TAB 1: DATA PREVIEW
# =====================================================

with tab_data:
    st.markdown("### Your spreadsheet")
    st.write("Review the records loaded from your selected worksheet.")

    if df.empty:
        st.warning("This worksheet has no data rows.")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            height=390,
            hide_index=True
        )

    with st.expander("View column names and data types"):
        column_info = pd.DataFrame({
            "Column": df.columns.astype(str),
            "Data type": [str(dtype) for dtype in df.dtypes],
            "Missing values": df.isna().sum().values,
            "Unique values": [
                df[col].nunique() for col in df.columns
            ]
        })

        st.dataframe(
            column_info,
            use_container_width=True,
            hide_index=True
        )

# =====================================================
# TAB 2: COLUMN INSIGHTS
# =====================================================

with tab_insights:
    st.markdown("### Understand your data")

    if df.empty or len(df.columns) == 0:
        st.info("No data is available for analysis.")
    else:
        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        insight_left, insight_right = st.columns(2)

        with insight_left:
            st.markdown("#### Missing values by column")

            missing_data = df.isna().sum()
            missing_data = missing_data[missing_data > 0]

            if not missing_data.empty:
                st.bar_chart(missing_data)
            else:
                st.success("No missing values found.")

        with insight_right:
            st.markdown("#### Numerical column distribution")

            if numeric_columns:
                selected_numeric = st.selectbox(
                    "Choose a numerical column",
                    numeric_columns,
                    key="numeric_column"
                )

                chart_data = df[selected_numeric].dropna()

                if not chart_data.empty:
                    st.bar_chart(
                        chart_data.reset_index(drop=True),
                        height=260
                    )
                else:
                    st.info("This column contains no numerical values.")
            else:
                st.info("No numerical columns were found.")

        st.markdown("#### Statistical summary")

        if numeric_columns:
            st.dataframe(
                df[numeric_columns].describe().T,
                use_container_width=True
            )
        else:
            st.info("No numerical statistics are available.")

# =====================================================
# TAB 3: AI ANALYST
# =====================================================

with tab_ai:
    st.markdown("### 🤖 Ask questions about your data")

    st.write(
        "Type a question in plain English. "
        "The AI will use the selected worksheet to prepare an answer."
    )

    if not API_KEY:
        st.error(
            "GEMINI_API_KEY was not found. Add it to your .env file "
            "before using AI analysis."
        )
    else:
        question = st.text_input(
            "Your question",
            key="question",
            placeholder="Example: Which student got the highest marks?"
        )

        st.markdown("#### Try an example question")

        examples = [
            "How many rows and columns are there?",
            "Give me a summary of this dataset.",
            "Which record has the highest numerical value?",
            "Show the top 5 records.",
            "How many missing values are there?",
            "Calculate the average of numerical columns."
        ]

        for start in range(0, len(examples), 2):
            example_cols = st.columns(2)

            for offset, col in enumerate(example_cols):
                index = start + offset

                if index < len(examples):
                    with col:
                        st.button(
                            examples[index],
                            key=f"example_{index}",
                            use_container_width=True,
                            on_click=select_example,
                            args=(examples[index],)
                        )

        analyze = st.button(
            "🔍 Analyze my data",
            type="primary",
            use_container_width=True
        )

        if analyze:
            if not question.strip():
                st.warning("Please enter a question or select an example.")
            elif df.empty:
                st.warning("The selected worksheet contains no data rows.")
            else:
                try:
                    client = get_gemini_client(API_KEY)

                    with st.spinner(
                        "🤖 Analyzing your worksheet... Please wait."
                    ):
                        data_text = df.to_string(index=False)

                        try:
                            numerical_summary = df.describe(
                                include="all"
                            ).to_string()
                        except Exception:
                            numerical_summary = "Not available."

                        prompt = f"""
You are an accurate Excel data analyst.

WORKSHEET:
{selected_sheet}

NUMBER OF ROWS:
{len(df)}

NUMBER OF COLUMNS:
{len(df.columns)}

COLUMN NAMES:
{list(df.columns)}

DATA TYPES:
{df.dtypes.to_dict()}

EXCEL DATA:
{data_text}

STATISTICAL SUMMARY:
{numerical_summary}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer using only the supplied worksheet data.
2. Never invent records, names, values, or facts.
3. Calculate carefully and explain the result simply.
4. For highest or lowest values, identify the correct record.
5. For averages, totals, and counts, use the actual data.
6. For filters, show matching records when practical.
7. For top N questions, return the correct records in order.
8. Handle missing values carefully and explain exclusions.
9. If the answer cannot be determined from the data, say so.
10. Use a Markdown table when useful.
11. Do not claim to have analyzed rows or columns that are absent.
12. Keep the answer clear, useful, and concise.
"""

                        response = client.models.generate_content(
                            model="gemini-3.5-flash-lite",
                            contents=prompt
                        )

                        answer = response.text

                    st.markdown("---")
                    st.markdown("### 💡 AI Analysis Result")

                    if answer:
                        st.markdown(
                            '<div class="answer-banner">'
                            'Analysis completed. Review the answer below.'
                            '</div>',
                            unsafe_allow_html=True
                        )
                        st.markdown(answer)
                    else:
                        st.warning(
                            "The AI returned an empty response. "
                            "Please try again."
                        )

                except Exception as e:
                    st.error(
                        f"AI analysis failed: {e}"
                    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    '📊 AI Excel Agent · Intelligent spreadsheet analysis'
    '</div>',
    unsafe_allow_html=True
)