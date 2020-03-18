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


def generate_text(probs, min_words=0):
    sentence = [np.random.choice(list(probs.keys()))]
    while True:
        word = np.random.choice(list(probs[sentence[-1]].keys()), p=list(probs[sentence[-1]].values()))
        sentence.append(word)
        # End condition
        if len(sentence) > min_words and word[-1] in punctuation:
            break
    sentence[0] = sentence[0].capitalize()
    return " ".join(sentence)


if __name__ == "__main__":
    poems = open(config.clean_txt_path, "r", encoding='utf-8-sig').read()
    poems = poems.lower().replace("\n", " ").split(' ')
    p = generate_probs(poems)
    out = generate_text(p, 5)
    print(out)
