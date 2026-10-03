message = "Hello Everybody! My name is John."
print(message)

song = """Bohemian rhapsody,
Queen,
Drums"""

print(song)

print(song[0])
print(song[len(song)-1])
print(song[-1])

print(message[6:15])

#Reversing strings

print(message[::-1])
rev_message = "".join(reversed(message))
print(rev_message)
rev_message2 = list(reversed(message))
print(rev_message2)
print(song.lower())
print(song.upper())
print(song.title())



