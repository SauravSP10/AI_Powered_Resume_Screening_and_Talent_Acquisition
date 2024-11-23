import os
import pdfplumber
import spacy
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load NLP model
nlp = spacy.load("en_core_web_sm")

# Preprocess text to normalize content
def preprocess_text(text):
  doc = nlp(text)
  tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
  return " ".join(tokens)

# pdf to txt conversion / Extract text from PDF files
def extract_feature_from_pdf(file_path):
  with pdfplumber.open(file_path) as pdf:
    text = ""
    for page in pdf.pages:
      text += page.extract_text()
  return text
# docx to txt conversion / Extract text from DOCX files
def extract_feature_from_docx(file_path):
  with open(file_path, 'r') as file:
    text = file.read()
  return text

# Load resumes from a folder
def load_resumes(folder_path):
  resumes = []
  filenames = []
  for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if file.endswith(".pdf"):
      text = extract_feature_from_pdf(file_path)
    elif file.endswith(".docx"):
      text = extract_feature_from_docx(file_path)
    else:
      continue
    resumes.append(preprocess_text(text))
    filenames.append(file)
  return resumes, filenames

# write your job description / what skills required in candidats
job_description = "Python, Deep Learning, NLP, web developer, c "

# folder contaning resumes
folder_path="path/resume_folder" #Paste your resume folder path
resumes, filenames = load_resumes(folder_path)

# preprocessing job description
processed_job = preprocess_text(job_description)

# using vectorizer (TF-IDF)
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([processed_job] + resumes)

# calculating cosine similarity
similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])

# resume ranking by similarity
ranked_resumes = sorted(zip(filenames, similarity_scores[0]), key=lambda x: x[1], reverse=True)

# Print Output results
print("Top Resumes:")
for i, (filename, score) in enumerate(ranked_resumes[:10]):
    print(f"{i + 1}. {filename} - Similarity Score: {score:.2f}")
