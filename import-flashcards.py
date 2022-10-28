import argparse
import os
import csv
import re
import shutil
from jinja2 import FileSystemLoader, Environment

SIGN_VARIATION_REGEX = re.compile("\(.+\)")

def get_gif_file_name(sign):
    words = sign.upper().strip().split(" ")
    file_sign_name = words[0]
    for word in words[1:]:
        if not SIGN_VARIATION_REGEX.match(word):
            file_sign_name += "-" + word

    return "sign_{}.gif".format(file_sign_name)

def get_flashcards(csv_file_path, flashcards_folder, flashcards_deck, gif_folder):
    flashcards = []
    csv_file_name = os.path.basename(csv_file_path)
    tag = os.path.splitext(csv_file_name)[0]
    # Ignore hidden files
    if not csv_file_name.startswith('.'):
        print("Reading {}".format(csv_file_path))
        with open(csv_file_path) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader: 
                flashcard = {"tag": tag, "deck": flashcards_deck}
                sign = row[0]
                flashcard['sign'] = sign
                if len(row) > 1:
                    flashcard['iframe'] = row[1]
                flashcards.append(flashcard)
                # Add local gif file for word if it exists
                gif_file_name = get_gif_file_name(sign)
                gif_file_path = os.path.join(gif_folder, gif_file_name)
                if os.path.exists(gif_file_path):
                    # Copy gif into project if it isn't already there
                    gif_destination_path = os.path.join(flashcards_folder, gif_file_name)
                    if not os.path.exists(gif_destination_path):
                        shutil.copy(gif_file_path, gif_destination_path)
                    flashcard['gif'] = gif_file_name

    return flashcards

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates ASL flashcards imprted from CSV')
    parser.add_argument('--import-folder', '-i', required=True, type=str, help="Folder to CSV files to import as flashcards")
    parser.add_argument('--flashcards-folders', '-f', required=True, type=str, nargs="+", help="Path to directory to generate flashcards in")
    parser.add_argument('--gif-folder', '-g', required=True, type=str, help="Path to directory that contains gifs to add to flashcards")
    args = parser.parse_args()

    flashcards_path = "./{}".format("/".join(args.flashcards_folders))
    flashcards_deck = "::".join(args.flashcards_folders)
    flashcards = []
    for file_name in os.listdir(args.import_folder):
        file_path = os.path.join(args.import_folder, file_name)
        flashcards += get_flashcards(file_path, flashcards_path, flashcards_deck, args.gif_folder)
    
    
    jinja_loader = FileSystemLoader(searchpath="./{}".format(args.flashcards_folders[0]))
    jinja_env = Environment(loader=jinja_loader)
    template = jinja_env.get_template("Template Flashcard.md")
    for flashcard in flashcards:
        flashcard_file_name = flashcard['sign'].replace("/", "") + ".md"
        with open(os.path.join(flashcards_path, flashcard_file_name), 'w') as file:
            file.write(template.render(flashcard)) 
