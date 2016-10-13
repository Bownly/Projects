#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This code converts the raw text files dumped from a DPPt rom into a more human readable format.
# Further, it groups the resulting files into groups of 10 for a more convenient file count.
# Note: For copyright reasons, I'm not putting the text files on github

import codecs

start = 1
end = 601

name_mc = '主人公'
name_rival = 'ライバル'

for j in range(start, end):

    replacements = {'－':'ー',
                    '⋯':'…',
                    '\\n':'\n', # \n take you to the 2nd line
                    '\\f':'\r\r', # \f starts a new text page
                    '\\r':'\r\r', # \r ends the textbox
                    'VAR(260, 0)':'[#]',  # Route number
                    'VAR(264, 1)':'[ITEM]',  # Some random bag item
                    'VAR(264, 2)':'[POCKET]',  # Some random bag pocket
                    'VAR(256, 0)':'[PKMN]',  # Starter? Rando Pokemon?
                    'VAR(256, 1)':'[PKMN]',  # Starter? Rando Pokemon?
                    'VAR(257, 0)':'[PKMN]',  # Pokemon nickname
                    'VAR(259, 0)『': name_rival +'『',   # Rival name
                    'VAR(259, 1)『': name_rival + '『',   # Rival name
                    'VAR(259, 0)': name_mc,   # MC name
                    'VAR(259, 1)': name_rival,   # Rival name
                    'VAR(262, 0)':'[MOVE]',  # some random move or whatever
                    'VAR(262, 1)':'[MOVE]',  # some random move or whatever
                    'VAR(262, 2)':'[MOVE]',  # some random move or whatever
                    'VAR(262, 3)':'[MOVE]',  # some random move or whatever
                    'VAR(264, 0)':'[TM]',    # some random item(tm?) or whatever
                    'VAR(270, 0)':'[TRAINER]', # player avatar in multiplayer
                    'VAR(281, 0)':'[ITEM]',  # some random underground item
                    'VAR(287, 2)':'[POCKET]',  # Some random bag pocket
                    'VAR(306, 0)':'[＃]',     # amount of pokemon caught
                    'VAR(308, 1)':'[＃]',     # amount of pokemon seen
                    'VAR(308, 0)':'[#]',     # streak count
                    'VAR(65280, 0)':'',      # Something about text color
                    'VAR(65280, 1)':'',      # Something about text color
                    'VAR(65281, 100)':'',    # Changes text size I think
                    'VAR(65281, 200)':'',    # Changes text size I think
                    'VAR(512, 1)':'',        # Puts 下画面 icon in text box afaict
                    }

    fileObj = codecs.open( "raw/" + str(j) + '.txt', "r", "utf-8" )
    iny = fileObj.read()

    # since var(259, 0/1) seem to switch back and forth, this code does some necessary damage control
    if iny.find(u'VAR(259, 0)『') != -1:
        print "unicode iny find: ", iny.find(u'VAR(259, 0)『')
        replacements['VAR(259, 1)'] = name_mc
        replacements['VAR(259, 0)'] = name_rival
    elif iny.find(u'VAR(259, 1)『'):
        replacements[u'VAR(259, 0)'] = name_mc
        replacements[u'VAR(259, 1)'] = name_rival

    fileObj.close()

    iny = open('raw/' + str(j) + '.txt', 'r').read()
    out = open('edited/Pearl_' + str(j) + '.txt', 'w')

    for i in replacements.keys():
        iny = iny.replace(i, replacements[i])
    out.write('File number: ' + str(j) + '\n\n' + iny)
    out.close

# merges files in groups of 10
linebreak = '\n======================================================================\n'
start2 = (end - start) / 10
zero_buffer = '00'

for j in range(start2):
    if j < 10:
        zero_buffer = '0'
    else:
        zero_buffer = ''
    out = open('merged/Pearl_Merged_' + zero_buffer + str(start + 10 * j) + '-' + zero_buffer + str(start + 10 * j + 9) + '.txt', 'w')
    out.write('')
    out.close()
    out = open('merged/Pearl_Merged_' + zero_buffer + str(start + 10 * j) + '-' + zero_buffer + str(start + 10 * j + 9) + '.txt', 'a+')
    for i in range(0, 10):
        iny = open('edited/Pearl_' + str(start + 10 * j + i) + '.txt').read()
        out.write(iny)
        out.write(linebreak)
    out.close()
