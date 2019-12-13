import re

# I'd like to thank stack overflow for their help here
with open("halo_corpus_file.corp", encoding="utf-8") as corpus_file:
    # expression = re.compile(".*halo.*", re.IGNORECASE)
    num_surrounding_words = 3
    search_term = "reach"
    # word_regex_before = r'\w+\s' * num_surrounding_words
    # word_regex_after = r'\s\w+' * num_surrounding_words
    word_regex_before = r'\w+\s'
    word_regex_after = r'\s\w+'
    pat_context = re.compile(r'((' + word_regex_before + r'){0,' + str(num_surrounding_words) + r'}' + search_term + r'(' + word_regex_after + r'){0,' + str(num_surrounding_words) + r'}' + r')', re.IGNORECASE)
    pat_word = re.compile(r'(' + search_term + r')', re.IGNORECASE)
    # pat_word = re.compile(r'\s(' + search_term + r')\s', re.IGNORECASE)
    pat_lines = re.compile(r"^(.*\n*.*" + search_term + r".*\n*.*)$", re.MULTILINE)

    corpus = corpus_file.read()
    hits = pat_context.findall(corpus)
    for hit in hits:
        print(hit[0])
    iterator = re.finditer(pat_lines, corpus)
    count = 0
    for match in iterator:
        count +=1
        # print(match.span())
        print("-------")
        print(corpus[match.span()[0]: match.span()[1]])
        print("-------")
    print(count)
    # find word count
    hits = pat_word.findall(corpus)
    print(len(hits))
    # query = re.search(".*Halo.*", corpus)
    # print(query.group())

    # corpus = corpus_file.readlines()
    # for line in corpus:
    #     print(line)
    #     query = re.search(".*Reach.*", line)
    #     if query is None:
    #         continue
    #     print(query.group())
    #     break