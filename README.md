# carbon
This is a Python utilities module developed by the [author](https://nvfp.github.io/about) that bundles functions used across many of his projects.

## Installation
- Manual: Download this repository and save it to your machine (e.g. ~/code/carbon)

## Try it
```python
from carbon.ffmpeg import get_audio_sample_rate
from carbon.gui.button import Button
from carbon.time import get_sexagecimal
from carbon.utils import minmax_normalization
```

## Troubleshoot
- If Python can't find the module, as indicated by `ModuleNotFoundError: No module named 'carbon'`, try putting it in Python's standard folder for external libraries (~/Python3/Lib/site-packages).