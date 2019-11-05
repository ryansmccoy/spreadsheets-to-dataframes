=======================================================================================
From Spreadsheets to DataFrames: Escaping Excel Hell with Python (Work in Progress)
=======================================================================================


`Presentation given at [STL Python] <https://www.meetup.com/STL-Python/events/265283397>`_

Details

A spreadsheet is a wonderful invention and an excellent tool for certain jobs. All too often, however, spreadsheets are called upon to perform tasks that are beyond their capabilities. It's like the old saying, 'If the only tool you have is a hammer, every problem looks like a nail.' But some problems are better addressed with a screwdriver, with glue, or with a swiss army knife.

Python is often called the Swiss army knife of the programming world, due to its versatility and flexibility in use. That's why it has become increasingly popular over time. Companies can adopt Python to perform some uniquely complex processes over the long-term.

During this talk, Ryan will discuss his firsthand account of Excel Hell and how he managed to escape it using Python. He will also discuss some of the relevant libraries he uses for web scraping, data processing, analysis, and visualization, including Requests, Pandas, Flask, and Airflow, as well as few strategies he uses when approaching problems with data.

`Intro [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_gotem_co/Ed80otUOcyZIjnb3_wexK4gBal7c5NmQzUYX2MBaJbbYXg?e=sxgRbz>`_

`Excel to Python [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_gotem_co/EfZc2NJYryhDsyaqFdSrN9UBNEqyTY9tUqd5b4c3sABprQ?e=TH17We>`_

`Python Libraries & Resources [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_gotem_co/EdXZeyVGz7VFvZu6zCbEfw8BNUYPhT6SDejGtfw8I1_z1Q?e=xeQTL6>`_

`Data Management [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_gotem_co/EX91EofZ7w9JunZvZ4wmZ8EBTWT5ztaRepBkooGdX0CohQ?e=q2B770>`_


`01-basics.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/01-basics.ipynb>`_

`02-webscraping.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/02-webscraping.ipynb>`_

`03-tidy-data.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/03-tidy-data.ipynb>`_

`04-pandas.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/04-pandas.ipynb>`_
`05-data-analysis.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/05-data-analysis.ipynb>`_
`06-data-visualizations.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/06-data-visualizations.ipynb>`_

# Quick Start Guides

#### Setup Environment & Run Example  (Windows):

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.7 pandas numpy lxml jupyter matplotlib -y
    $ activate spreadsheets-to-dataframes
    $ conda install -c conda-forge fbprophet
    $ pip install -r requirements_dev.txt

#### Setup Environment & Run Example (Linux):

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.7 pandas numpy lxml jupyter matplotlib -y
    $ source activate spreadsheets-to-dataframes
    $ conda install -c conda-forge fbprophet
    $ pip install -r requirements_dev.txt

* Free software: MIT license

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
