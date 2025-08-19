from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


result = classifier("the keyboard fells really strong and I love the sound os the keys")
print(result)