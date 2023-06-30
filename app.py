from entity_extraction import EntityExtraction

sentence = "toyota avanza putih"
extractor = EntityExtraction()
result = extractor.doc(sentence)
print(result)