SHELL := /bin/bash
IMPORT_DIR := $(shell cat ./flashcards.properties | grep "import.dir" | cut -d '=' -f2 2> /dev/null)
ANKI_MEDIA_DIR := $(shell cat ./flashcards.properties | grep "anki.media.dir" | cut -d '=' -f2 2> /dev/null)

.PHONY: all
all: flashcards

# Sets up project environment
.PHONY: setup
setup:
	@echo "Give input WITHOUT using variables such as HOME. Do NOT use those."
	@read -p "Directory to import flashcards and gifs from:" importdir; \
  echo "import.dir=$$importdir" >> flashcards.properties
	@read -p "Directory to export Anki media to:" ankimediadir; \
  echo "anki.media.dir=$$ankimediadir" >> flashcards.properties
	pip3 install -r requirements.txt
	cat ./flashcards.properties
	@echo "Setup done!"

# Imports and generates flashcards from CSV
.PHONY: flashcards
flashcards:
	@[[ ! -z "$(DECK)" ]] || (echo "DECK must be defined. Run make DECK='my deck'"; exit 1)
	python3 import-flashcards.py -i "$(IMPORT_DIR)" -a "$(ANKI_MEDIA_DIR)" -f "ASL N00b" "$(DECK)"
