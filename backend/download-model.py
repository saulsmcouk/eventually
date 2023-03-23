import gensim.downloader as api

# Download the pre-trained model (in this case, the "glove-wiki-gigaword-300" model)
model = api.load("glove-wiki-gigaword-300")

# Save the model to disk as a binary file
model.save("pretrained_model.bin")
