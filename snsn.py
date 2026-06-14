import os

print(os.path.abspath("model.pkl"))

with open("model.pkl", "rb") as f:
    print(f.read(20))
    