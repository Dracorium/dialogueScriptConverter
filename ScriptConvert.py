'''
ScriptConvert.py
Conversion script to convert .txt scripts into .csv for UE usage

Current limitations: 
    - it requires manual input from user for tokens
    - Doesn't correctly make Choice section 
        (but that seems like it needs the format "Choice1_1" to properly label)

I'm restructuring this script to have a few features:
    - Accept/process a list of files from any location
    - Gather tokens from source file's name/hierarchy
        - Sequence ID
        - Scene ID/Number (number is most likely)
        - Suffix maybe?
    - Converted script csvs need to go to a specific location

Other Needs:
    - We may need a "script creator" to enforce naming convention for tokens

'''

import re #regular expressions
import os #to handle file paths for different operating systems
import sys
import fileinput
import pathlib

os.chdir('./') #change functioning directory to the folder of this file


def get_files_to_convert(*args):
    '''
    Will take any number of arguments for files to process and check
    their validity
    '''
    # sys.argv[0] accesses the file path of the script run

    files_to_convert = []

    try:
        sys.argv[1]
    except:
        print('No files given for conversion')
        sys.exit()

    for i in range(1, len(sys.argv)):
        source = str(sys.argv[i])
        if os.path.exists(f'{source}'):
            files_to_convert.append(source)
            print(f'Source path found [{source}]')
        else:
            print(f'Source file [{source}] NOT found.')

    try:
        files_to_convert[0]
    except:
        print('No valid files given for conversion')
        sys.exit()

    for i in range(0, len(files_to_convert)):
        source_file = files_to_convert[i]
        file_name = os.path.basename(source_file)
        print(f'Source file >> {file_name}')


def parse_file_name(*args):
    '''
    Retrieves tokens from the source file's name
    Tokens in file name will create the file path for the converted files
    File name convention: <sequence_id>_<scene_id>_<suffix>.txt

    sequence_id = alpha coded with any length (RSY, P, TART, etc)
    scene_id = number coded with 3 places
    suffix = optional token or identifier

    return: sequence_id, scene_id, suffix
    '''
    pass


def set_csv_destination():
    pass


def format_name(character_name):
    '''
    Format's name to use Title Casing
    '''
    character_name = str(character_name)
    if len(character_name) >= 2:
        character_name = character_name[0] + character_name[1:].lower() #keep first letter capitalized
        character_name = character_name
    return character_name


def pause_program():
    try:
        program_pause = raw_input('Press the <ENTER> key to continue...')
    except:
        program_pause = input('Press the <ENTER> key to continue...')


def create_csv_file():
    '''
    Creates csv file to convert script.txt lines for UE
    '''
    file_name_input = None
    converted_file = None
    scene_id = None
    starting_line_id = None
    print('Starting file with scene number {scene_id}'.format(**locals()))
    try:
        converted_file.close()
    except:
        pass
    
    if len(file_name_input) > 4 and file_name_input[0:5] == "Scene":
        csv_file_name = file_name_input + '.csv'
    else:
        csv_file_name = 'Scene' + str(scene_id) + '_' + file_name_input + '.csv'
    converted_file = open(csv_file_name, 'w')
    #first line of the file should contain column names
    converted_file.write(
        ',Speaker,Expression,Sound,Text,SpecialEvent,SpecialEffect,CharX,CharY,CharScale\n'
        )
    starting_line_id = 1
    scene_id += 1
    return file_name_input, converted_file, scene_id, starting_line_id


get_files_to_convert()

# create_csv_file()


# fileFound = False

# while not fileFound:
#     print("What is the file name (no file extension needed)?")
#     try:
#         file_name_input = input()
#     except:
#         file_name_input = raw_input()
#     file_name = file_name_input + ".txt"
#     fileFound = os.path.isfile(file_name)
#     if not fileFound:
#         print("ERROR: Cannot find a .txt file in this folder with that name. Please try again."
#               "\n***"
#               )
#         exit()


# print("What's the first scene number?")
# try:
#    scene_id = int(input())
# except ValueError:
#     print("That wasn't a valid number. Defaulting to scene number 0.")
#     scene_id = 0

# scriptFile = open(file_name) #w opens in write mode
# fullScript = scriptFile.readlines()
# scriptFile.close()


# print("Start at what row number?")
# try:
#     starting_line_id = int(input())
# except ValueError:
#     print("That wasn't a valid number. Defaulting to row number 1.")
#     starting_line_id = 1


# #loop through each line, alter it, and write it to new file
# for line in fullScript:
#     line = line.rstrip('\n')
#     line = line.replace('"', '""') #exit out of double quotes by making two
#     character_name = dialogue = specialEvent = '' #reset vars in the loop
#     if len(line) >= 1:
#         if line[0] != "#":  #hashtags reserved for comments
#             if line[0:2] == "__":
#                 create_csv_file()
#             elif line[0] == '*':
#                 try:
#                     specialEvent, dialogue = line.split(': ', 1)
#                 except:
#                     #if no colon, just set the special event
#                     specialEvent = line
#                 specialEvent = specialEvent[1:] #take out asterisk
                
#             else:
#                 try:
#                     character_name, dialogue = line.split(': ', 1) #split line only once
#                     character_name = format_name(character_name)
#                 except:
#                     print("This string could not be split:")
#                     print(line)
#                     character_name = line


#     line = str(starting_line_id) + ',"' + character_name + '","Nothing","None","' + dialogue + '","' + specialEvent + '","none","0.0","0.0","0.0"\n'
    
#     converted_file.write(line)
#     starting_line_id += 1


# converted_file.close()
# print("Script conversions complete!")
# pause_program()
