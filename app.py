from entity_extraction import EntityExtraction

sentence = "innova red toyota avanza white"
extractor = EntityExtraction()
result = extractor.doc(sentence)
print(result)
