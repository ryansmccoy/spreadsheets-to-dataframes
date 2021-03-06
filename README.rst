=======================================================================================
From Spreadsheets to DataFrames: Escaping Excel Hell with Python
=======================================================================================

==============================================================================================================================================================================

`Pycon 2021 Tutorial Video [YouTube] - May 12, 2021 <https://www.youtube.com/watch?v=llgTl9BDuKw>`_


Other Presentations:

`STL Python Presentation [YouTube] <https://www.meetup.com/STL-Python/events/265283397>`_

`Chicago Python Users Group [YouTube] <https://www.youtube.com/watch?v=CtN_EVqZ72s>`_

Details

A spreadsheet is a wonderful invention and an excellent tool for certain jobs. All too often, however, spreadsheets are called upon to perform tasks that are beyond their capabilities. It’s like the old saying, 'If the only tool you have is a hammer, every problem looks like a nail.' However, some problems are better addressed with a screwdriver, with glue, or with a Swiss Army Knife.

Python is described by some in the programming world as the Swiss Army Knife of programming languages because of its unrivaled versatility and flexibility in use. This allows its users to solve complex problems relatively easily compared with other programming languages and is one of the reasons why Python has become increasingly popular over time.

In this tutorial, we’ll briefly discuss spreadsheets, signs that you might be living in “Excel Hell”, and then we’ll spend the rest of the time learning how to escape it using Python.

In the first section, we’ll extend on what spreadsheet users already know about cells, rows, columns, and formulas, and map them to their Python equivalent, such as variables, lists, dictionaries, and functions. At the end of this section, we’ll do an interactive exercise and learn how we can perform a simple calculation, similar to one you might do in Excel, but instead using Python.

In the second section, we’ll discuss (and attempt) how we can perform more complex tasks including web scraping, data processing, analysis, and visualization, by utilizing a few popular 3rd party libraries used including Requests, Pandas, Flask, Matplotlib, and others.

In the last section, we’ll round out our discussion with a few important concepts in data management, including concept of tidy data, building a data pipeline, and a few strategies (and packages) to use when approaching various data problems, including demo using Apache Airflow.

Slides
======================

`Intro [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/Ed80otUOcyZIjnb3_wexK4gBal7c5NmQzUYX2MBaJbbYXg?e=sxgRbz>`_

`Excel to Python [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EfZc2NJYryhDsyaqFdSrN9UBNEqyTY9tUqd5b4c3sABprQ?e=TH17We>`_

`Python Libraries & Resources [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EdXZeyVGz7VFvZu6zCbEfw8BNUYPhT6SDejGtfw8I1_z1Q?e=xeQTL6>`_

`Data Management [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EX91EofZ7w9JunZvZ4wmZ8EBTWT5ztaRepBkooGdX0CohQ?e=q2B770>`_

Tutorial Code
======================

Section 1 - Python Fundamentals for an Excel User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`01 basics_but_important_stuff.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1-01-basics_but_important_stuff.ipynb>`_

`02 files_lists_dictionaries.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1-02-files_lists_dictionaries.ipynb>`_

Section 1 - Challenges
~~~~~~~~~~~~~~~~~~~~~~~

`challenge_1.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_1.py>`_

`challenge_1_answer.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_1_answer.py>`_

`challenge_2.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_2.py>`_

`challenge_2_answer.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_2_answer.py>`_

`challenge_3.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_3.py>`_

`challenge_3_answer.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section1_challenge_3_answer.py>`_

Section 2 - Real-World Python Example for an Excel User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`01-real-world-example.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section2-01-real-world-example.py>`_

`02-real-world-example-refactored.py <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section2-02-real-world-example-refactored.py>`_

Section 2 - Challenge
~~~~~~~~~~~~~~~~~~~~~~~

`section2_challenge.rst <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/section2_challenge.rst>`_


Section 3 - Best Practices in Python & Data for an Excel User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Data Management [Slides] <https://gotemstl-my.sharepoint.com/:p:/g/personal/ryan_mccoystl_com/EX91EofZ7w9JunZvZ4wmZ8EBTWT5ztaRepBkooGdX0CohQ?e=q2B770>`_

`07-airflow <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/07-airflow>`_

STL Python - Talk Code
======================

`01-basics.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/01-basics.ipynb>`_

`02-webscraping.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/02-webscraping.ipynb>`_

`03-tidy-data.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/03-tidy-data.ipynb>`_

`04-pandas.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/04-pandas.ipynb>`_

`05-data-analysis.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/05-data-analysis.ipynb>`_

`06-data-visualizations.ipynb <https://github.com/ryansmccoy/spreadsheets-to-dataframes/blob/master/06-data-visualizations.ipynb>`_

STL Python - Folders
===================================================

* 01-basics - examples used in presentation
* 02-webscraping - program that clicks through a calendar (written in javascript) and exports csv files
* 02-selenium-safari - program that logins to website, scrapes html from javascript generated page, cleans html, and exports to pdf files
* 02-webscrape-celery - example of that uses a message queue, and celery to download list of urls
* 04-other-analysis - examples of different quantitative notebooks
* 05-other-visualizations - examples of different data visualization tools
* 06-flask - different flask examples
* 07-airflow - example that uses airflow to download and store stock prices

