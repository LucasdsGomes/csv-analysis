# Análise Exploratória de Dados — Salários e Experiência

## 📌 Objetivo
Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) para identificar padrões e relações entre variáveis relacionadas ao mercado de trabalho, como experiência profissional, idade, salário, carga horária e avaliação de desempenho.

O foco do projeto é transformar dados brutos em insights claros e compreensíveis, utilizando Python e bibliotecas amplamente usadas em ciência de dados.

---

## Imagens
<img width="638" height="507" alt="image" src="https://github.com/user-attachments/assets/f7467ead-b9a3-425e-8103-b0e268ac9189" />
<img width="639" height="505" alt="image" src="https://github.com/user-attachments/assets/49acd298-7872-43c7-b5f8-d80afad6bc9d" />
<img width="640" height="509" alt="image" src="https://github.com/user-attachments/assets/ecc174e1-bc10-46b4-81f7-7993610a3428" />

---

## 📊 Dataset
O conjunto de dados é fictício e foi criado exclusivamente para fins educacionais, simulando informações de profissionais:

- Idade
- Anos de experiência
- Salário
- Horas trabalhadas por semana
- Avaliação de desempenho

---

## 🔍 Análises realizadas
- Estatísticas descritivas (média, mediana, dispersão)
- Visualização da relação entre:
  - Experiência × Salário
  - Idade × Salário
  - Horas trabalhadas × Avaliação de desempenho

---

## 💡 Principais insights
- Existe uma relação positiva entre anos de experiência e salário: profissionais mais experientes tendem a receber salários mais altos.
- A idade apresenta correlação com o salário, porém menos forte que a experiência profissional.
- Trabalhar mais horas por semana não garante necessariamente melhores avaliações de desempenho.
- Avaliações mais altas tendem a ocorrer em faixas mais equilibradas de carga horária.

---

## 🛠️ Tecnologias utilizadas
- Python 3
- Pandas
- Matplotlib
- Streamlit
---

## ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório
```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
---
cd nome-do-repositorio
---
python -m venv .venv
---
source venv/bin/activate  # Linux/macOS
venv\Scripts\Activate.ps1   # Windows
---
pip install -r requirements.txt
```

### 2️⃣ Comandos principais para execução
--file           Caminho do arquivo CSV
--column         Nome da coluna a ser analisada
--save           Executa análise estatística descritiva salvando-a individualmente
--verify         Executa verificação de qualidade dos dados
--save-quality   Salva relatório de qualidade em arquivo .txt
--plot           Gera histograma da coluna selecionada

## Execução Básica
```python main.py --file caminho/do/arquivo.csv --column nome_da_coluna```
## Análise Estatística da Coluna
```python main.py --file dados.csv --column salario --stats```
## Verificação de Qualidade dos Dados
```python main.py --file dados.csv --column idade --verify```
## Salvar Relatório de Qualidade
```python main.py --file dados.csv --column idade --verify --save-quality```
## Gerar Histograma
```python main.py --file dados.csv --column salario --plot```

LEMBRANDO QUE O --FILE SÓ É OBRIGATÓRIO SE FOR UM ARQUIVO ÚNICO DE DADOS SEPARADO DO PADRÃO EM data/data.csv. CASO CONTRÁRIO:
```python main.py --column nome_da_coluna```


📈 Próximos passos

- Aplicar a análise em datasets reais
- Explorar correlação estatística
- Automatizar geração de relatórios
- Evoluir para análises orientadas a negócio


