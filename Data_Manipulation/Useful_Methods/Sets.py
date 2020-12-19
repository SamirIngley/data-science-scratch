# collection of distinct elements,
# define a set using curly braces

primes_below_10 = {2, 3, 5, 7}

# however for empty sets you can't do {} since that's for dicts, instead s = set()
# IN membership is very fast in a set and more appropriate than a list

stopwords_list = ["a", "an",  "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list     # False but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # VERY FAST to check

