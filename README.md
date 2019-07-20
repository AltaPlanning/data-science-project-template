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

`pip`-only packages, including Alta's `data-science` and Chester's `streetspace`
```bash
(dsp) ~ pip install PySimpleGUI
(dsp) ~ pip install rinohtype
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
