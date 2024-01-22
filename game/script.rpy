# The script of the game goes in this file.

# The game starts here.

label start:

    scene expression "#777"

    show screen extra_animated_value_screen

    "Start"
    $ extra_animated_value_points += 150
    "..."
    $ extra_animated_value_points -= 450
    "..."
    $ extra_animated_value_points -= 200
    "..."
    $ extra_animated_value_points += 1000
    "..."
    $ extra_animated_value_points -= 450
    "..."
    $ extra_animated_value_points -= 450
    "..."
    $ extra_animated_value_points += 750
    "..."
    $ extra_animated_value_points -= 350
    "End"

    hide screen extra_animated_value_screen

    return
