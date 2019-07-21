# data-science-project-template
Repo-based template for Data Science projects that use Python and PgSQL

## Update the `sphinx` documentation as you go!

The initial `sphinx-quickstart` command has already been run,
but you'll want to continue commenting your code and rebuilding
the HTML-based documentation throughout your work.

To update the HTML build run:
```bash
(dsp) ~ sphinx-apidoc -f -e -M -o source/ ../
(dsp) ~ make html
```

___


## Python environment Installation

Build a new virtual environment named `dsp` using `conda`, and add the `conda-forge` channel:

```bash
~
~ conda create -n dsp python=3.6
~ conda activate dsp
(dsp) ~ conda config --env --add channels conda-forge
```

Install the various open-source modules needed:

General `python` tooling:
```bash
(dsp) ~ conda install ipython
(dsp) ~ conda install jupyter
(dsp) ~ conda install jupytext
```

Database i/o:
```bash
(dsp) ~ conda install psycopg2
(dsp) ~ conda install geoalchemy2
```

Excel file i/o:
```bash
(dsp) ~ conda install xlsxwriter
(dsp) ~ conda install xlrd
```

Data visualization:
```bash
(dsp) ~ conda install seaborn
(dsp) ~ conda install -c plotly plotly_express
```

General UI/feedback:
```bash
(dsp) ~ conda install tqdm
```

Documentation:
```bash
(dsp) ~ conda install sphinx
(dsp) ~ conda install sphinx_rtd_theme
```

Data analysis:
```bash
(dsp) ~ conda install python-igraph
(dsp) ~ conda install osmnx
(dsp) ~ conda install -c udst pandana
```

NOTES:
1. `python-igraph` is not available via `conda` on Windows
2. `osmnx` does not reliably install on Windows machines when
building environments with the `conda` installation packaged
with `ArcGIS Pro`/`arcpy`. If you want to build this environment to
include `arcpy` then you'll want to `pip install` a number of `.whl`
files first, including `GDAL`, `fiona`, `rtree`, `pyproj`, `shapely`.
  - After installing the `.whl` files with the processed described below,
 you'll then need to use `pip`:
  - `pip install osmnx`

If you experienced either issue, download the necessary `.whl` file(s) from
[here](https://www.lfd.uci.edu/~gohlke/pythonlibs).
There are a lot of files to choose from, but only one will work here.
First find the name of the pacakge you want to download.
Then find the one with `cp36` and `win_amd64` in the name.
As of 7/21/2019, the correct version of `igraph` is named
`python_igraph-0.7.1.post6-cp36-cp36m-win_amd64.whl`.
Move the downloaded file into your terminal's current
directory or `cd` into your `Downloads` folder. Install
the wheel with `pip` and use `TAB` completion to avoid
typing the full filename:
 - `pip install python_igraph-0.7.1.post6-cp36-cp36m-win_amd64.whl`


Finally, install `pip`-only packages, including Alta's `data-science` and Chester's `streetspace`
```bash
(dsp) ~ pip install PySimpleGUI
(dsp) ~ pip install git+https://github.com/chesterharvey/StreetSpace.git
(dsp) ~ pip install git+https://github.com/AltaPlanning/data-science.git
```
___

## Refresh environment modules as needed

For `pip install`-ed packages
(like `data-science` or `streetspace`),
use the following commands to update:
```bash
(dsp) ~ pip uninstall alta_data_science
(dsp) ~ pip install git+https://github.com/AltaPlanning/data-science.git
```
