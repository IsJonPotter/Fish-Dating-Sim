# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Crush")
define p = Character("Pwotagonist")


# The game starts here.

label start:

    scene bg room

    p "Alright!"

    p "Today's the day!"

    p "I'm gonna ask her out!"

    show thegirl

    c "Oh hi, Pwotagonist! What's up?"

    # This ends the game.

    return
