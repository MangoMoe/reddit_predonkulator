import numpy as np

names = ["atheism", "Frugal", "gadgets", "halo", "Home", "IAmA", "legaladvice", "linguisticshumor", "movies", "pics", "popular", "relationship_advice", "trashy", "videos", ]
num_posts = np.array([922, 955, 250, 956, 237, 249, 989, 976, 456, 976, 1000, 971, 660, 612, ]) # note that not always were 1000 posts extracted, this was just the max
comments_per_post = np.array([47.33839479392625, 38.372774869109946, 277.532, 13.333682008368202, 2.50210970464135, 296.43775100401604, 6.406471183013145, 12.1875, 106.34210526315789, 30.63217213114754, 147.873, 13.879505664263645, 123.86363636363636, 61.46895424836601, ])
words_per_item = np.array([42.39277874837612, 43.23968017850502, 30.21161359987497, 26.962610024005237, 21.05021971123666, 42.340355285846044, 81.61982006543076, 18.11120589375727, 31.193324173603816, 22.038903453409716, 24.152512544249124, 75.67223872349244, 21.23520241691843, 25.242807944276134, ])
word_total = np.array([1892668, 1627801, 2126384, 370655, 33533, 3167609, 598763, 233544, 1543820, 680936, 3595657, 1095507, 1757213, 974852, ])

print("Average number of posts collected per subreddit: {}".format(np.mean(num_posts)))
print("Average number of comments per post: {}".format(np.mean(comments_per_post)))
print("Average number of words per item (post or comment): {}".format(np.mean(words_per_item)))
print("Total number of words in corpus: {}".format(np.sum(word_total)))