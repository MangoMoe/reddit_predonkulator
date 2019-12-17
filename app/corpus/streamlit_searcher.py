import streamlit as st

import re
import glob
import numpy as np
import time

# TODO use @st.cache at some point to optimize stuff
st.title("Reddit corpus searcher")

st.sidebar.markdown("Here we go I guess")
search_term = st.sidebar.text_input("Search Term")

search_all = st.sidebar.checkbox("Search All Subreddits Recorded")
# Note to self, using input anywhere here will cause that code to run on the terminal running the streamlit server lol
if not search_all:
    corpus_name = st.sidebar.text_input("Subreddit Name")
search_type = st.sidebar.radio("Search Type", ("Comment Context", "Concordance Lines", "Frequency"))

if not search_all:
    try:
        with open(corpus_name + "_corpus_file.corp", encoding="utf-8") as corpus_file:
            corpus = corpus_file.read()

            if search_type == 'Comment Context':
                # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
                # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
                # adds an extra context line on each side (for a total of 2), for some reason wayyyyy slower if you put * after \n instead of +
                pat_lines = re.compile(r"^(.*\n+.*\n+.*" + search_term + r".*\n+.*\n+.*)$", re.MULTILINE | re.IGNORECASE)
                # pat_lines = re.compile(r"\n+.*\n+.*" + search_term + r".*\n+.*\n+", re.MULTILINE | re.IGNORECASE)
                with st.spinner('Wait for it...'):
                    iterator = re.finditer(pat_lines, corpus)
                    for match in iterator:
                        # print(match.span())
                        "-------"
                        splits = corpus[match.span()[0]: match.span()[1]].splitlines()
                        for split in splits:
                            st.write(split)

            elif search_type == 'Concordance Lines':
                num_surrounding_words_left = st.sidebar.number_input("Number of words to the left", value=3)
                num_surrounding_words_right = st.sidebar.number_input("Number of words to the right", value=3)

                with st.spinner('Wait for it...'):
                    word_regex_before = r'\w+\s'
                    word_regex_after = r'\s\w+'
                    pat_context = re.compile(r'((' + word_regex_before + r'){0,' + str(num_surrounding_words_left) + r'}' + search_term + r'(' + word_regex_after + r'){0,' + str(num_surrounding_words_right) + r'}' + r')', re.IGNORECASE)
                    hits = pat_context.findall(corpus)
                st.success('Done!')

                my_bar = st.progress(0)
                for i, hit in enumerate(hits):
                    hit[0]
                    my_bar.progress(int(100 * (i / len(hits))))
            elif search_type == 'Frequency':
                pat_word = re.compile(r'(' + search_term + r')', re.IGNORECASE)
                # pat_word = re.compile(r'\s(' + search_term + r')\s', re.IGNORECASE)

                # find word count

                with st.spinner('Wait for it...'):
                    hits = pat_word.findall(corpus)
                st.write("Frequency of '{}' was {}".format(search_term, len(hits)))
                st.success('Done!')
            else:
                "Invalid type of search"
    except FileNotFoundError:
        "No corpus file matching that subreddit was found"

