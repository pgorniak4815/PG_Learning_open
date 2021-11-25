"""
Case Study from "Using Python for Research" course.

The task is to find and plot the distribution of word frequencies
for each translation of Hamlet. Check if distribution depends on the translation.
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']

    for ch in skips:
        text.replace(ch,"")

    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts. Use Counter from collections.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']

    for ch in skips:
        text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts


def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


def word_stats(word_counts):
    """
    Return number of unique words and word frequencies.
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)


book_titles = {
    'English':
       {'shakespeare': ("A+Midsummer+Night's+Dream", 'Hamlet', 'Macbeth',
        'Othello', 'Richard+III', 'Romeo+and+Juliet', 'The+Merchant+of+Venice')},
    'French':
        {'chevalier': ("L'enfer+et+le+paradis+de+l'autre+monde", "L'i%CC%82le+de+sable",
        'La+capitaine', 'La+fille+des+indiens+rouges', 'La+fille+du+pirate',
        'Le+chasseur+noir', 'Les+derniers+Iroquois')},
    'German':
        {'shakespeare': ('Der+Kaufmann+von+Venedig', 'Ein+Sommernachtstraum', 'Hamlet',
        'Macbeth', 'Othello', 'Richard+III', 'Romeo+und+Julia')},
    'Portuguese': 
        {'shakespeare': ('Hamlet',)}}


hamlets = pd.DataFrame(columns = ["language","text"])

title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = "./Using_Python_For_Research_Course/Project_Gutenberg/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

grouped_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show()   