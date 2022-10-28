SHELL := /bin/bash
IMPORT_DIR := $(shell cat ./flashcards.properties | grep "import.dir" | cut -d '=' -f2 2> /dev/null)
GIF_DIR := $(shell cat ./flashcards.properties | grep "gif.dir" | cut -d '=' -f2 2> /dev/null)

.PHONY: all
all: flashcards

# Sets up project environment
.PHONY: setup
setup:
	@echo "Give input WITHOUT using variables such as HOME. Do NOT use those."
	@read -p "Default directory to import flashcards from:" importdir; \
  echo "import.dir=$$importdir" >> flashcards.properties
	@read -p "Default directory to pull gifs from:" gifdir; \
  echo "gif.dir=$$gifdir" >> flashcards.properties
	pip3 install -r requirements.txt
	cat ./flashcards.properties
	@echo "Setup done!"

.PHONY: flashcards
flashcards:
	python3 import-flashcards.py -i "$(IMPORT_DIR)" -g "$(GIF_DIR)" -f "ASL Vocab" "$(DECK)" 

.PHONY: asl-101-flashcards
asl-101-flashcards:
	$(MAKE) flashcards DECK="ASL 101"
