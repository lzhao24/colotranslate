import pandas as pd
from deep_translator import GoogleTranslator
from openai import OpenAI
api_key = "INSERT_KEY"
client = OpenAI(api_key=api_key)


def simplify_colonoscopy_report(report_text):
    """Simplify the colonoscopy report into a patient-friendly format."""
    prompt = f"""Please simplify the following colonoscopy report into a patient-friendly format. Use clear, everyday language and avoid medical jargon. Follow the structured template below to maintain consistency across all reports. Retain all critical details and findings, and provide explanations for any necessary medical terms or concepts. Here is the colonoscopy report:
{report_text}
Simplified Colonoscopy Report Template:
1. Introduction:
Briefly introduce the purpose of the report and the type of study performed. (e.g., "This report summarizes the findings from your recent [type of procedure].")
2. Key Findings:
Explain in detail the findings of the report for a patient to easily understand; do not add your own interpretation of the results; make sure the information is accurate to the findings in the report.
3. Impression:
Summarize the overall impression or diagnosis in an easy-to-understand manner. (e.g., "The spot in your [organ] is likely a benign growth called a [medical term].")
"""
    try:
        chat_completion = client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": prompt}],
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error simplifying report: {e}"
    
    
def translate_text_google(text, target_language):
    """Translate the text using GoogleTranslator."""
    try:
        translator = GoogleTranslator(source="auto", target=target_language)
        return translator.translate(text)
    except Exception as e:
        return f"Error translating with Google: {e}"
    
    
def translate_text_gpt(text, target_language):
    """Translate the text using GPT."""
    prompt = f"""Translate the following text into {target_language}:
{text}
"""
    try:
        chat_completion = client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": prompt}],
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error translating with GPT: {e}"
    
    
def process_and_translate(report_text, target_language):
    """Simplify the report once and then translate it using GPT and Google."""
    try:
        simplified_report = simplify_colonoscopy_report(report_text)
        translated_gpt = translate_text_gpt(simplified_report, target_language)
        translated_google = translate_text_google(simplified_report, target_language)
        return simplified_report, translated_gpt, translated_google
    except Exception as e:
        return f"Error: {e}", f"Error: {e}", f"Error: {e}"
    
    
target_languages = ['es', 'ar', 'zh-CN']  # REPLACE
input_file = pd.read_csv('INPUT_FILE_NAME.csv') # REPLACE, ensure input file is in same path as this script

for lang in target_languages:
    results = input_file['Report'].apply(lambda x: process_and_translate(x, lang))
    input_file['Simplified'] = results.apply(lambda x: x[0])
    input_file['Translated o1'] = results.apply(lambda x: x[1])
    input_file['Translated Google'] = results.apply(lambda x: x[2])
    input_file.to_csv(f"OUTPUT_FILE_NAME_{lang}.csv", index=False) # REPLACE FILE NAME
    print("Processing complete.")
