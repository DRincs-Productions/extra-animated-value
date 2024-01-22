# Extra Animated Value

#### Note: All you really need are the files in [The game folder](game). Just a few sample images and a small script file. They can be dropped into a new or existing project and a label called to view an example (details in the .rpy file). 
#### Alternatively, just clone the lot as a zip from [The Repository Main Page](https://github.com/RenpyRemix/extra-animated-value)

Extending AnimatedValue for Bars.

![extra_animated_value](https://github.com/DRincs-Productions/extra-animated-value/assets/67595890/847a65c0-6676-440c-b608-6a39d43a18fd)


###### Note: This gif (limited to 256 colours) is not as smooth or pretty as an in-game bar would be.

As you may or may not know, AnimatedValue is pretty limited in what it allows. Internally it just holds a value and an old value then uses a linear progression to move from one to the other over a set duration that is independent of the size of the change.

This extends that fairly limited class and allows:

- Querying (and thus display) of the current value as it changes.
- Facility to use a warper to control the movement curve.
- Ability to set a duration for the full range to change and use times as proportions of that for non full changes.
- Dynamic Text methods to easily display values taken from the class.
- A Displayable designed to help make bar images more dynamic.



### Important Reading:

The overview of the system is more fully explained in [Explain ExtraAnimatedValue](explain_extra_animated_value.md)

The additional image displayable is explained in [Explain ValueImage](explain_value_image.md)

[![Support me on Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/bePatron?u=19978585)

### Please note:

The way that some parts of this approach work might not be suitable for complete beginners. As such it will likely require some knowledge of Ren'Py in order to extend it to your particular needs. 

Though I have tried to explain it as simply as possible, I will not be available to help extend it unless under a paid contract.
Basically, if you want it to do more, you are expected to know enough Ren'Py to handle that yourself (or consider paying someone)
