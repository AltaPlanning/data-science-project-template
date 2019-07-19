# data-science-project-template
Repo-based template for Data Science projects that use Python and PgSQL


## MacOS Installation
Build a new virtual environment using `conda`, and add the `conda-forge` channel:
```bash
cpu:~ you$ conda create -n ds_projects python=3.6
cpu:~ you$ conda activate ds_projects
(ds_projects) cpu:~ you$ conda config --env --add channels conda-forge
```

Install the various open-source modules needed:
```bash
(ds_projects) cpu:~ you$ conda install ipython
(ds_projects) cpu:~ you$ conda install osmnx
(ds_projects) cpu:~ you$ conda install ipython
(ds_projects) cpu:~ you$ conda install python-igraph
(ds_projects) cpu:~ you$ conda install tqdm
(ds_projects) cpu:~ you$ conda install psycopg2
(ds_projects) cpu:~ you$ conda install geoalchemy2
(ds_projects) cpu:~ you$ conda install xlsxwriter
(ds_projects) cpu:~ you$ conda install xlrd
(ds_projects) cpu:~ you$ conda install -c plotly plotly_express
(ds_projects) cpu:~ you$ pip install PySimpleGUI
```

Install Alta's `data-science` and Chester's `streetspace` packages:
```bash
(ds_projects) cpu:~ you$ pip install git+https://github.com/chesterharvey/StreetSpace.git
(ds_projects) cpu:~ you$ pip install git+https://github.com/AltaPlanning/data-science.git
```

## Refreshing modules
If the module was installed via `pip`, use the following commands to update the `data-science` or `streetspace` packages:
```bash
(ds_projects) cpu:~ you$ pip uninstall alta_data_science
(ds_projects) cpu:~ you$ pip install git+https://github.com/AltaPlanning/data-science.git
```
