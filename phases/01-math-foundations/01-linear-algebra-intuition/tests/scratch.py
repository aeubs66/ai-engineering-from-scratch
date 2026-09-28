a = [3, 4]
b = [1, 2]

dot = a[0] * b[0] + a[1] * b[1]
length = (a[0] ** 2 + a[1] ** 2) ** 0.5

print("dot product:", dot)
print ("length of a:", length)

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def length(a):
    return (a[0] ** 2 + a[1] ** 2) ** 0.5

def cosine(a, b):
    return dot(a, b) / (length(a) * length(b))

hi = [9, 8]
hello = [8, 9]
car = [1, 9]

print("hi and hello: ", cosine(hi, hello))
print("hi and car:", cosine(hi, car))

words = {
    "hello" : [8, 9],
    "car" : [1, 9],
    "dog" : [9, 2],
    "cat" : [8, 3],
}

query = [9, 8]

best_word = None
best_score = -1

for name, vector in words.items():
    score = cosine(query, vector)
    print(name, score)
    if score > best_score:
        best_score = score
        best_word = name
        
print("best match:", best_word)