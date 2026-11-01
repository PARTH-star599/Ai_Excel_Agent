# 📊 AI Excel Agent – Intelligent Spreadsheet Analysis

An AI-powered Excel analysis application built using **Python, Streamlit, Pandas, and Google Gemini API**.

AI Excel Agent helps users analyze Excel spreadsheets, understand datasets, discover insights, and get answers to data-related questions using simple natural language. No need to write complex Excel formulas or Python code!

## 🚀 Features

- **Excel File Upload:** Upload Excel workbooks in `.xlsx` and `.xls` formats.
- **Multiple Worksheets:** Select and analyze individual sheets from a workbook.
- **Data Preview:** View spreadsheet records in an interactive table.
- **Dataset Overview:** Get total rows, columns, missing cells, and duplicate row counts.
- **Column Insights:** Explore column names, data types, unique values, and missing values.
- **Statistical Analysis:** View numerical summaries such as mean, minimum, maximum, and standard deviation.
- **Data Visualization:** Visualize missing values and numerical column distributions.
- **AI-Powered Analysis:** Ask questions about your Excel data using natural language.
- **Smart Data Insights:** Find highest values, calculate averages, identify missing values, and retrieve top records.
- **Modern Dashboard:** Clean and responsive interface built with Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Excel data processing and analysis |
| Google Gemini API | AI-powered data analysis |
| Google Gen AI SDK | Gemini API integration |
| Python-dotenv | Secure API key configuration |
| OpenPyXL | Excel workbook support |

## 📂 Project Structure

```text
Ai_Excel_Agent/
│
├── app.py              # Main Streamlit application
├── excel_tools.py      # Excel data handling functions
├── create_excel.py     # Sample Excel file generator
├── requirements.txt    # Project dependencies
├── .env                # Gemini API key (not uploaded)
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/PARTH-star599/Ai_Excel_Agent.git
```

### 2. Open the Project Folder

```bash
cd Ai_Excel_Agent
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements.txt file, install:

```bash
pip install streamlit pandas python-dotenv google-genai openpyxl xlrd
```

### 5. Configure Gemini API Key

Get your API key from Google AI Studio:

https://aistudio.google.com/apikey

Create a file named `.env` in the main project folder.

Add the following:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Important:** Replace `your_gemini_api_key_here` with your actual Gemini API key.

Never upload your API key to GitHub or share it publicly.

### 6. Run the Application

Execute the following command:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Default local address:

```text
http://localhost:8501
```

## 💡 How to Use

1. Start the AI Excel Agent application.
2. Upload an Excel workbook (`.xlsx` or `.xls`).
3. Select the worksheet you want to analyze.
4. Explore the Data Preview section.
5. Open Column Insights to view statistics and visualizations.
6. Navigate to the AI Analyst section.
7. Enter your question in simple English.
8. Click **Analyze My Data**.
9. View the AI-generated analysis and insights.

## 🤖 Example Questions

You can ask questions such as:

- Which student scored the highest marks?
- Calculate the average marks.
- Show the top 5 records.
- How many missing values are present?
- Give me a summary of this dataset.
- Which department has the highest performance?
- Find the lowest numerical value.
- How many rows and columns are present?

## 🔐 Security

- Gemini API keys are stored in environment variables using a `.env` file.
- API credentials should never be committed to GitHub.
- Uploaded Excel data is provided to the Gemini API when AI analysis is requested.
- Avoid uploading confidential or sensitive spreadsheets.

## 🔮 Future Improvements

- Support for CSV and additional data formats.
- Advanced interactive charts and graphs.
- Automatic data cleaning and preprocessing.
- Excel formula generation using AI.
- Download AI-generated reports in PDF format.
- Data filtering and sorting through natural language.
- Advanced predictive analytics and forecasting.
- Deployment with a public web application link.

## 👨‍💻 Developer

**Parth Sarnaik**

Computer Science and Engineering Student

GitHub: [PARTH-star599](https://github.com/PARTH-star599)

Project Repository: [AI Excel Agent](https://github.com/PARTH-star599/Ai_Excel_Agent)

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

Suggestions, feedback, and contributions are always welcome!

---

**Built with ❤️ using Python, Streamlit, Pandas, and Google Gemini AI.**
