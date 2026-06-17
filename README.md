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
