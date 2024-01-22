import renpy.exports as renpy
from renpy.store import DynamicDisplayable, Text

__all__ = [
    "ExtraAnimatedValue",
]

@renpy.pure
class ExtraAnimatedValue(renpy.AnimatedValue):
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
