init python:
    from pythonpackages.extra_animated_value.extra_animated_value import ExtraAnimatedValue
    from pythonpackages.extra_animated_value.value_image import ValueImage

default extra_animated_value_points = 500
default extra_animated_value_max = 1000


screen extra_animated_value_screen():

    $ bar_val = ExtraAnimatedValue(
                    value=extra_animated_value_points, 
                    range=extra_animated_value_max, 
                    range_delay=2.5,
                    warper="easein_elastic")

    $ bar_val2 = ExtraAnimatedValue(
                    value=extra_animated_value_points, 
                    range=extra_animated_value_max, 
                    range_delay=3.5,
                    warper="easein_bounce")

    $ bar_val3 = ExtraAnimatedValue(
                    value=extra_animated_value_points, 
                    range=extra_animated_value_max, 
                    range_delay=3.0,
                    warper="ease_quart")

    fixed:

        area (20, 20, 400, 400)

        vbox:

            spacing 30

            fixed:

                area (0,0, 400, 50)

                bar:
                    value bar_val
                    left_bar "images/bar/health_bar_400x50_left.png"
                    right_bar "images/bar/health_bar_400x50_right.png"
                    area (0,0, 400, 50)

                add bar_val.text(
                    "{0.current_value:.0f}/{0.range:.0f}",
                    size = 22,
                    color = "#DDE",
                    outlines = [(abs(1), "#222")],
                    bold = True,
                    xcenter = 0.5,
                    ycenter = 0.5)

            frame:

                area (0,0, 400, 50)

                bar:
                    value bar_val2
                    area (0,0, 392, 42)

                add bar_val2.text('{.percent:.01%}',
                    size = 22,
                    color = "#DDE",
                    outlines = [(abs(1), "#222")],
                    bold = True,
                    xcenter = 0.5,
                    ycenter = 0.5)

            fixed:

                area (0,0, 400, 75)

                bar:
                    value bar_val3
                    left_bar ValueImage(
                        bar_val3,
                        Transform("images/bar/hp_bar_red.png", zoom=0.5),
                        Transform("images/bar/hp_bar_yellow.png", zoom=0.5),
                        Transform("images/bar/hp_bar_green.png", zoom=0.5))
                    right_bar Transform("images/bar/hp_bar_blank.png", zoom=0.5)
                    area (0,0, 400, 75)

                add bar_val3.text(
                    "{0.current_value:.0f} hp",
                    size = 22,
                    color = "#FFF",
                    outlines = [(abs(2), "#000")],
                    bold = True,
                    xcenter = 0.5,
                    ycenter = 0.57)


label extra_animated_value_example:

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
