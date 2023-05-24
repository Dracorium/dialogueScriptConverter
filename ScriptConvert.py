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
        - Suffix maybe? Should make this optional (doesn't attribute
          to csv file directory)
    - Converted script csvs need to go to a specific location with hierarchy
      created from the above tokens 

Other Needs:
    - We may need a "script creator" to enforce naming convention for tokens

'''

import re #regular expressions
import os #to handle file paths for different operating systems
import sys
import fileinput
import pathlib

class ScriptConverter:

    def __init__(self, *args):
        # Constants
        self.COLUMN_TITLES = [
            'LineID',
            'Speaker',
            'Expression',
            'Sound',
            'Text',
            'SpecialEvent',
            'SpecialEffect',
            'CharX',
            'CharY',
            'CharScale'
            ]
        self.NOT_LIST = ''
        self.NOTHING_AT_ALL = None

        # Other stuff
        self.root_dir = 'D:\\.tools\\dialogueScriptConverter\\samples\\root'
        self.file_name = ''
        self.name_tokens = dict(
            sequence_id = None,
            scene_id = None,
            suffix = None
            )



    def get_environment_variables(self, *args):
        pass


    def get_files_to_convert(self, *args):
        '''
        Will take any number of arguments for files to process and check
        their validity

        return: files_to_convert
        '''
        # sys.argv[0] accesses the file path of the script run

        files_to_convert = []

        try:
            sys.argv[1]
        except:
            print('No files given for conversion.')
            # self.pause_program(exit=True)
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
            # self.pause_program(exit=True)
            sys.exit()

        for i in range(0, len(files_to_convert)):
            source_file = files_to_convert[i]
            file_name = os.path.basename(source_file)
            print(f'Source file: {file_name}')

        return files_to_convert


    def parse_file_name(self, file_name):
        '''
        Retrieves tokens from the source file's name
        Tokens in file name will create the hierarchy for the converted files
        File name convention: <sequence_id>_<scene_id>_<suffix>.txt

        sequence_id = alpha coded with any length (RSY, P, TART, etc)
        scene_id = number coded with 3 places
        suffix = optional token or identifier

        return name_tokens
        '''
        name_tokens = self.name_tokens
        name_keys = list(name_tokens.keys())
        file_name = file_name.replace(' ', '_')
        file_name_parts = file_name.split('_')

        for i in range(0, len(file_name_parts)):
            name_tokens[name_keys[i]] = file_name_parts[i]

        print(f'This is the file name now: {file_name}')
        print('''This is the naming convention:\n
                 Sequence: {sequence_id} 
                 Scene: {scene_id} 
                 Suffix: {suffix} \n'''.format(**name_tokens))

        return name_tokens


    def set_file_destination(self, name_tokens):
        '''
        Create the 
        '''
        seq_token = name_tokens.get('sequence_id')
        scene_token = name_tokens.get('scene_id')
        suffix_token = name_tokens.get('suffix')

        destination = f'{self.root_dir}\\{seq_token}\\{scene_token}'
        print(f'Destination: {destination}')

        return destination


    def create_row(self, row_items):
        '''
        Creates row for csv based off items
        '''
        row_string = ''

        if row_items == None:
            print('There is nothing in this list.')
            # self.pause_program()
            sys.exit()
        
        if not type(row_items) == list:
            print('This is not a list.')
            # self.pause_program()
            sys.exit()

        for i in range(0, len(row_items)):
            current_item = row_items[i]
            row_string += f'{current_item},'

        print(f'This is the row_string: {row_string}')

        return row_string


    def create_converted_file(self, input_file_name, destination, 
                              extension='.csv'):
        '''
        Converts the .txt input file and it lines into a format for UE
        Default file type for the converted file: .csv

        return: converted_file
        '''
        # input_file_name, converted_file, scene_id, starting_line_id 
        converted_file_name = '{destination}\\input_file_name{extension}'
        try:
            open(converted_file_name, 'x')
        except:
            print(f'''{converted_file_name} already exists. Exiting 
                      the tool...''')
            self.pause_program(exit=True)

        open(converted_file_name, 'w')



        # first_row = create_row(self.COLUMN_TITLES)
        # converted_file.write(first_row)
        # starting_line_id = 1
        # scene_id += 1
        return converted_file

        # try:
        #     converted_file.close()
        # except:
        #     pass


    def format_name(self, character_name):
        '''
        Format's name to use Title Casing
        '''
        character_name = str(character_name)
        if len(character_name) >= 2:
            #keep first letter capitalized
            character_name = character_name[0] + character_name[1:].lower() 
            character_name = character_name
        return character_name


    def pause_program(self, exit=False):
        try:
            pause = raw_input('Press the <ENTER> key to continue...')
        except:
            pause = input('Press the <ENTER> key to continue...')
        if exit:
            sys.exit()

    def run_warning():
        pass



# ==============================TESTING=================================
    def run_script_converter(self):
        print('\nThis is a test of the script converter tool...\n')

        files_to_convert = self.get_files_to_convert()


        name_tokens = self.parse_file_name(file_name='RSY 012 test')
        destination = self.set_file_destination(name_tokens)


        # print(type(self.COLUMN_TITLES)
        # create_row(self.NOTHING_AT_ALL)

        # self.create_csv_file()

ScriptConverter = ScriptConverter()
ScriptConverter.run_script_converter()

# ======================================================================

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


# create_csv_file()


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
