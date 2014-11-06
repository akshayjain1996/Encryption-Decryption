"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck.txt'
MSG_FILENAME = 'message_file1.txt' #File containing the message you want to encrypt/decrypt
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    
#Opens the files of deck and message for reading, converts the content into a 
#form comprehendable by the program using the read_deck and read_message
#functions, and then encrypts or decrypts the message and prints it.

    deck = open(DECK_FILENAME , 'r')
    message = open(MSG_FILENAME , 'r')
    processed_deck = cipher_functions.read_deck(deck)
    processed_msg = cipher_functions.read_messages(message)
    final_msg  = cipher_functions.process_messages(processed_deck , processed_msg , MODE)
    for msg in final_msg :
        print(msg)
    
    pass

main()
