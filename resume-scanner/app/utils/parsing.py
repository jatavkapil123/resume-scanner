import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume(resume_text):
    doc = nlp(resume_text)
    parsed_data = {
        "name": "Extracted Name",
        "contact_info": "Extracted Contact Info",
        "education": "Extracted Education",
        "experience": "Extracted Experience",
        "skills": "Extracted Skills"
    }
    return parsed_data

