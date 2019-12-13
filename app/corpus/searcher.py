import re

# I'd like to thank stack overflow for their help here
with open("halo_corpus_file.corp", encoding="utf-8") as corpus_file:
    # expression = re.compile(".*halo.*", re.IGNORECASE)
    num_surrounding_words = 3
    search_term = "halo"
    word_regex_before = r'\w+\s' * num_surrounding_words
    word_regex_after = r'\s\w+' * num_surrounding_words
    pat = re.compile(r'(' + word_regex_before + search_term + word_regex_after + r')')
    # pat = re.compile(r'(\w+\s\w+\shalo\s\w+\s\w+)')
    corpus = corpus_file.read()
    hits = pat.findall(corpus)
    for hit in hits:
        print(hit)
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