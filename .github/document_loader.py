
import os

def load_documents(folder):
    docs=[]
    for f in os.listdir(folder):
        with open(os.path.join(folder,f)) as file:
            docs.append(file.read())
    return docs
