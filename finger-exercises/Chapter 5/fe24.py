"""Finger exercise: Using encoder and encrypt as models, implement
the functions decoder and decrypt. Use them to decrypt the message

22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*1
37*59*11*23*11*1*57*6*173*7*11

which was encrypted using the opening of Don Quixote."""


DON_QUIXOTE = """In a village of La Mancha, the name of which
I have no desire to call to mind, there lived not long since one of
those gentlemen that keep a lance in the lance-rack, an old
buckler, a lean hack, and a greyhound for coursing. """

SECRET_MESSAGE = "22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11"

PLAIN_TEXT = "comprehension is incomprehensible"

gen_code_keys = (lambda book, plain_text: ({c: str(book.find(c)) for c in plain_text}))

gen_decode_keys = (lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')})

encoder = (lambda code_keys, plain_text: ''.join(['*' + code_keys[c] for c in plain_text])[1:])

decoder = (lambda decode_keys, cipher_text: ''.join(decode_keys[s] for s in cipher_text.split('*')))

gen_code = gen_code_keys(DON_QUIXOTE, PLAIN_TEXT)
coded_message = encoder(gen_code, PLAIN_TEXT)

gen_decode = gen_decode_keys(DON_QUIXOTE, SECRET_MESSAGE)
decoded_message = decoder(gen_decode, SECRET_MESSAGE)

print(coded_message)
print(decoded_message)
