import string
def generate_hashtag(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    hashtag = ''.join(word.capitalize() for word in s.split())
    hashtag = '#' + hashtag
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag if len(hashtag) > 1 else False
input_string = "I very like Pyton"
print(generate_hashtag(input_string))