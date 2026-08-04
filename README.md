# Polish Word Generation

This project aims to generate nonce-words that sound naturally Polish by following the language's typical sound patterns.

- bigarms
- MLP
- wavenet

## Generation

words in API are generated using the code in wavenet/wavenet3.ipynb as it outperforms other techniques that I tried

| Real words        | Generated words |
| ----------------- | --------------- |
| abiudykacja       | cyłogistyca     |
| arkadowanie       | chronon         |
| hebrajszczyzna    | ekompencja      |
| fotomontaż        | kormatyzracja   |
| jabłuszko         | żekonitielacha  |
| lampownia         | inwekratyczność |
| niesłuszność      | iziofilimowanie |
| płaskorzeźba      | preodomant      |
| stępor            | rzedawój        |
| wysiłek           | tap             |
| zewidencjonowanie | uzajni          |
| bezwładność       | zlerek          |
| grzybiarnia       | łóż             |
| wodowskaz         | oddzięcie       |
| ślusarnia         | rozproedzistka  |
| praworządność     | gruchesja       |

## API

API using Flask

| 10 random real words                           | 10 random generated words                    |
| ---------------------------------------------- | -------------------------------------------- |
| [mzums.com/pl/real](https://mzums.com/pl/real) | [mzums.com/pl/gen](https://mzums.com/pl/gen) |
| ![](image-1.png)                               | ![](image.png)                               |

## Training details:

The model is trained to predict the next character given a fixed context window of previous characters. I use Maximum Likelihood Estimation (MLE) – specifically categorical cross-entropy – as the training objective.

The table below shows the validation per-character negative log-likelihood (NLL) measured after 300,000 optimization iterations (batches) for each architecture:

- Bigram (baseline): 2.41
- MLP: 1.94
- WaveNet: 1.73

_Lower values indicate better predictive performance._

## Dataset

training on ~48k words

dataset based on:  
https://raw.githubusercontent.com/ostr00000/jezyk-polski-slowniki/refs/heads/master/class_a.txt

## Additional credits
This project largely follows makemore from Andrej Karpathy's [*Zero to Hero*](https://karpathy.ai/zero-to-hero.html) series, although it also contains a lot of my comments, explanations, experiments and the API.

## Local setup
1. Clone the repo  
  `git clone https://github.com/mzums/polish_word_generation`
2. Enter the directory  
  `cd polish_word_generation`
3. Create conda evironment  
  `conda create --name polish_word_generation python=3.12`
4. Activate the environment  
  `conda activate polish_word_generation`
5. Install dependencies  
  `pip install -r requirements.txt`
6. Play with the notebooks
7. Generate words with `wavenet/wavenet3.ipynb`
8. Run the API  
    `python api/app.py`
8. Check results  
    `http://127.0.0.1:5001/pl/gen`  
    `http://127.0.0.1:5001/pl/real`