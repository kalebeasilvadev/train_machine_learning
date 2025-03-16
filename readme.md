# Documentação do Projeto: Treinamento e Re-treinamento de Modelo de Machine Learning

Este repositório contém um projeto de **Aprendizado de Máquina** que ilustra o fluxo completo de criação, exportação, aprimoramento e validação de um modelo treinado inicialmente no [Teachable Machine](https://teachablemachine.withgoogle.com/). O arquivo principal do repositório é o **`retreinamento.ipynb`**, responsável por carregar o modelo exportado e realizar ajustes de hiperparâmetros, validação com novos dados e análise de métricas.

---

## 1. Visão Geral do Projeto

1. **Treinamento Inicial no Teachable Machine**  
   - Foi criado um modelo para classificar pelo menos duas categorias (imagens, áudio ou poses, dependendo do escopo escolhido).  
   - Após obter resultados satisfatórios, o modelo foi exportado para uso fora do Teachable Machine (em TensorFlow, Keras ou outro formato compatível).

2. **Repositório e Arquivos Principais**  
   - **`retreinamento.ipynb`**: Notebook em Python (Google Colab / Jupyter) que carrega o modelo exportado e realiza o re-treinamento e teste.  
   - *Possíveis pastas auxiliares*:
     - `models/`: Contém arquivos do modelo exportado (caso existam `.h5`, `.json`, `.pb` ou outros relacionados).  
     - `data/`: Conjunto de dados adicionais para testes ou re-treinamento (se necessário).  
     - `images/`: Imagens de suporte ou documentação.

3. **Motivação**  
   - Demonstrar como iniciar um projeto de **Machine Learning** de forma simples com o Teachable Machine.  
   - Aprender a exportar e, em seguida, melhorar o modelo em um ambiente de desenvolvimento Python (Google Colab / Jupyter Notebook), ajustando hiperparâmetros, testando novas amostras e computando métricas de avaliação.

---

## 2. Estrutura do Repositório

```
train_machine_learning/
├── models/
│   ├── <arquivos_modelo_exportado>.h5
│   ├── ...
├── data/
│   ├── <arquivos_de_dados_para_teste_ou_treinamento>
│   ├── ...
├── images/
│   ├── <imagens_de_documentação>
│   ├── ...
├── retreinamento.ipynb
├── README.md (este arquivo de documentação)
└── ...
```

- **`retreinamento.ipynb`**: Contém o passo a passo para carregar o modelo, re-treiná-lo e avaliá-lo.
- **`models/`**: Possível local onde estão armazenados os arquivos gerados pelo Teachable Machine ou treinamentos anteriores.
- **`data/`**: Onde podem estar armazenados dados (imagens, CSVs, etc.) para testes adicionais ou retraining.

---

## 3. Como Executar o Projeto

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/kalebeasilvadev/train_machine_learning.git
   cd train_machine_learning
   ```

2. **Instalar Dependências (opcional)**  
   Se estiver executando localmente (fora do Google Colab), crie um ambiente virtual e instale as dependências necessárias. Caso use Google Colab, basta garantir que as bibliotecas principais estejam instaladas no notebook.

   ```bash
   # Exemplo de criação de ambiente virtual e instalação de pacotes
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou venv\Scripts\activate  # Windows

   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   *Observação:* Pode ser que o arquivo `requirements.txt` não esteja disponível em seu repositório. Nesse caso, instale manualmente as bibliotecas que aparecem no notebook (ex.: TensorFlow, Scikit-Learn, etc.).

3. **Abrir o Notebook `retreinamento.ipynb`**  
   - No Google Colab, basta fazer o upload deste notebook ou usar a opção “Open in Colab” se disponível.
   - Localmente, abra o Jupyter Notebook/ JupyterLab:
     ```bash
     jupyter notebook retreinamento.ipynb
     ```

4. **Executar as Células Passo a Passo**  
   - Siga as instruções dentro do notebook para:
     1. Carregar o modelo exportado do Teachable Machine.
     2. Realizar o re-treinamento ou ajuste de hiperparâmetros.
     3. Testar o modelo em dados adicionais.
     4. Gerar as métricas de avaliação (acurácia, matriz de confusão, recall, etc.).

---

## 4. Explicação Resumida do `retreinamento.ipynb`

O notebook **`retreinamento.ipynb`** foi estruturado para contemplar as seguintes etapas:

1. **Importação de Bibliotecas**  
   Bibliotecas como TensorFlow, Keras, NumPy, Pandas e Scikit-Learn são importadas.

2. **Carregamento do Modelo**  
   - O modelo, previamente treinado no Teachable Machine, é carregado (em formato `.h5`, `.json` + pesos ou outro padrão).  
   - É verificado se o modelo foi importado corretamente.

3. **Pré-processamento dos Dados**  
   - Conversão de imagens em tensores (no caso de classificação de imagens).  
   - Normalização ou padronização de dados, se necessário.  

4. **Re-treinamento/Ajuste**  
   - Ajuste de hiperparâmetros (por exemplo, taxa de aprendizado, camadas adicionais, epochs, batch size, etc.).  
   - Treinamento em novos dados ou re-treinamento com uma fração dos dados originais para refinar o modelo.

5. **Validação e Testes**  
   - Criação da matriz de confusão para análise de como o modelo classifica cada categoria.  
   - Cálculo de métricas como **acurácia**, **precisão**, **recall**, **F1-Score**, entre outras.

6. **Conclusões e Próximos Passos**  
   - Análise dos resultados obtidos.  
   - Sugestões de melhorias ou de dados adicionais para melhor performance.

---

## 5. Principais Métricas

Durante o re-treinamento, as métricas utilizadas para avaliar o desempenho do modelo incluem:

- **Acurácia (accuracy)**: Percentual de acertos do modelo em relação ao total de previsões.
- **Precisão (precision)**: Habilidade do modelo em não classificar positivamente amostras que são negativas.
- **Recall**: Capacidade de identificar corretamente as amostras positivas.
- **Matriz de Confusão (confusion matrix)**: Mostra os acertos e erros de forma tabular para cada classe, permitindo análise aprofundada de onde o modelo pode falhar.

Essas métricas podem ser vistas nos *outputs* do notebook, geralmente representadas em forma de texto (scores numéricos) e, quando possível, em gráficos (matriz de confusão).

---

## 6. Resultados e Discussões

- **Resultados Obtidos**  
  Explique no seu relatório ou aqui no README quais foram os principais valores de acurácia e demais métricas após o re-treinamento. Exemplifique:

  > *Exemplo:* “O modelo atingiu **92%** de acurácia e apresentou um **recall** de **90%**, o que indica boa capacidade de detecção das classes propostas.”

- **Possíveis Melhorias**  
  - Aumentar o conjunto de dados (mais imagens ou samples de áudio).
  - Realizar técnicas de aumento de dados (data augmentation).
  - Ajustar parâmetros da rede, como número de camadas, número de neurônios e taxa de dropout.
  - Otimizar a taxa de aprendizado (learning rate) ou testar diferentes otimizadores (Adam, SGD, RMSprop etc.).

---

## 7. Considerações Finais

Este projeto demonstra, de forma simplificada, todo o processo de:
1. **Treinamento de um modelo em uma ferramenta de fácil acesso** (Teachable Machine).  
2. **Exportação** do modelo para um formato compatível com bibliotecas de Machine Learning.  
3. **Re-treinamento e validação** com dados adicionais ou ajustes de hiperparâmetros, utilizando bibliotecas avançadas como TensorFlow e Scikit-Learn.

A proposta atende aos critérios básicos de um workflow de **Machine Learning supervisionado**, que vão desde a coleta de dados até a análise de métricas. Sinta-se à vontade para contribuir com sugestões, melhorias ou abrir **Issues** neste repositório.

---

## 8. Referências

- [Teachable Machine](https://teachablemachine.withgoogle.com/)  
- [Documentação do TensorFlow](https://www.tensorflow.org/?hl=pt-br)  
- [Documentação do Keras](https://keras.io/)  
- [Scikit-Learn: Machine Learning em Python](https://scikit-learn.org/stable/)  

---

### Autor

- [Kalebe Andrade Silva](https://github.com/kalebeasilvadev)

Caso tenha dúvidas ou deseje colaborar, abra uma **Issue** ou envie um **Pull Request**. Agradecemos o seu interesse! 

--- 

<sup>© 2025 - Projeto de Aprendizado de Máquina - Todos os direitos reservados.</sup>