# ASL N00b Notes
Notes and [flashcards]()<!--TODO: Add link to shared Anki decks--> by an ASL n00b for ASL n00bs. I am a hearing ASL student who is creating notes and flashcards as I learn to sign. Take everything here with a grain of salt because I am **not** an ASL expert and I am **not** a native signer. 

If you are able to, I highly recommend taking ASL courses taught by a Deaf or hard of hearing person at some point in your ASL learning journey. I personally recommend classes by [Queer ASL](https://www.queerasl.com/).

My notes are written in markdown for [Obsidian](https://obsidian.md/) and shared via Git. You can download the notes if you have [Obsidian and Git installed](https://desktopofsamuel.com/how-to-sync-obsidian-vault-for-free-using-git). My flashcards are exported from this project to [Anki](https://apps.ankiweb.net/).

## Generate Flashcards
Once you have the project setup, follow the steps below to generate flashcards. Git commit hooks and template comments will prompt you on when to use the plugin to generate Anki flashcards.

### Project Setup
The [Flashcards](https://github.com/reuseman/flashcards-obsidian) plugin for Obsidian is used to generate flashcards in [Anki](./ANKI.md). Install the [community plugin](https://help.obsidian.md/Advanced+topics/Community+plugins) and make sure it is working correctly.

This project also requires Python 3, Jinja, and custom configurations to generate flashcards. It also comes with version-controlled git hooks. To set all this up in your development environment for the project, run:
```bash
make setup
```

### Vocab Flashcards
To generate vocab flashcards, export a CSV in [this format](https://docs.google.com/spreadsheets/d/1wntkF6W-mNdyTxaEZI-RmvvdGeeDKY8iq9FHbYhtNog/edit?usp=sharing). Then, generate the flashcards into a sub-deck of `ASL N00b Flashcards` by passing the deck name to the following command:
```bash
make DECK="ASL N00b 1 (Baby's First Signs)"
```

### Trivia Flashcards
There is an [Obsidian template](https://help.obsidian.md/Plugins/Templates) for trivia flashcards. Create a new note in the `Trivia` folder for the appropriate deck and insert this template. Then, follow the instructions in the comments to fill out the remaining details for the card.