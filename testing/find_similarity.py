import spacy

nlp = spacy.load("en_core_web_lg")

string1 = "A beautiful landscape with a deer."
string2 = "Moose near a beautiful landscape."

string1 = nlp.vocab[string1]
string2 = nlp.vocab[string2]

string1.similarity(string2)