# Text Summarization

A simple extractive text summarizer for Swedish, using spacy. 

The summarization is done based on word frequencies (excluding stop words) in the document. Here, words occurring more repetedly in the text are assumed to be the most significant in forming the overall meaning of the text. Sentences are ranked based on how common their words are, and the n top ranked sentences are printed as the summary.  

A summary consisting of 5 sentences given the the sample text yields the output below. 

```Vi har flera alternativ av löparskor, allt från avancerade, dyrare skor till enklare, billigare löparskor. Addera ett par short och en t-shirt eller löpartights och en jacka och du är redo för hur många kilometer som helst. Detta på grund av att löpningen ökar din produktion av proteinet BDNF, som är mycket positivt för flera funktioner i hjärnan. Löpträning hjälper nybildningen av celler i hippocampus, något som är bra både för ditt minne men även för inlärningsförmågan. Så, om du har en arbetsuppgift, tenta eller bekymmer hemma som strular till det för dig föreslår vi att du tar en löprunda och ger tankeverksamheten en ny chans efter det.```
