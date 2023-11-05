import evadb

cursor = evadb.connect().cursor()

cursor.query("""
    CREATE FUNCTION IF NOT EXISTS SentimentAnalysis
        IMPL 'sentiment_analysis.py';
""").df()

cursor.query("""
    CREATE TABLE IF NOT EXISTS twits (
        id INTEGER UNIQUE,
        twit TEXT(140));
""").df()

cursor.query("LOAD CSV 'tweets.csv' INTO twits;").df()

response = cursor.query("""
    SELECT twit, SentimentAnalysis(twit) FROM twits     
""").df()

print(response)