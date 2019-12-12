import re

with open("halo_corpus_file.corp", encoding="utf-8") as corpus_file:
    expression = re.compile(".*halo.*", re.IGNORECASE)
    corpus = corpus_file.read()
    query = re.search(".*Halo.*", corpus)
    print(query.group())

    # corpus = corpus_file.readlines()
    # for line in corpus:
    #     print(line)
    #     query = re.search(".*Reach.*", line)
    #     if query is None:
    #         continue
    #     print(query.group())
    #     break