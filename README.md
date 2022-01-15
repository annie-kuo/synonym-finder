# synonym-finder
This program learns to solve a synonyms multiple choice quiz when provided texts or reading passages. An example of question that can be on the quiz is the following:

> Choose the correct synonym of the given word: Forestall

> (A) Avoid

> (B) Frighten

> (C) Prevent

> (D) Disappoint

To determine the option that is most likely to be the right answer, the program evaluates the *semantic similarity* between the given word and each option. The higher the semantic similarity between two words, the closer their meanings.

To compute the semantic similarity of each pair of words, a *semantic descriptor vector* is first computed for each word. This program can compute three types of similarity measures: the cosine similarity, the negative euclidean distance similarity, and the normalized negative euclidean distance similarity.

## Features
- Perform vector operations (addition, substraction, merging two vectors, dot product, normalization, computation of norm).
- Processes text files and computes the semantic descriptor vectors for each word.
- Computes the cosine similarity between two words.
- Computes the negative euclidean distance similarity between two words.
- Computes the normalized negative euclidean distance similarity between two words.
- Guess the synonym of a given word from a list of choices.
- Solve a synonyms multiple choice quiz.
- Evaluates its correctness given the answers (i.e. computes the percentage of correct answers).
- Generates a bar graph to plot the performance of the three similarity measures used to determine the most accurate one.
