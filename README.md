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


## MacOS Installation

Build a new virtual environment named `dsp` using `conda`, and add the `conda-forge` channel:

```bash
~
~ conda create -n dsp python=3.6
~ conda activate dsp
(dsp) ~ conda config --env --add channels conda-forge
```

Install the various open-source modules needed:

```bash
(dsp) ~ conda install ipython
(dsp) ~ conda install osmnx
(dsp) ~ conda install ipython
(dsp) ~ conda install python-igraph
(dsp) ~ conda install tqdm
(dsp) ~ conda install psycopg2
(dsp) ~ conda install geoalchemy2
(dsp) ~ conda install xlsxwriter
(dsp) ~ conda install xlrd
(dsp) ~ conda install -c plotly plotly_express
(dsp) ~ conda install sphinx
(dsp) ~ conda install sphinx_rtd_theme
(dsp) ~ pip install PySimpleGUI
```

Install Alta's `data-science` and Chester's `streetspace` packages:

```bash
(dsp) ~ pip install git+https://github.com/chesterharvey/StreetSpace.git
(dsp) ~ pip install git+https://github.com/AltaPlanning/data-science.git
```
___

## Refresh modules as needed

If the module was installed via `pip`, use the following commands to update the `data-science` or `streetspace` packages:
```bash
(dsp) ~ pip uninstall alta_data_science
(dsp) ~ pip install git+https://github.com/AltaPlanning/data-science.git
```
