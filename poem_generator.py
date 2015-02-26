from random import choice, random

def main():
    """
    Generates a poem from samples of William Carlos Williams's work
    using Markov chains.
    """
    with open("C:\\Users\\Richard\\Documents\\C O R N E L L\\1 2014\\CS 1610\\poem\\williams_samples.txt", "rt") as f:
        raw = f.read()
    words = raw.split()
    dictionary = prepare(words)
    poem = create(dictionary)
    print poem

def prepare(w):
    """
    Return a dictionary created from the words.
    """
    d = {} # create a new dictionary
    d['.'] = [w[0]] # key for starting a new sentence
    d[','] = [] # key for starting clause after a comma
    for i in range(len(w)-1):
        key = w[i]
        nxt = w[i+1]
        
        # words not at the end of a clause
        if key[-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            if key not in d:
                d[key] = []
            d[key].append(nxt)
        # words preceding a comma
        elif key[-1] not in '.!?':
            d[','].append(nxt)
        # words ending sentences
        else:
            d['.'].append(nxt)
    return d

def create(d):
    """
    Generates the poem.
    """
    newline = 0 # chance of new line
    finished = 0.1 # chance of ending the poem
    switch = False
    
    first = choice(d['.'])
    li = [first]
    i = 0
    while not switch:
        temp = li[i].replace('\n', '')
        
        # pick a word based on the last word
        if temp[-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            li.append(choice(d[temp]))
        # pick a word that comes after a comma
        elif temp[-1] not in '.!?':
            li.append(choice(d[',']))
        #if end of sentence:
        else: 
            # randomly end poem
            if random() < finished: 
                switch = True
            # start new sentence
            else:
                li.append(choice(d['.']))
                finished += 0.1
        
        # randomly go to next line
        if random() < newline:         
            li[-1] = '\n' + li[-1]
            newline = 0.05
        else:
            newline += 0.05
        
        i += 1
            
    return ' '.join(li)
    
main()