# carbon

This is a Python utilities module developed by the [author](https://nvfp.github.io) that bundles functions used across many of his projects.


## Installation

- Manual:
    - Download the latest `stable` version of this repository from the [releases](https://github.com/nvfp/carbon/releases) section.
    - Remove the version number (`carbon-1.x.x` -> `carbon`).
    - Place it in a folder where Python can recognize it as a module (e.g. `~/code/carbon`).


## Try it

- Basic:

    ```python
    from carbon.ffmpeg import get_audio_sample_rate
    from carbon.gui.button import Button
    from carbon.time import get_sexagecimal
    from carbon.utils import minmax_normalization
    ```
- Testing:
    ```sh
    python carbon\_testing\noise#__init__.py#perlin_noise_1d.py
    ```


## Compatibility purposes

TL;DR: It's recommended to always use the latest version.

**Minor** (argument order, scaling, generalization, etc.):
- `carbon.mdl.fn` -> `carbon.mdl.fn2`
- `carbon.mdl.fn` -> `carbon.mdl.v2.fn`

**Major** (data structure, component relations, overall usage, etc.):
- `carbon.mdl.Class` -> `carbon.mdl_v2.Class`
- `carbon.module` -> `carbon.module_new_name`

Mostly, basic functions (standalone, input-in-output-out) are the ones that undergo **Minor** changes. **Major** changes are mostly expected in structured things like big modules (interconnected functions, specific usage rules).


## FAQ

- Compatibility:
    - Latest version is always compatible with older versions (e.g., `carbon-1.3.0` works with projects that use `carbon-1.0.0` or `carbon-1.2.0`)


## Changelog

- 1.2.0 (May 12, 2023):
    - Updated `carbon.graph.graph2d.graph2d`: `carbon.graph.graph2d.v2`
    - Added `carbon/neuralnet/dense`
    - Added `carbon/neuralnet/convo`
    - Added `carbon/neuralnet/genetic`
    - Added `carbon/math`
    - Added `carbon/path`
    - Added `carbon/color`
    - Added `carbon/gui/shape`
    - Added `get_angle` and `rotate_coordinate` to `carbon/math`
    - Added `map_range` to `carbon/utils`
    - New methods for `carbon.gui.label.Label`: `set_font`, `set_font_by_id`, `set_fg`, `set_fg_by_id`
- 1.1.1 (2023 May 7):
    - Resolved the conflict between `Button.tags` and `self.tags`.
    - Added new arguments to `carbon.gui.label.Label` (`bd`, `bd_width`, `wraplength`, `padx`, `pady`)
- 1.1.0 (2023 May 4):
    - added `carbon/quick_visual`, `carbon/graph`, and `carbon/noise` modules


## Troubleshoot

- If Python can't find the module, as indicated by `ModuleNotFoundError: No module named 'carbon'`, try putting it in Python's standard folder for external libraries (`~/Python3/Lib/site-packages`).
- To report bugs/issues or ask questions, you can reach me [here](https://nvfp.github.io/contact) or open an issue/pull request.


## License

This project is licensed under the MIT license.