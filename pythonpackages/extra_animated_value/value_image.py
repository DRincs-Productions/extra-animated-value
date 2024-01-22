import renpy.exports as renpy
from renpy.store import Transform

class ValueImage(renpy.Displayable):
    """
    A displayable that returns an image based on
    values taken from a reference object (ExtraAnimatedValue)

    @value_object:
        object that holds the relevant values 
        (.percent, .value, .current_value)
        the ExtraAnimatedValue object

    @images:
        the images 
        Either just image references or tuples of name and position
        "1.png", "2.png"
        ## will dissolve between 1.png and 2.png across the range
        or
        ("1.png", 0.0), ("2.png", 0.8), ("3.png", 1.0)
        # will dissolve between 1.png and 2.png across the first 80%
        # of range then dissolve between 2.png and 3.png across rest

    @kwargs:
        dissolve: boolean - default True
    """

    def __init__(self, value_object, *images, **kwargs):

        super(ValueImage, self).__init__(**kwargs)

        self.value_object = value_object

        self.images = list(images)

        for idx, i in enumerate(self.images):

            if not isinstance(i, (list, tuple)):

                self.images[idx] = [
                    i, (float(idx) * (1.0 / (len(self.images) - 1)))]

            else:

                self.images[idx] = list(self.images[idx])

            self.images[idx][0] = renpy.displayable(self.images[idx][0])

        self.dissolve = kwargs.get("dissolve", True)


    def render(self, width, height, st, at):

        self.old_value = getattr(self.value_object, "percent")

        layers = [self.images[0][0]]

        use_perc = self.old_value 

        for img, perc in self.images:

            if perc <= self.old_value:

                layers[0] = img
                use_perc = perc

            else:

                if self.dissolve:

                    ratio = (float(self.old_value - use_perc) 
                                / (perc - use_perc))

                    if ratio > 0.01:

                        layers.append(renpy.render(
                            Transform(img, alpha=ratio), 
                            width, height, st, at))

                break

        layers[0] = renpy.render(layers[0], width, height, st, at)

        # Create the render we will return.
        render = renpy.Render(*layers[0].get_size())

        for k in layers:

            render.blit(k, (0, 0))

        if (getattr(self.value_object, "value") 
            != getattr(self.value_object, "current_value")):

            renpy.redraw(self, 0)

        # Return the render.
        return render


    def event(self, ev, x, y, st):

        return

    def visit(self):

        return [k[0] for k in self.images]
