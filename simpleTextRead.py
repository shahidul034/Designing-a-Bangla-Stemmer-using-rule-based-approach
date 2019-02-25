with open("simple movie reviews.txt", "r") as file:
    documents = file.read().splitlines()

print(documents)

'''Let’s get all the unique words from the four loaded sentences ignoring the case,
 punctuation, and one-character tokens.
 These words will be our vocabulary (known words).
 '''

# Import the libraries we need
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Step 2. Design the Vocabulary
# The default token pattern removes tokens of a single character. That's why we don't have the "I" and "s" tokens in the output
count_vectorizer = CountVectorizer()

# Step 3. Create the Bag-of-Words Model
bag_of_words = count_vectorizer.fit_transform(documents)

# Show the Bag-of-Words Model as a pandas DataFrame
feature_names = count_vectorizer.get_feature_names()
pd.DataFrame(bag_of_words.toarray(), columns = feature_names)
