'''
@author: kvmu

This is a quick and dirty script to generate n TeX files of a 5 by 4 array of words and pictures.
I'm required to pick 20 random words/pictures from a given set of words and pictures and
produce a file of the result in pdf format. I do this by first creating TeX files and then compiling
them (there is a batch compile script in the corresponding output directories).
'''

import numpy as np
import os
import itertools

def random_gen(low, high):
    '''
    An infinite generator which yields an integer from the discrete uniform distribution.

    requires:
    low - an integer >= 0
    high - an integer > low

    returns:
    nothing
    '''
    while True:
        yield np.random.randint(low, high)


def make_random_list(low, high):
    '''
    A function that creates a list of length list_length (default value = 20) containing
    unique integers selected by random from the discrete uniform distribution.

    requires:
    low - an integer >= 0
    high - an integer > low

    returns:
    a list of random integers from [low, high), including low, excluding high
    '''
    list_length = 20  # number of items in output grid of words or pictures
    gen = random_gen(low, high) # initialize generator
    items = set()
    for x in itertools.takewhile(lambda x: len(items) < list_length, gen):
        items.add(x)
    return list(items) # change into list so it can be indexed later on


def gen_photo_TeX(fnames, photo_path):
    '''
    This function generates the LaTeX string to create a 5x4 array of photos.

    assumes:
    the photos corresponding to the filenames in fnames are in the directory photo_path

    requires:
    fnames - a list of photo filenames
    photo_path - an absolute or relative path to the photos

    returns:
    tex_string - a string containing the formatted LaTeX
    '''
    tex_string = ('\\documentclass[12pt,a4paper]{article}\n\\usepackage{graphicx}\n'+
                          '\\newcommand*{\\addheight}[2][.5ex]{\\raisebox{0pt}[\dimexpr'+
                          '\\height+(#1)\\relax]{#2}}\n'+'\\begin{document}\n\\thispagestyle{empty}\n'+
                          '\\begin{center}\n\\begin{tabular}{cccc}\n')
    for i, fname in enumerate(fnames):
        if (i+1) % 4 == 0: # if it is the last column
            tex_string += '\\addheight{\\includegraphics[width=0.2\\linewidth]{'+photo_path+fname+'}} \\\\\n'
        else:
             tex_string += '\\addheight{\\includegraphics[width=0.2\\linewidth]{'+photo_path+fname+'}} &\n'
    tex_string += '\\end{tabular}\n\\end{center}\n\\end{document}'
    return tex_string


def gen_word_TeX(words):
    '''
    This function generates the LaTeX string to create a 5x4 array of words.

    assumes:
    the list of words corresponds to a photo, ie if the word is 'apple', there must exist a picture of an
    apple in the photo directory.

    requires:
    words -  a list of words

    returns:
    tex_string - a string containing the formatted LaTeX
    '''
    tex_string = ('\\documentclass[12pt,a4paper]{article}\n\\usepackage{graphicx}\n'+
                         '\\usepackage[margin=0.5in]{geometry}\n'+
                         '\\begin{document}\n' + '\\thispagestyle{empty}\n' +
                         '\\begin{table}[]\n\\centering\n\\Huge\n'+ '\\begin{tabular}{cccc}\n')
    for i in range(5): # the number of rows
        a, b, c, d =  words[4*i:(i+1)*4] # indexing in groups of 4
        tex_string += (a + '&' + b + '&' + c + '&' + d + '\\\\  & & & \\\\\n')
    tex_string += '\\end{tabular}\n\\end{table}\n\\end{document}'
    return tex_string


def save_TeX(TeXString, savePath, filename):
    '''
    This function writes the created TeX into a file.

    assumes:
    TeXString is valid LaTeX code and savePath exists

    requires:
    TeXString - a string object containing formatted LaTeX
    savePath - the absolute or relative path to where .tex file is saved
    filename - the name of the .tex file

    returns:
    nothing
    '''
    texDoc = open(savePath+filename, 'w+')
    texDoc.write(TeXString)
    texDoc.close()
    return


def make_photo_matricies(photo_savepath, num_sets):
    '''
    This function does a batch creation of the desired output files (for photos).

    assumes:
    photo_savepath exists

    requires:
    photo_savepath - a relative or absolute path where the output files are to be saved
    num_sets - an integer >= 0 that specifies how many TeX files to generate

    outputs:
    nothing
    '''
    photo_path = 'C:/Users/Kevin/Documents/GitHub/psych-study/photos' #where the input photos are located
    for index in range(num_sets):
        fnames = os.listdir(photo_path)
        index_choices = make_random_list(0,len(fnames))
        fnames = [fnames[i] for i in index_choices]
        stringo = gen_photo_TeX(fnames, photo_path)
        save_TeX(stringo, photo_savepath, 'photo_'+str(index+1)+'.tex')
    return


def make_word_matricies(word_savepath, num_sets):
    '''
    This function does a batch creation of the desired output files (for words).

    assumes:
    word_savepath exists

    requires:
    word_savepath - a relative or absolute path where the output files are to be saved
    num_sets - an integer >= 0 that specifies how many TeX files to generate

    outputs:
    nothing
    '''
    word_path = 'C:/Users/Kevin/Documents/GitHub/psych-study/' # where the input words are located
    text_filename = 'PSYCH217-ItemList.txt'
    for index in range(num_sets):
        words_list = map(lambda x: x.title(),
                                     np.genfromtxt(word_path+text_filename, delimiter='.', dtype=str)[:,1])
        index_choices = make_random_list(0, len(words_list))
        words_list = [words_list[i] for i in index_choices]
        stringo = gen_word_TeX(words_list)
        save_TeX(stringo, word_savepath, 'word_'+str(index+1)+'.tex')
    return


def main():
    '''
    Creates the output!
    '''
    photo_savepath = 'C:/Users/Kevin/Documents/GitHub/psych-study/photos_output/'
    words_savepath = 'C:/Users/Kevin/Documents/GitHub/psych-study/words_output/'
    make_photo_matricies(photo_savepath, 100)
    make_word_matricies(words_savepath, 100)
    return


if __name__ == '__main__':
    main()
