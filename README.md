# Recomendador Personalizado de Estudos

## Visão Geral do Projeto

Este repositório contém o projeto "Recomendador Personalizado de Estudos", que visa desenvolver um sistema capaz de adaptar trilhas de aprendizagem ao desempenho individual do aluno. A motivação para este trabalho surge da dificuldade em identificar lacunas de conhecimento e priorizar conteúdos e revisões de forma estratégica em ambientes educacionais.

Com o crescente volume de dados gerados por plataformas de ensino online e gamificadas, há um potencial significativo para transformar esses dados em recomendações de estudo personalizadas. O problema central abordado é a ausência de um mecanismo que acompanhe continuamente o progresso do estudante e ajuste as recomendações conforme sua evolução. Espera-se que a solução proposta promova maior eficiência no estudo, reduza defasagens de aprendizagem e apoie decisões pedagógicas baseadas em dados, otimizando o tempo de estudo e aumentando o aproveitamento educacional.

## Objetivo do Projeto

O objetivo principal deste projeto é desenvolver uma solução baseada em Inteligência Artificial capaz de sugerir trilhas de estudo personalizadas, considerando o desempenho individual do aluno e priorizando revisões estratégicas para otimizar o processo de aprendizagem.

## Integrantes

*   **Bianca Conceição Baise** — RA: 10417489<br/>
*   **Guilherme Vieira Rodrigues** — RA: 10419633<br/>
*   **Julia Petersen Aderne de Sá** — RA: 10419605<br/>
*   **Maria Eduarda Pinheiro Leal da Cunha** — RA: 10416676<br/>
*   **Rodrigo Nascimento Tomaz** — RA: 10418449

## Contexto Acadêmico

Este projeto é desenvolvido no âmbito da disciplina de Inteligência Artificial e não possui vínculo com outras disciplinas ou com o Trabalho de Conclusão de Curso (TCC) dos integrantes.

## Área e Abordagem de Inteligência Artificial

O projeto está inserido na área de **Educação** e **Sistemas de Recomendação**. A abordagem principal utiliza técnicas de **Machine Learning (ML)** e **Deep Learning (DL)** para análise de dados e geração de recomendações personalizadas.

## Estrutura do Repositório

O repositório está organizado nas seguintes pastas para facilitar a navegação e o acesso aos diferentes componentes do projeto:

*   `relatorio/`: Contém o artigo parcial, versões do relatório, o template SBC e outros documentos relacionados ao desenvolvimento do projeto.<br/>
*   `dataset/`: Contém amostras do dataset e arquivos auxiliares. O dataset completo não é versionado devido ao seu tamanho e é obtido via script automatizado.<br/>
*   `notebooks/`: Inclui os notebooks Jupyter utilizados para análise exploratória dos dados, bem como para as etapas de limpeza e preparação.<br/>
*   `codigo/`: Contém os scripts Python auxiliares e as rotinas principais de análise e preparação de dados.

## Dataset

O projeto utiliza o dataset ASSISTments Data Set 2012-2013:<br>
https://www.kaggle.com/datasets/nicolaswattiez/skillbuilder-data-2009-2010?resource=download

O dataset contém registros de interações de estudantes com exercícios, incluindo:
- identificação do aluno: `user_id`
- habilidade/conteúdo: `skill`
- acerto ou erro:`correct`
- tempo de resposta:`ms_first_response`
- número de tentativas: `attempt_count`
- uso de dicas: `hint_count`
- sequência temporal: `start_time` e `end_time`
- identificação de exercício: `problem_id`
- lista de exercícios: `assignment_id`
- ordem de aprendizado: `sequence_id`
- emoção do aluno: `Average_confidence(FRUSTRATED)`, `Average_confidence(CONFUSED)` e `Average_confidence(CONCENTRATING)`

## Preparação dos Dados

Devido ao grande volume do dataset original, ele não foi incluído diretamente no repositório.

Para garantir reprodutibilidade, foi desenvolvido um script automatizado para download e organização dos dados:

`python codigo/load_data.py`

## Como Executar

Para explorar e executar os componentes deste projeto, siga as orientações abaixo:

1. **Instalação de Dependências**
   `pip install pandas kagglehub`<br/>

2. **Baixar o dataset:**
   `python codigo/load_data.py`<br/>
   Este script realiza o download automático do dataset e o organiza na pasta `dataset/raw/`<br>

3. **Gerar amostra dos dados:** `python codigo/create_sample.py`<br>
   A amostra será salva em: `dataset/sample.csv`.<br>
   Essa etapa é necessária devido ao grande volume do dataset original, permitindo análises sem sobrecarga de memória.<br/>

## Etapa Atual do Projeto (Parte 2)

Esta versão do repositório corresponde à Parte 2 do projeto de Inteligência Artificial. Nesta fase, foram abordados os seguintes aspectos:

*   Proposta detalhada do projeto.
*   Definição e aquisição do dataset.
*   Realização da análise exploratória dos dados.
*   Implementação das etapas de preparação e pré-processamento dos dados.
*   Elaboração do relatório parcial.

O repositório será continuamente atualizado nas próximas etapas do projeto, incluindo a Parte 3, com a implementação dos modelos de recomendação e a análise dos resultados.

## Observações Finais

Este README será atualizado conforme o progresso do projeto. Sugestões e contribuições são bem-vindas para aprimorar a documentação e o desenvolvimento da solução.
