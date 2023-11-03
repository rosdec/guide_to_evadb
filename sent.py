from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you"]
print(sentiment_pipeline(data))