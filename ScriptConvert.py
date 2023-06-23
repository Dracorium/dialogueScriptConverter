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
import tkinter #create dialog boxes

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

        # Constructing variables for tool
        # self.root_dir = 'X:\\Writing\\vnframework'
        self.root_dir = 'D:\\.tools\\dialogueScriptConverter\\samples\\root'
        self.name_tokens = dict(
            sequence = None,
            scene = None,
            suffix = None
            )
        self.files_to_convert = []



    def get_environment_variables(self, *args):
        pass


    def get_files_to_convert(self, *args):
        '''
        Will take any number of arguments for files to process and check
        their validity

        return: files_to_convert
        '''
        # sys.argv[0] accesses the file path of the script run

        # self.files_to_convert = []

        try:
            sys.argv[1]
        except:
            print('No files given for conversion.')
            # self.pause_program(exit=True)
            sys.exit()

        for i in range(1, len(sys.argv)):
            source = pathlib.Path(sys.argv[i])
            if source.exists():
                print(f'Source path found [{source}]')
                self.files_to_convert.append(source)
            else:
                print(f'Source file [{source}] NOT found.')

        try:
            self.files_to_convert[0]
        except:
            print('No valid files given for conversion')
            # self.pause_program(exit=True)
            sys.exit()

        # for i in range(0, len(self.files_to_convert)):
        #     source_path = self.files_to_convert[i]
        #     file_name = os.path.basename(source_path)
        #     print(f'Source file: {file_name}')


    def parse_file_name(self, source_name):
        '''
        Retrieves tokens from the source file's name
        Tokens in file name will create the hierarchy for the converted files
        File name convention: <sequence>_<scene>_<suffix>.txt

        sequence = alpha coded with any length (RSY, P, TART, etc)
        scene = number coded with 3 places (but could change)
        suffix = optional token or identifier

        return name_tokens
        '''
        name_tokens = self.name_tokens
        name_keys = list(name_tokens.keys())
        file_name = source_name.replace(' ', '_')
        name_parts = source_name.split('_')

        for i in range(0, len(name_parts)):
            name_tokens[name_keys[i]] = name_parts[i]

        print(f'This is the file name now: {file_name}')
        print('''This is the naming convention:\n
                 Sequence: {sequence} 
                 Scene: {scene} 
                 Suffix: {suffix} \n'''.format(**name_tokens))

        return file_name, name_tokens


    def set_file_destination(self, name_tokens):
        '''
        Create the directory for the destination of the converted file

        return: destination
        '''
        seq_token = name_tokens.get('sequence')
        scene_token = name_tokens.get('scene')
        suffix_token = name_tokens.get('suffix')

        destination = pathlib.Path(f'{self.root_dir}\\{seq_token}\\{scene_token}')
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


    def create_output_file(self, source_file, destination_path, 
                              extension='csv'):
        '''
        Converts the .txt/.ink input file and it lines into a format for UE
        Default file type for the converted file: csv

        return: output_file
        '''
        # source_file, output_file, scene, starting_line_id 
        # try:
        #     output_file.close()
        # except:
        #     pass
        file_name = f'{source_file}.{extension}'
        destination_file = destination_path / file_name

        destination_path.mkdir(parents=True, exist_ok=True)
        if destination_file.exists():
            print(f'{destination_file} already exists. Exiting the tool...')
            self.pause_program()

        with destination_file.open('w') as output_file:
            first_row = self.create_row(self.COLUMN_TITLES)
            output_file.write(first_row)

        return output_file


    def convert_script_lines(self, file):
        '''
        Crawl through each line in the source script file and
        translate formatting into a dictionary 

        return: line_string
        '''

        with file.open('r') as script_file:
            script_lines = script_file.readlines()

        #loop through each line, alter it, and write it to new file
        for line in script_lines:
            character_name = None
            dialogue = None
            event_flag = None

            # Check for comments, may have to alter this for ink language
            if line[0] == '/':  

            # All of this here is again original code that I'm just deciphering XD

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



    def format_name(self, character_name):
        '''
        Formats name to use Title Casing
        Weird that the original author didn't use this method.
        '''
        character_name = character_name.title()
        return character_name


    def pause_program(self, exit=False):
        try:
            pause = raw_input('Press the <ENTER> key to continue...')
        except:
            pause = input('Press the <ENTER> key to continue...')
        if exit:
            sys.exit()

    def run_warning(self):
        pass



# ==============================TESTING=================================
    def run_script_converter(self):
        print('\nThis is a test of the script converter tool...\n')

        self.get_files_to_convert()

        for file in self.files_to_convert:
            source_name = file.stem
            # print(f'Source file: {source_name}')
            file_name, name_tokens = self.parse_file_name(source_name)
            destination = self.set_file_destination(name_tokens)
            # output_file = self.create_output_file(file_name, destination)
            # print(output_file.name)
            self.convert_script_lines(file)





        # print(type(self.COLUMN_TITLES)
        # create_row(self.NOTHING_AT_ALL)

        # self.create_csv_file()

ScriptConverter = ScriptConverter()
ScriptConverter.run_script_converter()

# ======================================================================

'''
Everything down here is from the original code that this was forked from.
VN Framework is what we're using to manage dialogue and event data for the 
"visual novel" part of the game.

'''


# fileFound = False

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
