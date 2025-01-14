
# Extra Animated Value

Extending AnimatedValue for Bars.

![extra_animated_value](https://github.com/DRincs-Productions/extra-animated-value/assets/67595890/847a65c0-6676-440c-b608-6a39d43a18fd)

( Note: This gif (limited to 256 colours) is not as smooth or pretty as an in-game bar would be. )

As you may or may not know, AnimatedValue is pretty limited in what it allows. Internally it just holds a value and an old value then uses a linear progression to move from one to the other over a set duration that is independent of the size of the change.

This extends that fairly limited class and allows:

- Querying (and thus display) of the current value as it changes.
- Facility to use a warper to control the movement curve.
- Ability to set a duration for the full range to change and use times as proportions of that for non full changes.
- Dynamic Text methods to easily display values taken from the class.
- A Displayable designed to help make bar images more dynamic.

where you can find the images for the bar: [life bar](https://www.freepik.com/search?format=search&query=life%20bar&type=vector)

## Documentation

**[Wiki](https://github.com/DRincs-Productions/extra-animated-value/wiki)**


## Install LTS Version

To install a precise version install it manually: [Releases](https://github.com/DRincs-Productions/NQTR-System/releases).

But I recommend you to use git submodule:

```bash
git submodule add -b python-lib -- https://github.com/DRincs-Productions/extra-animated-value 'pythonpackages/extra_animated_value'

```

**AND** create a empty file `__init__.py` into `pythonpackages/` so `pythonpackages/__init__.py`.


## Please note

The way that some parts of this approach work might not be suitable for complete beginners. As such it will likely require some knowledge of Ren'Py in order to extend it to your particular needs.

Though I have tried to explain it as simply as possible, I will not be available to help extend it unless under a paid contract.
Basically, if you want it to do more, you are expected to know enough Ren'Py to handle that yourself (or consider paying someone)
