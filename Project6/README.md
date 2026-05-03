# Resume vs Job Description Matcher 
Resume vs Job Description Matcher is an NLP-powered tool that analyzes a candidate's CV (PDF/DOCX) and compares it with a job description to calculate a match percentage. It extracts relevant skills from both documents using keyword matching, and also provides additional similarity metrics (Cosine and Semantic) for a comprehensive evaluation. The goal is to help recruiters or job seekers quickly assess the suitability of a resume for a specific role.

---

### Features:

- Upload CV in PDF or DOCX format.

- Paste any job description text.

- Automatic skill extraction using a customizable skill list.

- **Jaccard Similarity** for precise skill overlap percentage.

- **Cosine Similarity** (TF-IDF based) for overall text alignment.

- **Semantic Similarity** (Sentence-BERT) to capture contextual meaning.

- Highlights missing skills from the CV.

- Clean, interactive web interface built with Streamlit.

resume_matcher/
├── cv_selection_main.py   # Main Streamlit application
├── skills_list.py         # Customizable skill keywords list
├── requirements.txt       # Python dependencies
└── README.md            # Project documentation
-


### Technologies Used:
- Python, Streamlit, PyPDF2, python-docx, scikit-learn, Sentence-Transformers, pandas, regex.

### How to Run:

- Install dependencies: pip install -r requirements.txt

- Run the app: streamlit run cv_selection_main.py

- Open http://localhost:8501/ in your browser.
