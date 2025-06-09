# colotranslate
*derivative of mazaneesh/RadTranslate*

ColoTranslate is a Python-based tool designed to simplify colonoscopy reports using GPT o1-preview and translate them into multiple languages using both GPT o1-preview and Google Translate.

## Features
- **Simplification of Medical Reports**: Converts colonoscopy reports into patient-friendly summaries using o1-preview.
- **Translation of Medical Reports**: Translates simplified reports into multiple languages using GPT o1-preview and Google Translate.
- **Batch Processing**: Processes multiple reports in an input CSV file and saves the simplified and translated outputs in CSV format.

## Requirements
- Python 3.x
- deep_translator: For translating text using Google Translate.
- openai: To interact with the GPT o1-preview model.

Install the dependencies with:
pip install deep-translator openai

## Setup
- git clone https://github.com/lzhao24/colotranslate
- In the script, replace the placeholder with your OpenAI API key: api_key = "INSERT_KEY"
- Prepare input CSV file: Ensure that column headings are "Report", "Simplified", "Translated o1", and "Translated Google"
- Run the script: You can specify the target languages for translation (using ISO language codes). By default, the supported languages are: Spanish (es), Chinese Simplified (zh-CN), and Arabic (ar). Run one language at a time.

## Output Files
After processing, the script generates CSV files with all columns of the input CSV file filled in 

Each file contains:
- The original report
- The simplified report
- The o1-preview translated report
- The Google Translate translated report

## Customization
Target Languages: Modify the target_languages list in the script to change the languages for translation.
