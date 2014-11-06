# The values of the two jokers. Their values are fixed and cannot change in the
#program.
JOKER1 = 27
JOKER2 = 28
ASCII_OF_A = 65

'''#####     Functions for running an encryption or decryption.     #####'''


def clean_message(secret_text):
    ''' (str) -> str
    
    Return a copy of the message that includes only its alphabetical characters,
    where each of those characters has been converted to uppercase
    
    >>>clean_message('asd 2dsga')
    'ASDDSGA'
    
    >>>clean_message('eNCRYp3T')
    'ENCRYPT'
    '''
    
    changed_text = ''
    
    for i in range(len(secret_text)):
        if secret_text[i].isalpha():
            changed_text = changed_text + secret_text[i].upper()
            
    return changed_text


'''#####     NEXT FUNCTION     ##########     NEXT FUNCTION     #####'''


def encrypt_letter(character , keystream_value):
    '''(str , int) -> str
    
    Applys the keystream value to the character to encrypt the character and 
    return the result.
    
    >>>encrypt_letter('B' , 5)
    'G'
    
    >>>encrypt_letter('P' , 2)
    'R'
    '''
#Finding position of character wrt A : ASCII value of character - ASCII value
#of A, i.e. 65

    character_value = ord(character) - ASCII_OF_A
    
#Adding keystream value to character value. If the result is >26, then taking
#remainder.   

    encrypt_value = character_value + keystream_value
    if encrypt_value >= 26 :
        encrypt_value = encrypt_value % 26
        
#Adding 65, i.e. ASCII value of A to bring the value back to ASCII compatible 
#value, converting it into a character and returning it.

    encrypt_value += ASCII_OF_A
    
    return chr(encrypt_value)


'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def decrypt_letter(character , keystream_value):
    '''(str , int) -> str
    
    Applys the keystream value to the character to decrypt the character 
    and return the result.
    
    >>>decrypt_letter('G' , 5)
    'B'
    
    >>>decrypt_letter('R' , 2)
    'P'
    '''
    
#Finding position of character wrt A : ASCII value of character - ASCII 
#value of A, i.e. 65   

    character_value = ord(character) - ASCII_OF_A
    
#Subtracting keystream value from character value. If the result is <0, 
#then adding 26. 

    decrypt_value = character_value - keystream_value
    if decrypt_value < 0 :
        decrypt_value = decrypt_value + 26
        
#Adding 65, i.e. ASCII value of A to bring the value back to ASCII compatible 
#value, converting it into a character and returning it..

    decrypt_value += 65
    return chr(decrypt_value)
    

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''

    
def swap_cards (deck , index):  
    '''(list of int , int) -> NoneType
    
    Swaps the card at the given index in the deck with the card that follows
    it. The deck is treated as circular, i.e. if the ard appears at the last 
    position then it is swapped with the first card of the deck.
    
    >>>deck = [5 , 6 , 3 , 7 , 9]
    >>>swap_cards ( deck , 3)
    >>>deck
    [5, 6, 3, 9, 7]
    
    >>>deck = [5 , 3 , 7 , 8 , 4 , 9]
    >>>swap_cards (deck , 5)
    >>>deck
    [9, 3, 7, 8, 4, 5]
    '''
    
    deck_len = len(deck) - 1
    
#if given index is the last card of the deck, then it is swapped with the 
#first card of the deck. Else it is swapped with the next card.
    
    if index == deck_len :
        temp = deck[0]
        deck[0] = deck[index]
        deck[index] = temp
    else :
        temp = deck[index + 1]
        deck[index + 1] = deck[index]
        deck[index] = temp

    
'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''

        
def move_joker_1(deck):
    '''(list of int) -> NoneType
    
    Finds the JOKER1 and swaps it with its next card. Deck is treated to be 
    circular.
    
    >>>deck = [23, 27, 13, 16]
    >>>move_joker_1(deck)
    >>>deck
    [23, 13, 27, 16]
    
    >>>deck = [1, 5, 27, 17, 28]
    >>>move_joker_1(deck)
    >>>deck
    [1, 5, 17, 27, 28]
    '''
    
    status = 'notfound'
    i = 0
    
#Loop runs as long as the JOKER1 is not found. When found, swap_cards is 
#called to execute the required swap   

    while status == 'notfound' :
        if deck[i] == JOKER1 :
            swap_cards (deck, i)
            status = 'found'
        else:
            i = i + 1
            

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def move_joker_2(deck):
    '''(list of int) -> NoneType
    
    Finds the JOKER2 and moves it two cards down, i.e. swaps it twice with the 
    card following it after each swap.Deck is treated to be circular.
    
    >>>deck = [23, 28, 13, 16]
    >>>move_joker_2(deck)
    >>>deck
    [23, 13, 16, 28]
    
    >>>deck = [1, 4, 17, 16, 9, 28, 10]
    >>>move_joker_2(deck)
    >>>deck
    [28, 4, 17, 16, 9, 10, 1]
    '''
    
    status = 'notfound'
    i = 0
    
