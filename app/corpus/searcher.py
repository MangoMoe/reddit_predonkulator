import re
import glob
import numpy as np

# I'd like to thank stack overflow for their help here
# TODO make it do the search on all the corpora
corpus_name = input("enter the name of the subreddit you want to search, or enter 'search all' to search all corpora: ")
if len(corpus_name.split()) == 1:
    with open(corpus_name + "_corpus_file.corp", encoding="utf-8") as corpus_file:
        corpus = corpus_file.read()
        # expression = re.compile(".*halo.*", re.IGNORECASE)
        search_type = input("enter 'lines' to search for a word and its surrounding lines.\nEnter 'context' to search for a word and a number of words before or after.\nEnter 'frequency' to find the frequency of a word:\n")
        search_term = input("Enter your search term: ")
        if search_type == 'lines':
            # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
            # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
            # adds an extra context line on each side (for a total of 2), for some reason wayyyyy slower if you put * after \n instead of +
            pat_lines = re.compile(r"^(.*\n+.*\n+.*" + search_term + r".*\n+.*\n+.*)$", re.MULTILINE | re.IGNORECASE)
            # pat_lines = re.compile(r"\n+.*\n+.*" + search_term + r".*\n+.*\n+", re.MULTILINE | re.IGNORECASE)
            iterator = re.finditer(pat_lines, corpus)
            for match in iterator:
                # print(match.span())
                print("-------")
                print(corpus[match.span()[0]: match.span()[1]])
        elif search_type == 'context':
            num_surrounding_words_left = int(input("Enter number of surrounding words on left side: "))
            num_surrounding_words_right = int(input("Enter number of surrounding words on right side: "))
            word_regex_before = r'\w+\s'
            word_regex_after = r'\s\w+'
            pat_context = re.compile(r'((' + word_regex_before + r'){0,' + str(num_surrounding_words_left) + r'}' + search_term + r'(' + word_regex_after + r'){0,' + str(num_surrounding_words_right) + r'}' + r')', re.IGNORECASE)
            hits = pat_context.findall(corpus)
            for hit in hits:
                print(hit[0])
        elif search_type == 'frequency':
            pat_word = re.compile(r'(' + search_term + r')', re.IGNORECASE)
            # pat_word = re.compile(r'\s(' + search_term + r')\s', re.IGNORECASE)

            # find word count
            hits = pat_word.findall(corpus)
            print(len(hits))
        else:
            # TODO return an error here
            pass
else:
    # TODO make it so this is less of a copy and paste of the abovve code
    results = []
    # get some stuff from all corpora
    num_results_per_reddit = int(input("How many results per subreddit? "))
    search_type = input("enter 'lines' to search for a word and its surrounding lines.\nEnter 'context' to search for a word and a number of words before or after.\nEnter 'frequency' to find the frequency of a word:\n")
    search_term = input("Enter your search term: ")
    if search_type == 'context':
        num_surrounding_words_left = int(input("Enter number of surrounding words on left side: "))
        num_surrounding_words_right = int(input("Enter number of surrounding words on right side: "))
    for filenum, filename in enumerate(glob.glob("*.corp")):
        count = 0
        with open(filename, encoding="utf-8") as corpus_file:
            results.append([])
            corpus = corpus_file.read()
            # expression = re.compile(".*halo.*", re.IGNORECASE)
            if search_type == 'lines':
                # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
                # pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)
                # adds an extra context line on each side (for a total of 2), for some reason wayyyyy slower if you put * after \n instead of +
                pat_lines = re.compile(r"^(.*\n+.*\n+.*" + search_term + r".*\n+.*\n+.*)$", re.MULTILINE | re.IGNORECASE)
                # pat_lines = re.compile(r"\n+.*\n+.*" + search_term + r".*\n+.*\n+", re.MULTILINE | re.IGNORECASE)
                iterator = re.finditer(pat_lines, corpus)
                for match in iterator:
                    if count > num_results_per_reddit:
                        break
                    count += 1
                    # print(match.span())
                    results[filenum].append("-------\n" + corpus[match.span()[0]: match.span()[1]])
            elif search_type == 'context':
                word_regex_before = r'\w+\s'
                word_regex_after = r'\s\w+'
                pat_context = re.compile(r'((' + word_regex_before + r'){0,' + str(num_surrounding_words_left) + r'}' + search_term + r'(' + word_regex_after + r'){0,' + str(num_surrounding_words_right) + r'}' + r')', re.IGNORECASE)
                hits = pat_context.findall(corpus)
                for hit in hits:
                    if count > num_results_per_reddit:
                        break
                    count += 1
                    results[filenum].append(hit[0])
            elif search_type == 'frequency':
                pat_word = re.compile(r'(' + search_term + r')', re.IGNORECASE)
                # pat_word = re.compile(r'\s(' + search_term + r')\s', re.IGNORECASE)

                # find word count
                hits = pat_word.findall(corpus)
                results[filenum].append(len(hits))
            else:
                # TODO return an error here
                pass
    for result, name in zip(results, glob.glob("*.corp")):
        print("\n\nr/{}:".format(name[:-5]))
        for hit in result:
            print(hit)
    if search_type == 'frequency':
        print("\n")
        print("Total frequency: {}".format(np.sum(np.array(results))))
        print("Mean frequency: {}".format(np.mean(np.array(results))))
