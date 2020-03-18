import config
from collections import defaultdict
import numpy as np
from string import punctuation


def generate_probs(text):
    chain = defaultdict(lambda: defaultdict(lambda: 0.))

    for ind in range(len(text) - 1):
        chain[text[ind]][text[ind + 1]] += 1

    for k, v in chain.items():
        total = sum(v.values())
        for word, count in v.items():
            chain[k][word] = count / total

    return chain


def generate_text(num_words, probs):
    sentence = [np.random.choice(list(probs.keys()))]
    for i in range(1, num_words):
        sentence.append(np.random.choice(list(probs[sentence[i-1]].keys()), p=list(probs[sentence[i-1]].values())))
    sentence[0] = sentence[0].capitalize()
    return " ".join(sentence)


if __name__ == "__main__":
    poems = open(config.clean_txt_path, "r", encoding='utf-8-sig').read()
    poems = poems.lower().replace("\n", " ").split(' ')
    p = generate_probs(poems)
    out = generate_text(10, p)
    print(out)