#Loop runs as long as the JOKER2 is not found. When found,  swap_cards is 
#called twice to execute the required swap. Also, when JOKER2 is at the last 
#position, then swap_cards is called which swaps it with the first card, hence 
#its index is changed to 0

    while status == 'notfound' :
        if deck[i] == JOKER2 :
            for j in range(2):
                if i == len(deck)-1:
                    swap_cards (deck, i)                
                    i = 0
                else:
                    swap_cards (deck, i)
                    i += 1
            status = 'found'
        else:
            i = i + 1
            

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def triple_cut(deck):
    '''(list of int) -> NoneType
    
    Finds the two jokers and executes triple cut, i.e.Swap the cards above the 
    first joker (the joker closest to the top of the deck) with the cards below 
    the second joker
    
    >>>deck = [23, 25, 27, 14, 15, 28, 17, 5]
    >>>triple_cut(deck)
    >>>deck
    [17, 5, 27, 14, 15, 28, 23, 15]
    
    >>>deck = [1, 9, 23, 28, 17, 5, 27]
    >>>triple_cut(deck)
    >>>deck
    [28, 17, 5, 27, 1, 9, 23]

    '''
    
#Finding the indices of the two jokers.

    for i in range(len(deck)):
        if deck[i] == JOKER1:
            joker1_index = i
        elif deck[i] == JOKER2:
            joker2_index = i
            
            #Algorithm for TRIPLE CUT..!!

    status = 'notcompleted'
    while status == 'notcompleted':
        
#If JOKER1 comes after JOKER2, then the written code is executed. Else,
#the values of the variables are interchanged and then the code is executed.
        
        if joker1_index > joker2_index :
            new_deck = deck[:]  
            
#count the number of elements from the back to be moved to the front. Also 
#count the number of elements that are between the two jokers that are not 
#to be moved.

            chartoswap_back = len(deck[joker1_index + 1 :])
            if chartoswap_back == 28 :
                chartoswap_back = 0
            unchanged_char = len(deck[joker2_index : joker1_index+1])
            
#Now first move the elements of back of the deck to front. Then move the 
#elements between the two jokers. Then finally move the elements from the start 
#to the deck.
#All these movements replace the elements in the original. This is the reason
#the deck was earlist copied in a new_deck variable. 

            deck[:chartoswap_back] = (new_deck[joker1_index+1 :])
            deck[chartoswap_back : chartoswap_back + unchanged_char] = (new_deck[joker2_index : joker1_index+1])
            deck[chartoswap_back + unchanged_char : ] = (new_deck[:joker2_index])
            status = 'completed'
                    
#If JOKER1 comer before JOKER2 , then their indices are swaped and the above 
#code is executed

        else :
            temp = joker1_index
            joker1_index = joker2_index
            joker2_index = temp
  

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''
  
         
def insert_top_to_bottom (deck):
    '''(list of int) -> NoneType
    
    Looks at the number of the bottom-most card and moves that many cards from
    the top to above the bottom-most card. If the bottom-most card is JOKER2, 
    then JOKER1 is used the value of bottom-most card.
    
    >>>deck = [1, 2, 4, 7, 9, 3]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [7, 9, 1, 2, 4, 3]
    
    >>>deck = [3, 6, 18, 28, 27, 10, 2]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [18, 28, 27, 10, 3, 6, 2]
    '''
   
#Calculate the number of cards tha are to be moved from top to bottom.

    last_card_is_joker2 = ''
    
    if deck[-1] == JOKER2 :
        tomove = JOKER1
        last_card_is_joker2 = 'true'
    else :
        tomove = int(deck[-1])
        last_card_is_joker2 = 'false'
        
    len_of_deck = len(deck)
        
#Copy the list of cards that are to be moved to a new list

    cards_to_move = deck[:tomove]
    
#First moves the cards that come after the cards that are to be moved to the 
#bottom to the top of the  deck. Then the cards that are to be moved are 
#coppied and finally the last card is coppied into the deck.

    deck[:len_of_deck - tomove -1] = deck[tomove : -1]
    deck [len_of_deck - tomove -1 : len_of_deck -1] = cards_to_move[:]
    
    if last_card_is_joker2 == 'false':
        deck[len_of_deck -1] = tomove
    else :
        deck[len_of_deck -1] = JOKER2
    
    
