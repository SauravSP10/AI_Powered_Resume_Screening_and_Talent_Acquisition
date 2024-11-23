### **README.md**

# **AI-Powered Resume Screening and Talent Acquisition**

This project provides an **AI-powered solution** for automating resume screening and ranking based on their relevance to a specific job description. By leveraging **Natural Language Processing (NLP)** and machine learning techniques, the system enables faster and more efficient talent acquisition processes.

---

## **Features**

- **Automated Resume Ranking**: Ranks resumes by their similarity to a job description.
- **Multi-Format Support**: Processes resumes in `.pdf`, `.docx`, and `.txt` formats.
- **Customizable Output**: Displays the top N resumes with similarity scores and their content.
- **Efficient Text Analysis**: Uses TF-IDF vectorization and cosine similarity for accurate matching.
- **Modular Design**: Easy to integrate into larger HR or ATS systems.

---

## **Installation**

### **Requirements**
- **Python** 3.8 or higher
- Libraries:
  - `scikit-learn` (for text analysis)
  - `pdfplumber` (for PDF parsing)
  - `python-docx` (for Word document parsing)
  - `spacy` (for advanced text preprocessing)

Install dependencies with:
```bash
pip install scikit-learn pdfplumber python-docx spacy
python -m spacy download en_core_web_sm
```

---

## **File Structure**

```
AI_Powered_Resume_Screening_and_Talent_Acquisition/
├── resumes_folder/         # Directory containing resumes
│   ├── resume1.pdf
│   ├── resume2.docx
│   └── ...
├── ai_resume_screening.py     # Main script for screening
├── README.md               # Documentation
└── requirements.txt        # List of dependencies
```

---

## **Example Output**

```plaintext
Job Description: Looking for a data scientist with skills in Python, machine learning, and big data.

Top 10 Most Relevant Resumes:

Rank 1: resume1.pdf - Similarity Score: 0.91
Resume: Experienced in Python and machine learning for data analysis.

Rank 2: resume5.docx - Similarity Score: 0.88
Resume: Data scientist with experience in Python, SQL, and machine learning.

Rank 3: resume3.pdf - Similarity Score: 0.85
Resume: AI expert with deep learning and TensorFlow skills.
...
```

---

## **Customization**

### **Extract Specific Details**
- Enhance the script to extract details like **skills**, **experience**, or **education** using Named Entity Recognition (NER) from `spaCy`.

### **Add OCR for Scanned PDFs**
- Use `pytesseract` to process scanned resumes.

### **Web Application**
- Convert the script into a web interface using `Flask` or `Streamlit`.

---

## **Future Enhancements**
- **Integration with ATS**: Connect the script with Applicant Tracking Systems for seamless processing.
- **Database Support**: Store and retrieve resumes and results from a database.
- **Advanced Filtering**: Incorporate domain-specific keywords and filters for more precise matching.

---

## **Contributing**

Contributions are welcome! If you'd like to improve this project, follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push them.
4. Submit a pull request.

---

## **License**

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute this software as per the terms of the license.

---

## **Contact**

For any inquiries or feedback, feel free to reach out:
- **Email**: your-email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/your-username)

---

Enjoy automating your talent acquisition process! 🎉
