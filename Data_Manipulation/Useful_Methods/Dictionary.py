# Dictionary: associates values with keys
#   allows you to quickly retrieve the value corresponding to a given key.

empty_dict = {}
empty_dict2 = dict()

grades = {"Joel": 80, "Bruno": 100}


# CHECK IF IN DICT for the existance of a key using "in"
joel_had_grade = "Joel" in grades   # TRUE 
kate_has_grade = "Kate" in grades   # FALSE

# LOOK UP the value for a key with square brackets
joels_grade = grades["Joel"]

# IF NOT IN the dict, you'll get a KeyError
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# **** GET RETURNS A DEFAULT VALUE **** (instead of raising an exception) when you look up a key that's not in the dict
no_ones_grade = grades.get("No One")    # equals None
joels_grade = grades.get("Joel", 0)     # equals 80
kates_grade = grades.get("Kate", 0)     # equals 0

# ASSIGN key/value pairs using same square brackets
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)  # equals 3


# REPRESENT STRUCTURED DATA
tweet = {
    "user" : "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hash_tags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# *** ITERABLES *** allow us to iterate through the dictionary
# for key, value in tweet.items(): print(key, value)    # prints everything out
tweet_keys = tweet.keys()       # for key in tweet.keys():
tweet_values = tweet.values()   # iterable for the values
tweet_items = tweet.items()     # iterable for (key, value) tuples

# defaultdict allows us to not need to check if an item exists
from collections import defaultdict

word_counts = defaultdict(int)      # int() produces 0
for word in document:
    word_counts[word] += 1