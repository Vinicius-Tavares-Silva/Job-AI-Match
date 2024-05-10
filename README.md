# Job AI Match: Análise de Currículos com Poder de IA
Repositório para o desafio da Imersão Inteligência Artificial 2ª Edição


Job AI Match é uma aplicação inovadora que utiliza o poder do modelo de linguagem Gemini para analisar currículos e fornecer feedback valioso sobre a adequação de um candidato a uma vaga de emprego específica.

**Funcionalidades:**

*   **Leitura de PDF:** Extrai o texto de um currículo em formato PDF.
*   **Upload de Arquivo:** Permite que o usuário faça upload do currículo.
*   **Web Scraping:** Obtém informações da vaga de emprego a partir de um link fornecido pelo usuário.
*   **Análise de Currículo:** Envia o currículo e as informações da vaga para o modelo de IA do Google Generative AI.
*   **Feedback:** O modelo de IA gera um feedback estruturado com base nos seguintes tópicos:
    *   **Pontos Fortes:** Habilidades e experiências do candidato que são relevantes para a vaga.
    *   **Pontos a Melhorar:** Áreas onde o candidato pode se desenvolver para se tornar um candidato mais forte.
    *   **Recomendações:** Sugestões sobre como o candidato pode melhorar seu currículo ou se preparar para a entrevista.
    *   **Conclusão:** Uma avaliação geral da adequação do candidato à vaga.
    
**Como usar:**
1.  **Configurar a API:** Obtenha uma chave de API do Google Generative AI e defina-a na variável `api_key`.
2.  **Executar o código:** Execute o script Python no Google Colab ou em um ambiente Python local com as bibliotecas necessárias instaladas.
3.  **Fazer upload do currículo:** Siga as instruções para fazer upload do seu currículo em formato PDF.
4.  **Inserir o link da vaga:** Cole o link da vaga de emprego que você deseja se candidatar.
5.  **Obter feedback:** O modelo de IA irá analisar seu currículo e fornecer feedback estruturado.

Para obter o link da vaga selecione a opção de "Copiar link" no compartilhamento da vaga, exemplo:

![alt text](https://github.com/Vinicius-Tavares-Silva/Job-AI-Match/blob/main/images/linkedId-share.png)
![alt text](https://github.com/Vinicius-Tavares-Silva/Job-AI-Match/blob/main/images/gupy-share.png)

**Requisitos:**

*   Python 3.x
*   Bibliotecas: `hashlib`, `string`, `requests`, `textwrap`, `pdfx`, `pathlib`, `bs4`, `IPython`, `google.colab`, `google.generativeai`

**Observações:**

*   O modelo de IA foi treinado para analisar currículos e vagas de emprego na área de tecnologia.
*   A qualidade do feedback depende da qualidade do currículo e das informações da vaga.
*   Certifique-se de que o link da vaga seja válido e contenha informações suficientes sobre a posição.

**Exemplos de links de vagas:**

*   LinkedIn
*   Gupy
*   Indeed
*   Glassdoor

**Limitações:**

*   O modelo de IA pode não ser capaz de entender todos os tipos de currículos e vagas de emprego.
*   O feedback gerado pelo modelo de IA é apenas uma sugestão e não deve ser considerado como uma avaliação definitiva.\n\n**Isenção de responsabilidade:**\n\nEste código é fornecido apenas para fins educacionais e informativos. O autor não se responsabiliza por quaisquer danos ou perdas resultantes do uso deste código.
