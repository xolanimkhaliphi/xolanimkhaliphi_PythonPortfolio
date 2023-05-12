import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Garden Path sentences
gardenpathSentences = [
    "The old man the boat sailed out to sea.",
    "The horse raced past the barn fell.",
    "I convinced her children are noisy.",
    "The complex houses married and single soldiers and their families.",
    "The man who hunts ducks out on weekends."
]

# Tokenize and perform entity recognition on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Entities:")
    for entity in doc.ents:
        print("\t", entity.text, entity.label_)
    print()

# At the bottom of your file, write a comment about two unusual entities you found that spaCy gave one of the words
# of your sentences - did you expect this? One unusual entity that spaCy gave was "children" in the sentence "I
# convinced her children are noisy." It was labeled as "MISC" (miscellaneous), which I did not expect. This is likely
# because "children" is not a named entity, but rather a common noun referring to a group of people. Another unusual
# entity that spaCy gave was "ducks" in the sentence "The man who hunts ducks out on weekends." It was labeled as
# "MISC" (miscellaneous), which I did not expect. This is likely because "ducks" is not a named entity, but rather a
# common noun referring to a group of animals.
