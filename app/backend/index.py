from flask import Flask, request
from flask_cors import CORS, cross_origin

# Importação dos módulos
import hashlib
import string
import requests
import textwrap
import pdfx
from pathlib import Path
from bs4 import BeautifulSoup
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai

# Uso do secret do Colab
# api_key = userdata.get('API_KEY')
genai.configure(api_key='AIzaSyBIkD6CoMYqw-lncMbHMa-t9dbxO69WzIY')

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


# def file_reader(file_name):
#   try:
#     pdf = pdfx.PDFx(file_name)
#     return pdf.get_text()
#   except Exception as e:
#     print(f"Erro: Arquivo '{file_name}' fora do formato PDF")

# def file_upload():
#   try:
#     uploaded = files.upload()
#     return list(uploaded.keys())[0]
#   except Exception as e:
#     print(f"Erro: Arquivo inválido")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

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




# file_name = file_upload()
# if file_name != None:
#   file_content = file_reader(file_name)
#   if file_content != None:
#     recruiter = model.start_chat(history=[])
#     recruiter.send_message("Curriculo: " + file_content)

#     job_info = 'start'
#     while job_info != None:
#       prompt = input("URL: ")
#       job_info = get_job_info(prompt)
#       if job_info != None:
#         response = recruiter.send_message("Com base no curriculo enviado, quais são os pontos fortes e quais os pontos a se melhorar em relação a vaga a seguir: " + job_info)
#         display(to_markdown(f'{response.text}'))




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
  resume = request_data['cv']
  job_info = request_data['job']
  recruiter = model.start_chat(history=[])
  recruiter.send_message("Curriculo: " + resume)
  response = recruiter.send_message("Com base no curriculo enviado, quais são os pontos fortes e quais os pontos a se melhorar em relação a vaga a seguir: " + job_info)
  return response.text

if __name__ == '__main__':
    app.run()
