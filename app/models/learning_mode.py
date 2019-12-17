def build_learning_mode_data(words, translated_words, username):
    if len(words) != len(translated_words):
        raise ValueError('Corrupted input (len_diff)')

    cards = list()

    for index in range(len(words)):
        entry = {"word": words[index], "translated_word": translated_words[index]}
        cards.append(entry)

    return cards
