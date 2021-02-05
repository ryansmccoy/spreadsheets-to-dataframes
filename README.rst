=======================================================================================
From Spreadsheets to DataFrames: Escaping Excel Hell with Python
=======================================================================================


`Presentation given at [STL Python] <https://www.meetup.com/STL-Python/events/265283397>`_

`Presentation given at Chicago Python Users Group [YouTube] <https://www.youtube.com/watch?v=CtN_EVqZ72s>`_

Details

A spreadsheet is a wonderful invention and an excellent tool for certain jobs. All too often, however, spreadsheets are called upon to perform tasks that are beyond their capabilities. It's like the old saying, 'If the only tool you have is a hammer, every problem looks like a nail.' But some problems are better addressed with a screwdriver, with glue, or with a swiss army knife.

Python is often called the Swiss army knife of the programming world, due to its versatility and flexibility in use. That's why it has become increasingly popular over time. Companies can adopt Python to perform some uniquely complex processes over the long-term.

During this talk, Ryan will discuss his firsthand account of Excel Hell and how he managed to escape it using Python. He will also discuss some of the relevant libraries he uses for web scraping, data processing, analysis, and visualization, including Requests, Pandas, Flask, and Airflow, as well as few strategies he uses when approaching problems with data.

Slides
======================


`Intro [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/Ed80otUOcyZIjnb3_wexK4gBal7c5NmQzUYX2MBaJbbYXg?e=sxgRbz>`_

`Excel to Python [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EfZc2NJYryhDsyaqFdSrN9UBNEqyTY9tUqd5b4c3sABprQ?e=TH17We>`_

`Python Libraries & Resources [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EdXZeyVGz7VFvZu6zCbEfw8BNUYPhT6SDejGtfw8I1_z1Q?e=xeQTL6>`_

`Data Management [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EX91EofZ7w9JunZvZ4wmZ8EBTWT5ztaRepBkooGdX0CohQ?e=q2B770>`_

Code
======================

`01-basics.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/01-basics.ipynb>`_

`02-webscraping.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/02-webscraping.ipynb>`_

`03-tidy-data.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/03-tidy-data.ipynb>`_

`04-pandas.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/04-pandas.ipynb>`_

`05-data-analysis.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/05-data-analysis.ipynb>`_

`06-data-visualizations.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/06-data-visualizations.ipynb>`_

Folders
===================================================

* 01-presentation-example  - examples used in presentation
* 02-selenium-examples - program that clicks through a calendar (written in javascript) and exports csv files
* 02-selenium-safari - program that logins to website, scrapes html from javascript generated page, cleans html, and exports to pdf files
* 02-webscrape-celery - example of that uses a message queue, and celery to download list of urls
* 04-other-analysis - examples of different quantitative notebooks
* 05-other-visualizations - examples of different data visualization tools
* 06-flask - different flask examples
* 07-airflow - example that uses airflow to download and store stock prices

# Quick Start Guides
======================

Setup Environment & Run Example  (Windows):
==================================================

.. code-block:: bash

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.8 pandas scipy numpy lxml jupyter matplotlib fbprophet -c conda-forge -y
    $ activate spreadsheets-to-dataframes
    $ conda install -c conda-forge fbprophet
    $ pip install -r requirements_dev.txt

Setup Environment & Run Example (Linux):
==================================================

.. code-block:: bash

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.8 pandas scipy numpy lxml jupyter matplotlib fbprophet -c conda-forge -y
    $ source activate spreadsheets-to-dataframes
    $ conda install -c conda-forge fbprophet
    $ pip install -r requirements_dev.txt

Running Jupyter Notebooks:

Navigate to directory:

.. code-block:: bash

    $ activate spreadsheets-to-dataframes
    $ jupyter notebook

If have installing any of the packages on Windows:

https://www.lfd.uci.edu/~gohlke/pythonlibs/

^ download it from here and then pip install the downloaded file:

    https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyflux

* Free software: MIT license