Quick Start Guides
======================


`Install Anaconda & Pycharm <https://medium.com/@GalarnykMichael/setting-up-pycharm-with-anaconda-plus-installing-packages-windows-mac-db2b158bd8c>`_

* Anaconda = manages your Python environments

* Pycharm = code editor

`Install Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ - Allows you to git clone/download Github Projects'

Setup Environment & Run Example  (Windows):
==================================================

.. code-block:: bash

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.8 pandas scipy numpy lxml jupyter matplotlib -y
    $ activate spreadsheets-to-dataframes
    $ pip install -r requirements_dev.txt

Setup Environment & Run Example (Linux):
==================================================

.. code-block:: bash

    $ git clone https://github.com/ryansmccoy/spreadsheets-to-dataframes.git
    $ cd spreadsheets-to-dataframes
    $ conda create -n spreadsheets-to-dataframes python=3.8 pandas scipy numpy lxml jupyter matplotlib -y
    $ source activate spreadsheets-to-dataframes
    $ pip install -r requirements_dev.txt

Running Jupyter Notebooks:
==================================================

Navigate to spreadsheet-to-dataframe directory/folder:

.. code-block:: bash

    $ activate spreadsheets-to-dataframes
    $ jupyter notebook

(Optional) Install Docker to Run Airflow Example
===================================================

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

Python Books & Videos:
===================================================

`(Book) Python Crash Course, 2nd Edition <https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280>`_

`(Book) Introducing Python: Modern Computing in Simple Packages <https://www.amazon.com/Introducing-Python-Modern-Computing-Packages-ebook/dp/B0815R5543>`_

`(Book) Learning Python, 5th Edition <https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730>`_

`(Book) Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners <https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922>`_

`(Book) Think Python: How to Think Like a Computer Scientist <https://www.amazon.com/Think-Python-Like-Computer-Scientist-ebook/dp/B018UXJ9EQ>`_

`(Book) The Quick Python Book (Book) <https://www.amazon.com/Quick-Python-Book-Naomi-Ceder/dp/1617294039>`_

`(Book) Serious Python: Black-Belt Advice on Deployment, Scalability, Testing, and More  <https://www.amazon.com/Serious-Python-Black-Belt-Deployment-Scalability/dp/1593278780>`_

`(Github) A Whirlwind Tour of Python  <https://github.com/jakevdp/WhirlwindTourOfPython>`_

`(Github) Python Data Science Handbook  <https://github.com/jakevdp/PythonDataScienceHandbook>`_

`(Github) Introduction to Python <https://github.com/ipeirotis/introduction-to-python>`_

Cookiecutter:
===================================================

$ pip install cookiecutter

Resources:

https://github.com/cookiecutter/cookiecutter

https://github.com/audreyfeldroy/cookiecutter-pypackage

https://towardsdatascience.com/cookiecutter-creating-custom-reusable-project-templates-fc85c8627b07

Requests
===================================================

$ pip install requests

Resources:

https://python.readthedocs.io/en/stable/library/stdtypes.html

https://realpython.com/python-requests/

Have you mastered Requests? Then you should check out multithreading, concurrency, asyncio, message queues, parallelism.

https://yasoob.me/2019/05/29/speedingw-up-python-code-using-multithreading/

https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

https://creativedata.stream/multi-threading-api-requests-in-python/

https://levelup.gitconnected.com/asynchronous-tasks-in-python-with-celery-rabbitmq-redis-480f6e506d76

https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/

https://codeburst.io/automated-web-scraping-with-python-and-celery-ac02a4a9ce51

https://github.com/ryansmccoy/zmq-high-speed-subs


Pandas
===================================================

$ pip install pandas

Resources:

`Dealing With Data <https://github.com/ipeirotis/dealing_with_data>`_

`Pandas Cookbook <https://github.com/jvns/pandas-cookbook>`_

`brandon-rhodes\pycon-pandas-tutorial <https://github.com/brandon-rhodes/pycon-pandas-tutorial>`_

`Python pandas Q&A video series <https://github.com/justmarkham/pandas-videos>`_

`Master Data Analysis with Python <https://github.com/tdpetrou/Learn-Pandas>`_

Have you mastered Pandas?  Then you check out Dask and Spark.

https://dask.org/

https://spark.apache.org/docs/latest/api/python/

Visualization:
===================================================

$ pip install matplotlib

Resources:

https://github.com/fasouto/awesome-dataviz

https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

https://www.toptal.com/designers/data-visualization/data-visualization-tools

https://realpython.com/pandas-plot-python/

Have you mastered Matplotlilb?  Then you should checkout Javascript, D3, React, Tableau

Flask:
===================================================

$ pip install flask

Resources:

https://www.fullstackpython.com/flask.html

https://blog.miguelgrinberg.com/

Have you mastered Flask?  Then you should checkout FastAPI, Javascript, Node, React
