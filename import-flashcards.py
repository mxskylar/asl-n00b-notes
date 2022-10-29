import argparse
import os
import csv
import re
import shutil
from jinja2 import FileSystemLoader, Environment

def get_flashcard_files(csv_file_path, flashcards_folder, flashcards_deck, anki_media_folder):
    flashcards = {}
    csv_file_name = os.path.basename(csv_file_path)
    # Ignore hidden files
    if not csv_file_name.startswith('.'):
        print("Reading {}".format(csv_file_path))
        with open(csv_file_path) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader: 
                flashcard = {"deck": flashcards_deck}
                flashcard['sign'] = row[0]
                flashcard['gif'] = row[1]
                flashcard_file
                flashcard['tags'] = row[2:]
                flashcards.append(flashcard)
                
    return flashcards

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates ASL flashcards imported from CSV')
    parser.add_argument('--import-folder', required=True, type=str, help="Folder to CSV files to import as flashcards")
    parser.add_argument('--flashcard-folders', required=True, type=str, nargs="+", help="Path to directory to generate flashcards in")
    parser.add_argument('--new-sign-template', required=True, type=str, help="Name of new sign template file")
    parser.add_argument('--flashcard-template', required=True, type=str, help="Name of flashcard template file")
    parser.add_argument('--anki-media-folder', required=True, type=str, help="Path to Anki media directory")
    args = parser.parse_args()

    flashcards_path = "./{}".format("/".join(args.flashcard_folders))
    flashcards_deck = "::".join(args.flashcard_folders)
    flashcards = []
    for file_name in os.listdir(args.import_folder):
        file_path = os.path.join(args.import_folder, file_name)
        flashcards += get_flashcard_files(file_path, flashcards_path, flashcards_deck, args.anki_media_folder) 
    
    jinja_loader = FileSystemLoader(searchpath="./{}".format(args.flashcard_folders[0]))
    jinja_env = Environment(loader=jinja_loader)
    template = jinja_env.get_template(args.template)
    for flashcard in flashcards:
        flashcard_file_name = flashcard['sign'].replace("/", "") + ".md"
        with open(os.path.join(flashcards_path, flashcard_file_name), 'w') as file:
            file.write(template.render(flashcard)) 
