from entity_extraction import EntityExtraction

sentence = "honda jazz putih"
extractor = EntityExtraction()
result = extractor.doc(sentence)
print(result)
