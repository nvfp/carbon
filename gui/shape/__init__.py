import math as _math
import random as _random
import tkinter as _tk

from carbon.math import (
    get_angle as _get_angle,
    rotate_coordinate as _rotate_coordinate
)


class _Shape:

    page: _tk.Canvas = None
    @staticmethod
    def set_page(page: _tk.Canvas, /) -> None:
        _Shape.page = page


class Arrow(_Shape):

    arrows: dict[str, 'Arrow'] = {}
    arrow_tags: dict[str, list['Arrow']] = {}

    def __init__(
        self,
        from_x: int, from_y: int,
        to_x: int, to_y: int,
        /,
        color: str = '#ddd',
        width_rod: int = 1,
        width_tip: int = 2,
        tip_len: float = 20,
        tip_angle: float = 35,
        visible: bool = True,
        id: str | None = None,
        tags: str | list[str] | None = None,
    ) -> None:
        
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

        self.color = color
        self.width_rod = width_rod
        self.width_tip = width_tip
        self.tip_len = tip_len
        self.tip_angle = tip_angle

        self.visible = visible

        ## to make sure that we can modify a specific arrow without affecting the others
        if id is None:
            self.id = _random.randint(-10000, 10000)
            while self.id in Arrow.arrows:
                self.id = _random.randint(-10000, 10000)
        else:
            self.id = id
            if self.id in Arrow.arrows:
                raise ValueError(f'The Arrow\'s id {repr(id)} is duplicated.')
        Arrow.arrows[self.id] = self

        ## <tags>
        if type(tags) is str:
            self.tags = [tags]
        elif (type(tags) is list) or (type(tags) is tuple) or (tags is None):
            self.tags = tags
        
        if tags is not None:
            for tag in self.tags:
                if tag in Arrow.arrow_tags:
                    Arrow.arrow_tags[tag].append(self)
                else:
                    Arrow.arrow_tags[tag] = [self]
        ## </tags>

        ## init
        self._redraw()

    def _redraw(self):

        _Shape.page.delete(f'Arrow_{self.id}')

        if self.visible:
            _Shape.page.create_line(
                self.from_x, self.from_y,
                self.to_x, self.to_y,
                fill=self.color, width=self.width_rod, tags=f'Arrow_{self.id}'
            )

            ## <creating the tip>
            ## for `angle`: remember to flip the y-sign because tkinter's y-positive direction towards the bottom
            angle = _get_angle(self.from_x, -self.from_y, self.to_x, -self.to_y)
            
            tipx = self.tip_len*_math.sin(self.tip_angle*_math.pi/180)
            tipy = self.tip_len*_math.cos(self.tip_angle*_math.pi/180)
            
            ## Remember `tip_left` and `tip_right` with y-positive towards the top,
            ## as they transformed under normal Cartesian coordinates.
            tip_left = _rotate_coordinate(-tipx, -tipy, 0, 0, angle)
            tip_right = _rotate_coordinate(tipx, -tipy, 0, 0, angle)

            ## Revert to the tkinter coordinate scheme, where y-positive is oriented downwards.
            tip_left = (self.to_x+tip_left[0], self.to_y-tip_left[1])
            tip_right = (self.to_x+tip_right[0], self.to_y-tip_right[1])

            tip_points = [tip_left, (self.to_x, self.to_y), tip_right]
            _Shape.page.create_line(tip_points, fill=self.color, width=self.width_tip, tags=f'Arrow_{self.id}')
            ## </creating the tip>


    def set_visibility(self, visible: bool, /):
        if visible != self.visible:
            self.visible = visible
            self._redraw()

    @staticmethod
    def set_visibility_by_id(id: str, visible: bool, /):
        Arrow.arrows[id].set_visibility(visible)

    @staticmethod
    def set_visibility_by_tag(tag: str, visible: bool, /):
        for arrow in Arrow.arrow_tags[tag]:
            arrow.set_visibility(visible)

    @staticmethod
    def set_visibility_all(visible: bool, /):
        for arrow in Arrow.arrows.values():
            arrow.set_visibility(visible)