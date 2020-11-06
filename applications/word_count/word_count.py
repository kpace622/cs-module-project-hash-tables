def word_count(s):
    # Your code here
    dict = {}

    string = s.split()
    print(string)
    for x in string:
        x.lower()
        if x.isalpha():
            dict[x] = 1
    
    print("dict", dict)

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))