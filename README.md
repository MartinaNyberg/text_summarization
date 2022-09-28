# Text Summarization

A simple extractive text summarizer for Swedish, using spacy. 

The summarization is done based on word frequencies (excluding stop words) in the document. Here, words occurring more repetedly in the text are assumed to be the most significant in forming the overall meaning of the text. Sentences are ranked based on how common their words are, and the n top ranked sentences are printed as the summary.  
