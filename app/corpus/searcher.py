import re

# I'd like to thank stack overflow for their help here
with open("halo_corpus_file.corp", encoding="utf-8") as corpus_file:
    # expression = re.compile(".*halo.*", re.IGNORECASE)
    num_surrounding_words = 3
    search_term = "reach"
    word_regex_before = r'\w+\s' * num_surrounding_words
    word_regex_after = r'\s\w+' * num_surrounding_words
    pat_context = re.compile(r'(' + word_regex_before + search_term + word_regex_after + r')', re.IGNORECASE)
    # pat = re.compile(r'(\w+\s\w+\shalo\s\w+\s\w+)')
    corpus = corpus_file.read()
    hits = pat_context.findall(corpus)
    for hit in hits:
        print(hit)
    print(len(hits))
    pat_word = re.compile(search_term, re.IGNORECASE)
    # pat_word_newline = re.compile(r'\r\n.*\r\n.*search_term.*\r\n.*\r\n', re.IGNORECASE)
    pat_word_newline = re.compile(r"^(.*\n.*" + search_term + r".*\n.*)$", re.MULTILINE)
    iterator = re.finditer(pat_word_newline, corpus)
    count = 0
    for match in iterator:
        count +=1
        # print(match.span())
        # print("-------")
        # print(corpus[match.span()[0]: match.span()[1]])
        # print("-------")
    print(count)
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