from indicoio.custom import Collection
indicoio.config.api_key = '4db161e811d460e7173d6dbb19384330'

collection = Collection("collection_name")

# Add Data
collection.add_data([["text1", "label1"], ["text2", "label2"], ...])

# Training
collection.train()

# Telling Collection to block until ready
collection.wait()

# Done! Start analyzing text
collection.predict("indico is so easy to use!")
