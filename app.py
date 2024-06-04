from entity_extraction import EntityExtraction

sentence = "i have two cars: a red honda brio and a white honda jazz"
extractor = EntityExtraction()
result = extractor.doc(sentence)
print(result)
