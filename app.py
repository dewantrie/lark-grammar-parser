from entity_extraction import EntityExtraction

sentence = "innova merah toyota avanza putih"
extractor = EntityExtraction()
result = extractor.doc(sentence)
print(result)
