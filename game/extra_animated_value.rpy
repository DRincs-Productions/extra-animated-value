

            ###########################################
            #                                         #
            #           To use in your game           #
            #                                         #
            #  AnimatedValue and this extension use   #
            #  the screen redraw to replace themself  #
            #  and update their display.              #
            #                                         #
            #  As such, the instance should be        #
            #  created within the screen that         #
            #  displays the bar itself.               #
            #                                         #
            #  The example here shows 3 bars all      #
            #  using the same variable.               #
            #  You should use a similar approach for  #
            #  your bar or bars                       #
            #                                         #
            ###########################################

    # jump to or call extra_animated_value_example to view

    # You can delete these examples once you have your bars 
    # working how you want them.


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


            ###########################################
            #                                         #
            #   You can delete the examples above     #
            #   once you are happy                    #
            #                                         #
            ###########################################



            ###########################################
            #                                         #
            #  An extended AnimatedValue class for    #
            #  use with bars and vbars.               #
            #  Allowing several extra features as     #
            #  outlined in the docstring              #
            #                                         #
            ###########################################


init -1499 python:

    @renpy.pure
    class ExtraAnimatedValue(AnimatedValue):
        """
        This extends AnimatedValue to allow:
            Querying of the current value at any point in time 
            Setting delay based on the full range
            Allowing a warper to control animation movement
            A few properties for returning current values
            Dynamic text displayables to track changing values

        :doc: value

        This animates a value, taking `delay` seconds to vary the value from
        `old_value` to `value`.

        `value`
         The value itself, a number.

        `range`
         The range of the value, a number.

        `delay`
         The time it takes to animate the value, in seconds. Defaults
         to 1.0.

        `range_delay`
         The time it takes to animate the value, in seconds across the full
         range. Overrides `delay` if set. Defaults to None

         `warper`
         String warper name to use to animate between values

        `old_value`
         The old value. If this is None, then the value is taken from the
         AnimatedValue we replaced, if any. Otherwise, it is initialized
         to `value`.
        """

        def __init__(self, value=0.0, range=1.0, delay=1.0, 
                           old_value=None, range_delay=None,
                           warper="linear"):
            if old_value == None:
                old_value = value

            self.value = value
            self.current_value = value
            self.range = range
            self.delay = delay
            self.range_delay = range_delay or None
            self.old_value = old_value
            self.start_time = None
            self.warper = warper

            self.adjustment = None

        @property
        def percent(self):
            """
            Percent expressed as a float between 0.0 and 1.0
            (suitable for use with PyFormat :.01% syntax)
            """
            return float(self.current_value) / float(self.range)

        def text(self, format="{.current_value:.0f}", **kwargs):
            return DynamicDisplayable(self.dynamic_text, 
                                      format=format, 
                                      **kwargs)

        def dynamic_text(self, st, at, **kwargs):
            value = kwargs.pop('format', "{.current_value:.0f}").format(self)
            delay = (0.1 if self.value == self.current_value else 0.02)
            return Text(value, **kwargs), delay

        def periodic(self, st):

            if self.range < self.value:
                self.value = self.range

            if self.start_time is None:
                self.start_time = st

            if self.value == self.old_value:
                return

            if self.range_delay is not None:

                self.delay = self.range_delay \
                           * ( abs(self.old_value - self.value) 
                               / float(self.range) )

            base_fraction = (st - self.start_time) / self.delay
            base_fraction = min(1.0, base_fraction)

            if base_fraction == 1.0:

                self.current_value = self.value

            else:

                fraction = renpy.atl.warpers[self.warper](base_fraction)

                self.current_value = self.old_value \
                                   + fraction * (self.value - self.old_value)

            self.adjustment.change(self.current_value)

            if base_fraction != 1.0:
                return 0
