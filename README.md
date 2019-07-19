# data-science-project-template
Repo-based template for Data Science projects that use Python and PgSQL


## MacOS Installation
Build a new virtual environment using `conda`, and add the `conda-forge` channel:
```bash
aaron-at-work:~ aaronfraint$ conda create -n ds_projects python=3.6
aaron-at-work:~ aaronfraint$ conda activate ds_projects
(ds_projects) aaron-at-work:~ aaronfraint$ conda config --env --add channels conda-forge
```

Install the various open-source modules needed:
```bash
(ds_projects) aaron-at-work:~ aaronfraint$ conda install ipython
(ds_projects) aaron-at-work:~ aaronfraint$ conda install osmnx
(ds_projects) aaron-at-work:~ aaronfraint$ conda install ipython
(ds_projects) aaron-at-work:~ aaronfraint$ conda install python-igraph
(ds_projects) aaron-at-work:~ aaronfraint$ conda install tqdm
(ds_projects) aaron-at-work:~ aaronfraint$ conda install psycopg2
(ds_projects) aaron-at-work:~ aaronfraint$ conda install geoalchemy2
(ds_projects) aaron-at-work:~ aaronfraint$ conda install xlsxwriter
(ds_projects) aaron-at-work:~ aaronfraint$ conda install xlrd
(ds_projects) aaron-at-work:~ aaronfraint$ conda install -c plotly plotly_express
(ds_projects) aaron-at-work:~ aaronfraint$ pip install PySimpleGUI
```

Install Alta's `data-science` and Chester's `streetspace` packages:
```bash
(ds_projects) aaron-at-work:~ aaronfraint$ pip install git+https://github.com/chesterharvey/StreetSpace.git
(ds_projects) aaron-at-work:~ aaronfraint$ pip install git+https://github.com/AltaPlanning/data-science.git
```