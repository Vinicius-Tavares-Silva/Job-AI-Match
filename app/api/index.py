import os
import string
from io import BytesIO
from flask import Flask, request
from flask_cors import CORS, cross_origin

import requests
import google.generativeai as genai
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup


# Uso do secret do Colab
api_key = os.getenv('GEMINI_KEY')
genai.configure(api_key=api_key)

# Setup do modelo
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
system_instruction = "Voce é um recrutador especializado em triar curriculos, deve estruturar sua resposta sempre com 4 tópicos: Pontos Fortes, Pontos a Melhorar, Recomendações, Conclusão. Caso não identifique o curriculo ou os requisitos da vaga deve alertar o usuario"
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)


def file_reader(file):
  try:
    pdf = PdfReader(BytesIO(file.read()))
    content = ""
    for page in range(len(pdf.pages)):
      content += pdf.pages[page].extract_text()
    return content
  except Exception as e:
    return f"Erro: Arquivo fora do formato PDF"

def get_job_info(job_url):
  if len(job_url) == 0:
    return None
  try:
    html_text = requests.get(job_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    html_plain_text = soup.get_text().translate({ord(c): None for c in string.whitespace})
    return html_plain_text
  except Exception as e:
    print(f"Erro: Não foi possivel obter a vaga")
    return None

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return 'Hello World!'

@app.route('/items/<int:count>', methods=['GET'])
@cross_origin()
def items(count):
    return f'{count}'

@app.route('/job-match', methods=['POST'])
@cross_origin()
def job_match():
  request_data = request.get_json()
  resume = request_data['resume']
  job_info = request_data['job_url']
  recruiter = model.start_chat(history=[])
  recruiter.send_message("Curriculo: " + resume)
  response = recruiter.send_message("Com base no curriculo enviado, "
  "quais são os pontos fortes e quais os pontos a se melhorar em relação a vaga a seguir: " 
  + job_info)
  return response.text

@app.route('/read_resume', methods=['POST'])
@cross_origin()
def read_resume():
  file = request.files['file']
  file_content = file_reader(file)
  return file_content

if __name__ == '__main__':
    app.run()
