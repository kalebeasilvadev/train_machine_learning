# **Documentação do Notebook `retreinamento.ipynb`**

## **Objetivo**
Este notebook é usado para treinar e ajustar um modelo de classificação de imagens, focado na distinção entre duas classes: cães e gatos. Para isso, utilizamos a biblioteca TensorFlow/Keras para carregar, treinar, ajustar e avaliar o modelo.

---

## **Sumário**

1. **Bibliotecas utilizadas**  
   Importação de pacotes essenciais para o processamento de imagens, construção de modelos, treinamento e avaliação.  
   Principais pacotes:
   - TensorFlow/Keras (modelos e pré-processamento)
   - Scikit-learn (métricas)
   - Matplotlib e Seaborn (visualização)
   - Numpy (manipulação numérica)

2. **Carregamento do Modelo Pré-treinado**  
   - Uso de uma camada customizada `CustomDepthwiseConv2D`, necessária para resolver problemas relativos ao parâmetro `groups`.
   - Carregamento de um modelo salvo no formato Keras H5.
   - Compilação inicial utilizando `Adam` otimizado para classificação binária.

3. **Configuração dos Geradores de Dados**  
   - Caminhos de pastas para **treinamento**, **validação** e **teste**.
   - Aplicação de técnicas de *data augmentation* no conjunto de treinamento:
      - Rotação de imagens
      - Deslocamento horizontal/vertical
      - Espelhamento horizontal
   - Sem *data augmentation* para os conjuntos de validação e teste.

4. **Ajuste Fino (Fine-Tuning)**  
   - Congelamento de todas as camadas do modelo.
   - Descongelamento das últimas 5 camadas para ajuste mais profundo.
   - Recompilação do modelo com um *learning rate* menor (1e-5).
   - Uso de callbacks, como `EarlyStopping`, `ReduceLROnPlateau` e `ModelCheckpoint`.

5. **Treinamento do Modelo**  
   - Configuração de 10 épocas ajustáveis.
   - Treinamento utilizando os geradores e callbacks configurados.
   - Visualização das curvas de aprendizado do modelo:
      - Curva de acurácia
      - Curva de perda (loss)

6. **Avaliação do Modelo**  
   - Avaliação no conjunto de teste para obter métricas como:
      - Acurácia
      - Matriz de confusão (visualizada com heatmap)
      - Relatório de classificação (precisão, recall, F1-score)
   - Visualização das previsões com gráficos de dispersão (scatter plot).

7. **Previsão em Imagem Individual**  
   - Função para prever a classe de uma única imagem.
   - Predição em lote com visualização gráfica dos resultados.

---

## **Funcionamento em Detalhes**

### **1. Carregamento do Modelo**
O modelo carregado foi previamente salvo em `./content/model.h5`. É recompilado utilizando:
- **Funções perda:** `binary_crossentropy`
- **Métrica:** `accuracy`
- **Otimização inicial:** Taxa de aprendizado padrão com `adam`.

### **2. Configuração dos Dados**
Os dados são estruturados em três conjuntos:
- **Treinamento:** Especificado para aumentar a robustez do modelo com *data augmentation*.
- **Validação/Teste:** Realizado sem aumento de dados, apenas com normalização.

Dimensões da imagem de entrada: **224 x 224**  
Classes trabalhadas: **cães**, **gatos**  

### **3. Ajuste Fino e Treinamento**
Durante o fine-tuning:
- Apenas as últimas camadas foram ajustadas com um *learning rate* reduzido.
- Uso de três callbacks para melhorar o treinamento:
   1. **`EarlyStopping`:** Parar caso a validação não melhore após 5 épocas.
   2. **`ReduceLROnPlateau`:** Reduzir o LR em 50% caso a acurácia da validação não melhore em 3 épocas.
   3. **`ModelCheckpoint`:** Salvamento do melhor modelo no arquivo `fine_tuned_model.h5`.

O treinamento é realizado em **10 épocas** (ajustável).

### **4. Resultados e Avaliação**
Após o treinamento, o modelo é avaliado no conjunto de teste.  
As métricas incluem:
- **Acurácia no teste**
- **Matriz de Confusão**  
  Mostrada como um gráfico de calor para comparação das previsões corretas e incorretas.  
- **Relatório de Classificação:**  
  Inclui:
  - Precisão (Precision)  
  - Recall  
  - F1-Score  
  - Suporte (quantidade de exemplos por classe)  
- **Scatter Plot:** Visualização das previsões com dispersão utilizando `true_classes` e `predicted_classes`.

### **5. Função para Previsão Individual**
Uma função personalizada permite prever a classe de imagens únicas.  
Etapas do processo:
1. Carregamento da imagem.
2. Redimensionamento para **224x224** e normalização.
3. Previsão utilizando o modelo.
4. Retorno da classe como `Cachorro` ou `Gato`.

A funcionalidade também inclui previsão por lote, exibindo imagens e suas classes em uma grade.

---

## **Saídas do Notebook**
1. Treinamento do modelo com métricas claras sobre desempenho.
2. Visualização detalhada do processo de ajuste fino e validação.
3. Capacidade de prever imagens individuais, o que é útil em cenários do mundo real.
4. Visualizações e relatórios completos (curvas de aprendizado, matrizes de confusão, gráficos dispersos).

---

## **Pontos de Melhorias**
- Incluir mais classes para ampliar a capacidade do modelo.
- Ajustar os hiperparâmetros (e.g., taxa de aprendizado, arquitetura).
- Implementar validação cruzada para avaliar a variação do treinamento.

Essa documentação organiza os principais componentes do notebook, tornando-o mais compreensível e acessível a novos usuários. Em que mais posso ajudar? 😊