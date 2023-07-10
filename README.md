# watersort
To use, edit [main.py](https://github.com/joshuaSmith2021/watersort/blob/main/main.py). Add however many tubes are in the level.
You don't have to use variable names for the colors, I do it just to make it easy to see whats going on. To add a new color, just
create a new variable with a unique value, for example, `NEON = 214`.
Initialize tubes with the bottom layer in index 0. If a tube, for example, looks like this:

```
| BLUE |
| PINK |
| GRAY |
| RED  |
|------|
```

Then the tube declaration is `Tube(4, [RED, GRAY, PINK, BLUE])`. Be sure to initialize the two empty tubes as well, most likely
with `Tube(4, [])`.

Once you have entered your tubes, run `python3 main.py` to get the steps to solve the level. The output is a bunch of rows formatted like this:
`Source tube -> Destination tube (n = number of layers transferred)`

Note that this output is 1-indexed, so the first tube, which is technically index 0, will be shown as 1.

So, if you were moving two layers from tube index 0 to tube index 4, you would see `1 -> 5 (n = 2)`

I usually list the tubes as if I was reading a book, that is index 0 is the top left, index 1 is directly to the right of the top left, and
so on.