'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def get_card_at_top_index (deck) :
    '''(list of int) -> int
    
    Returns the card whoes index has the value equal to the value of the first
    card. If card at the first position id JOKER2, then value of JOKER1 is used
    as index.
    
    >>>deck = [2, 4, 6, 8, 3, 1]
    >>>get_card_at_top_index(deck)
    6
    
    >>>get_card_at_top_index([4, 17, 28, 17, 27, 19, 6])
    27    
    '''
    
    if deck[0] == JOKER2 :
        index = JOKER1
    else :
        index = deck[0]
        
    return deck[index]
     

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def get_next_value (deck):
    '''(list of int) -> int
    
    Returns a potential keystream value after doing all the five steps of the 
    algorithm
    
    >>>get_next_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    
    >>>get_next_value([14, 17, 20, 6, 28, 15, 18, 21, 24, 2, 1, 27, 23, 26, 9, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 12])
    23
    '''

#Calls all the functions required to generate a keystream value and returns the 
#generaated keystream value

    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    return get_card_at_top_index(deck)  


'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def get_next_keystream_value(deck):
    '''(list of int) -> int
    
    Repeats the five steps of keystream gen algorithm through get_next_value 
    until an acceptable keystream, i.e. b/w 1 and 26 is generated.
    
    >>>get_next_keystream_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    
    >>>get_next_keystream_value([14, 17, 20, 6, 28, 15, 18, 21, 24, 2, 1, 27, 23, 26, 9, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 12])
    23
    '''
    
#Calls the funnction to genetate keystream value until a keystream value <26 is 
#generated

    key_stream = get_next_value(deck)
    while key_stream > 26 :
        key_stream = get_next_value(deck)
    return key_stream


'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def process_message (deck , message , action):
    '''(list of int , str , str) -> str
    
    Return the encrypted or decrypted message, as selected in action.
    
    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_message(deck , 'CSC108 rocks', 'e')
    NBZYYBVD
    
    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_message(deck, 'LLFWRDC' , 'd')
    ACIPHER
    '''
    
    processed_message = '' 
    
#If the text needs to be encrypted, then first it is cleaned and then encrypted
#by generating a keystream value for each character.

    if action == 'e':
        cleaned_message = clean_message(message)
        for i in range(len(cleaned_message)):
            keystream = get_next_keystream_value(deck)
            processed_message += encrypt_letter(cleaned_message[i] , keystream)
            
#If text needs to be decrypted, then keystream values are generated for each 
#character and the character is decrypted.
            
    else:
        for i in range(len(message)):
            keystream = get_next_keystream_value(deck)
            processed_message += decrypt_letter(message[i] , keystream)
            
    return processed_message
            
            

'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def process_messages(deck , messages , action):
    '''(list of int , list of str , str) -> list of srt
    
    Return the list of encrypted or decrypted messages, as selected in action.
    
    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['CSC108 rocks' , 'Computer Science' , 'University_of_Toronto'], 'e')
    ['NBZYYBVD', 'JWVAFTCWBWZWWSX', 'RWFTYDLHTOGHHVPGZFP']
    
    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['LLFWRDC', 'ANXJO'], 'd')
    ['ACIPHER', 'PGPAD']
    '''
    
#Encrypts or decrypts every line of the given file.

    final_text = []
    for message in messages :
        final_text.append(process_message(deck , message , action))
        
    return final_text


'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def read_messages(file):
    '''(file open for reading) -> list of str
    
    Reads a the contents of a file and strips the newline character from each 
    line.
    
    '''
    
    contents_of_file = []
    contents_of_file = file.readlines()
    for i in range(len(contents_of_file)) : 
        contents_of_file[i] = contents_of_file[i].strip()
        
    return contents_of_file


'''#####     NEXT FUNCTION     ###############     NEXT FUNCTION     #####'''


def read_deck(file):
    '''(file open for reading) -> list of int
    
    Reads and returns the contents of the file containing the deck of cards.
    
    '''
    
#Checks for all sets of characters between empty spaces, either space character,
#or a newline character, and created the deck.

    deck = []
    i = 0
    temp = ''
    content = file.read()
    
    while i < (len(content) - 1):
        temp = temp + content[i]
        i = i + 1        
        if content[i] == ' ' or content[i] == '\n':
            deck.append(temp)
            i = i + 1
            temp = ''
            
#Converts the seperated characters in integer format. The data read from the 
#file is character, and is necessary to be converted to integer format 
#to be used in our program.

    for i in range(len(deck)):
        deck[i] = int(deck[i])
    return deck
    

'''#####     END OF FUNCTIONS     ############     END OF FUNCTIONS     #####'''