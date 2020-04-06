# IT For Business and Finance 2019/20

This repository (https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20) provides course informations and material supporting the first year master course of _IT For Business and Finance_ held at University of Siena in 2019/20.

**WARNING**: the course and this repository is under ongoing update.

---

**Symbols conventions**: updated sections/material in this README.md file will be highlited with &#x1F534; (a big red circle) displayed next to it.

- **Objectives**: To acquire practice in the use of financial models through Python programming language
- **Contents**: IT tools for modeling in Finance; Python
- **Teaching Methods**: Lessons in IT lab
- **Verification of learning**: written exam
- **Learning Material**:
  - Textbook: [Python for Finance, 2nd Edition](http://shop.oreilly.com/product/0636920117728.do), by Yves Hilpisch (O’Reilly). Copyright 2019 Yves Hilpisch, 978-1-492-02433-0.
  - All the reading and programming resources are listed in the class github repository: [IT-For-Business-And-Finance-2019-20](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20#resources)

---

# Table of contents
- [IMPORTANT COMMUNICATIONS](#bakeka)
- [Class Schedule](#class_schedule)
- [Contacts](#contacts)
- [Class Diary](#class_diary)
- [Resources](#resources)
  - [Reading](#reading_material)
  - [Programming](#programming_material)
- [Setup](#setup)

---

# IMPORTANT COMMUNICATIONS <a name="bakeka"></a> 
&#x1F534; The e-learning for IT for Business and Finance course at [http://elearning.unisi.it/moodle/](http://elearning.unisi.it/moodle/) (more info to come) is now active. You can access with your unisiPass credentials at [http://elearning.unisi.it/moodle/](http://elearning.unisi.it/moodle/) and type "IT pompa" in the "Cerca Corso" search window (top right corner of screen). E-learning material is under ongoing production and addition.

---

# Class Schedule <a name="class_schedule"></a> 
Classes start on Monday, February 24 2020 at 14:00 in _Aula informatica 1_. The timetable is:

Monday: 14:00-16:00\
Tuesday: 18:00-19:30 **this lesson starts sharply at 18:00**\
Wednesday: 14:00-16:00

Currently known amendements to this schedule are the following:

Monday 16/3: _Aula 1_\
Wednesday 4/3 and 18/3: _Aula 12_ 

---

# Contacts <a name="contacts"></a>
[Gabriele Pompa](https://www.linkedin.com/in/gabrielepompa/) (gabriele.pompa@unisi.it)

---

# Class Diary <a name="class_diary"></a>
This is the diary of the class. Here the topics covered during the lessons are listed, as well as the corresponding reading material.

**Conventions for reading material**: sections from 

**A**. the TextBook [Python for Finance (2nd ed.)](http://shop.oreilly.com/product/0636920117728.do) are labelled as _TB.ChapterNumber.SectionName_ to refer to a whole Section  (e.g. _TB.1.The Python Programming Language_) or as _TB.ChapterNumber.SubSectionName_ to refer to a particular sub-Section (e.g. _TB.1.Data-Driven Finance_ ).

**B**. the [Python Tutorial](https://docs.python.org/3.7/tutorial/) are labelled as _PyT.SectionNumber.SubSectionNumber.SubSubSectionNumber_ (SubSubSectionName)_ (e.g.: section 3.1.2 on [Strings](https://docs.python.org/3.7/tutorial/introduction.html#strings) is labelled _PyT.3.1.2 (Strings)_ ).

**C**. the [Numpy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html#quickstart-tutorial) are labelled as _Numpy Quickstart Tutorial - SectionName_ (list of SubSections).

**D**. the [Pandas - Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) are mentioned by section name (e.g.: [What kind of data does pandas handle?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)).

Below the list of lessons with relevant related material:

- **Lesson 1 (24/02)**: class presentation. introduction to: programming in Python, Anaconda platform, Jupyter Notebooks and interactive programming, Spyder IDE and programmatic programming, Python modules and `import` expressions.
  - _TB.1.The Python Programming Language_, _TB.1.Technology in Finance._
  - Lecture Notes **Introduction I** [.ipynb](Notebooks/Introduction_I.ipynb) | [.pdf](Notebooks/Printable/Introduction_I.pdf).
  
- **Lesson 2 (25/02)**:  motivations for adopting Python in Finance.
  - _TB.1.Python for Finance_, _TB.1.Data-Driven Finance_, _TB.2.Basic Operations with conda_, _TB.2.conda as a Virtual Environment Manager._ 
  
- **Lesson 3 (26/02)**:  random number generation. Histogram. Empirical distribution (normalized histogram). Template for `.py` files (scripts) in Spyder.
  - Spyder Template file [template_example.py](Scripts/template_example.py): use this file as a template example. Any script (`.py` file) that you write in Spyder IDE has to follow the structure of this template.
  - Lecture Notes **Introduction II** [.ipynb](Notebooks/Introduction_II.ipynb) | [.pdf](Notebooks/Printable/Introduction_II.pdf): Sec. 1, 2, 3.
  
- **Lesson 4 (2/03)**:  `int` data type, `.bit_length()` method for `int`, binary representation of integers (examples). `float` data type, issues of finite precision of internal binary representation of decimal numbers, arbitrary precision in Python ([`Decimal` module](https://docs.python.org/2/library/decimal.html)). Normal random variables in Python (Scipy [`norm` class](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)),`.pdf()` method of `norm` class, Normal fit to empirical distribution, `.fit()` method of `norm` class.
  - _TB.3.Integers_, _TB.3.Floats._
  - Lecture Notes **Introduction II** [.ipynb](Notebooks/Introduction_II.ipynb) | [.pdf](Notebooks/Printable/Introduction_II.pdf):: Sec. 4.
  - Lecture Notes **Basics_I___Data_Types** [.ipynb](Notebooks/Basics_I___Data_Types.ipynb) | [.pdf](Notebooks/Printable/Basics_I___Data_Types.pdf): Sec. 1 and 2.
  
- **&mu;&epsilon;&tau;&alpha;-Lesson 5 (3/03)**: gentle introduction to [github](https://github.com/). Teacher-Student(s) workflow (push-pull flow). Edit - Stage (`git add`) - Commit (`git commit`) pattern. Setup of a local development clone of a repository already established (hands-on example: `git clone` of the class repository into computers of _Aula Informatica 1_). Syncing local clone with updated class repository (the _hard_ way) with `git fetch` and `git reset`.   
  
- **Lesson 6 (4/03)**:  how to work this class, class/home study work-flow, how to take notes in class and at home (the `Personal_Notes` personal folder). Random number generation: Normal fit of a distribution, higher moments of a distribution (Skewness and Kurtosis), sample skewness and kurtosis, Jarque-Bera test of Normality, null-hypothesis and use of p-value of a test for decision-making.
  - [How To Work This Class](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md) tutorial.
  - Lecture Notes **Introduction II** [.ipynb](Notebooks/Introduction_II.ipynb) | [.pdf](Notebooks/Printable/Introduction_II.pdf):: Sec. 5 and 6.
  
- **Lesson 7 (9/03)**:  introduction to the e-learning platform [moodle](http://elearning.unisi.it/moodle/enrol/index.php?id=3326). `bool` data type, `while` loop, `if` statement. `str` data type (definition, indexing, slicing).
  - _TB.3.Basic Data Types_ (_TB.3.Excursion: Regular Expression_ is optional reading).
  - _[PyT.3.1.1](https://docs.python.org/3.7/tutorial/introduction.html#numbers) (Numbers),_ _[PyT.3.1.2](https://docs.python.org/3.7/tutorial/introduction.html#strings) (Strings),_ _[PyT.3.2](https://docs.python.org/3.7/tutorial/introduction.html#first-steps-towards-programming) (First Steps Toward Programming),_ _[PyT.4.1](https://docs.python.org/3.7/tutorial/controlflow.html#if-statements) (if Statements)._
  - Lecture Notes **Basics_I___Data_Types** [.ipynb](Notebooks/Basics_I___Data_Types.ipynb) | [.pdf](Notebooks/Printable/Basics_I___Data_Types.pdf): Sec. 3 and 4.
  - Videos: 
    - [Playlist: **e-learning general notes**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=2709cc15-21f0-4e84-96a0-ab8a00ca5a82)
    - [Playlist: **Lesson 7 - Data-Types**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=808049a7-dd1c-465d-bee5-ab8a00c96770)

- **Lesson 8 (10/03)**:  introduction to data-structures in Python, `tuple` data structure, `list` data structure, `for` loop, `dict` data structure, `set` data structure.
  - _TB.3.Basic Data Structures_ (_TB.3.Excursus: Functional Programming_ is optional reading).
  - _[PyT.3.1.3](https://docs.python.org/3.7/tutorial/introduction.html#lists) (Lists),_ _[PyT.4.2](https://docs.python.org/3.7/tutorial/controlflow.html#for-statements) (for Statements),_ _[PyT.4.3](https://docs.python.org/3.7/tutorial/controlflow.html#the-range-function) (The range() Function),_ _[PyT.4.4](https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) (break and continue Statemenents, and else Clauses on Loops),_ _[PyT.5.1](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists) (More on Lists),_ _[PyT.5.3](https://docs.python.org/3.7/tutorial/datastructures.html#tuples-and-sequences) (Tuples and Sequences),_ _[PyT.5.4](https://docs.python.org/3.7/tutorial/datastructures.html#sets) (Sets),_ _[PyT.5.5](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries) (Dictionaries)._
  - Lecture Notes **Basics_II___Data_Structures** [.ipynb](Notebooks/Basics_II___Data_Structures.ipynb) | [.pdf](Notebooks/Printable/Basics_II___Data_Structures.pdf)
  - Videos: 
    - [Playlist: **Lesson 8 - Data-Structures**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=45af903f-8dcd-4c21-b636-ab8a00ccfc3f)

- **Lesson 9 (11/03)**:  NumPy `ndarray` data-structure: arrays creation, indexing, slicing, iterating over arrays, basic operations, built-in methods, universal functions, shape manipulation, stacking of arrays
  - _TB.4.Regular Numpy Arrays,_ _TB.4.Basic Vectorization_.
  - _[Numpy Quickstart Tutorial - The Basics](https://docs.scipy.org/doc/numpy/user/quickstart.html#the-basics)_ (An Example; Array Creation; Printing Arrays; Basic Operations; Universal Functions; Indexing, Slicing and Iterating), _[Numpy Quickstart Tutorial - Shape Manipulation](https://docs.scipy.org/doc/numpy/user/quickstart.html#shape-manipulation)_ (Changing the shape of an array; Stacking together different arrays), _[Numpy Quickstart Tutorial - Indexing with Boolean Arrays](https://docs.scipy.org/doc/numpy/user/quickstart.html#indexing-with-boolean-arrays)_ (boolean arrays and how to use to do conditional selection).
  - Lecture Notes **Numerical_Computing___Numpy_Arrays** [.ipynb](Notebooks/Numerical_Computing___Numpy_Arrays.ipynb) | [.pdf](Notebooks/Printable/Numerical_Computing___Numpy_Arrays.pdf)
  - Exercises: [Exercise Sheet 1 - **ERRATA CORRIGE (Exercise 5)**](Exercises/Exercise_1.ipynb) - Solutions: [Ex_1](Exercises/Solutions/Ex_Sheet_1_Num_1.py), [Ex_2](Exercises/Solutions/Ex_Sheet_1_Num_2.py), [Ex_3](Exercises/Solutions/Ex_Sheet_1_Num_3.py), [Ex_4](Exercises/Solutions/Ex_Sheet_1_Num_4.py), [Ex_5](Exercises/Solutions/Ex_Sheet_1_Num_5.py)
  - Exercises: [Exercise Sheet 2](Exercises/Exercise_2.ipynb) - Solutions: [Ex_1](Exercises/Solutions/Ex_Sheet_2_Num_1.py), [Ex_2](Exercises/Solutions/Ex_Sheet_2_Num_2.py), [Ex_3](Exercises/Solutions/Ex_Sheet_2_Num_3.py), [Ex_4](Exercises/Solutions/Ex_Sheet_2_Num_4.py), [Ex_5](Exercises/Solutions/Ex_Sheet_2_Num_5.py), [Ex_6](Exercises/Solutions/Ex_Sheet_2_Num_6.py), [Ex_7](Exercises/Solutions/Ex_Sheet_2_Num_7.py)
  - Videos:
    - [Playlist: **Lesson 9 - NumPy Arrays**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=ea9d3e5f-4943-4784-ad4b-ab8a00cdcb97)

- **Lesson 10 (16/03)**:  Pandas `Series` data-structure: creation from 1-dim NumPy array using `pd.Series()` constructor, indexing and slicing using `[]` access operator, basic plotting, basic analytics, built-in methods, interface with NumPy's universal functions. Returns time-series: log-normal i.i.d. time-series (using NumPy's `random.lognormal` function), step-by-step computation, direct computation using `.shift()`, linear and log-returns.
  - _TB.5.The Series Class._
  - _[Pandas - Intro to data structures - Series](https://pandas.pydata.org/docs/getting_started/dsintro.html#series)._ 
  - Lecture Notes **Data_Analysis___Introduction_to_Pandas** [.ipynb](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/Notebooks/Data_Analysis___Introduction_to_Pandas.ipynb) | [.pdf](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/Notebooks/Printable/Data_Analysis___Introduction_to_Pandas.pdf): Sec. 1. Series.
  - Exercises: [Exercise Sheet 3](Exercises/Exercise_3.ipynb) - Solutions: [Ex_1](Exercises/Solutions/Ex_Sheet_3_Num_1.py), [Ex_2](Exercises/Solutions/Ex_Sheet_3_Num_2.py), [Ex_3](Exercises/Solutions/Ex_Sheet_3_Num_3.py), [Ex_4](Exercises/Solutions/Ex_Sheet_3_Num_4.py), [Ex_5](Exercises/Solutions/Ex_Sheet_3_Num_5.py)
  - Videos:
    - [Playlist: **Lesson 10 - Pandas Series**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=c2d9dfd9-77da-4305-b1da-ab8a00ce1dde)
 

- **Lesson 11 (18/03)**:  Pandas `DataFrame` data-structure: creation from multi-dim NumPy array using `pd.DataFrame()` constructor, columns selection using `[]` access operator, indexing and slicing of rows and columns using `.loc[]` and `.iloc[]` access operators, basic plotting, creation and deletion of columns, basic analytics on row- and column-wise base and `.groupby()` method, built-in methods, interface with NumPy's universal functions. Concatenation, Joining and Merging of two DataFrames using `.join()` method and `pd.merge()` function.
  - _TB.5.The DataFrame Class,_ _TB.5.Basic Analytics,_ _TB.5.Basic Visualization,_ _TB.5.Complex Selection,_ _TB.5.Concatenation, Joining, and Merging,_ _TB.5.Performance Aspects_.
  - _[Pandas - Intro to data structures - DataFrame](https://pandas.pydata.org/docs/getting_started/dsintro.html#dataframe)._ From _[Pandas - Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)_: 
    - [What kind of data does pandas handle?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html),
    - _[How do I select a subset of a `DataFrame`?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)_,
    - _[How to create plots in pandas?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)_, 
    - _[How to create new columns derived from existing columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)_, 
    - _[How to calculate summary statistics?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)_, 
    - _[How to combine data from multiple tables?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html)_.
  - Lecture Notes **Data_Analysis___Introduction_to_Pandas** [.ipynb](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/Notebooks/Data_Analysis___Introduction_to_Pandas.ipynb) | [.pdf](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/Notebooks/Printable/Data_Analysis___Introduction_to_Pandas.pdf): Sec. 2. DataFrames.
  - Exercises: [Exercise Sheet 4](Exercises/Exercise_4.ipynb) - Solutions: [Ex_1](Exercises/Solutions/Ex_Sheet_4_Num_1.py), [Ex_2](Exercises/Solutions/Ex_Sheet_4_Num_2.py), [Ex_3](Exercises/Solutions/Ex_Sheet_4_Num_3.py), [Ex_4](Exercises/Solutions/Ex_Sheet_4_Num_4.py)
  - Videos:
    - [Playlist: **Lesson 11 - Pandas DataFrames**](https://unisi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?pid=636951a2-4eba-4862-a705-ab8e00e4ad48)

- **Lesson 12 (30/03)**:  Python Serializations protocols (JSON and Pickle). IO operations between Pandas and output formats (SQL and `sqlite3` module, CSV and Excel)
  - TBD.
  - &#x1F534; **Data_Analysis___IO_with_Pandas - PARTIAL** [.ipynb](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/Notebooks/Data_Analysis___IO_with_Pandas%20-%20PARTIAL.ipynb) | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 13 (01/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 14 (06/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 15 (08/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 16 (15/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 17 (17/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 18 (22/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 19 (24/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_

- **Lesson 20 (29/04)**:  TBD.
  - TBD.
  - Lecture Notes _forthcoming_ [.ipynb] | [.pdf].
  - Exercises: _forthcoming_
  - Videos: _forthcoming_


# Resources <a name="resources"></a>

## Reading <a name="reading_material"></a>
- Textbook: [_Python for Finance -- Mastering Data-Driven Finance_ (2nd edition)](http://shop.oreilly.com/product/0636920117728.do) by Yves Hilpisch (O'Reilly). 
<img src="http://hilpisch.com/images/py4fi_2nd_shadow.png" width="75">

- Python tutorial: [Python 3.7 online tutorial](https://docs.python.org/3.7/tutorial/).

- Numpy tutorial(s): 
    - [Numpy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
    - [Numpy User Guide](https://docs.scipy.org/doc/numpy/user/index.html)

- Scipy tutorial: [Scipy Tutorial](https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/index.html)

- Pandas tutorial(s):
  - [Pandas - Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
  - [Intro to data structures](https://pandas.pydata.org/docs/getting_started/dsintro.html)

- Other useful resources online: [Beginner's Guide To Python](https://wiki.python.org/moin/BeginnersGuide).

- Tutorial from [Guido van Rossum](https://it.wikipedia.org/wiki/Guido_van_Rossum) (Python's first developer): [Python Tutorial Release 3.7.0 (September 02, 2018)](https://bugs.python.org/file47781/Tutorial_EDIT.pdf).


## Programming <a name="programming_material"></a>
- [Anaconda](https://www.anaconda.com/) platform <img src="images/Anaconda_Logo.png" width="75">
is a free and open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. Package versions are managed by the package management system `conda` The Anaconda distribution includes data-science packages suitable for Windows, Linux, and MacOS (quoting [wikipedia](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)) page)

  Tips: 
  
   - [How to manage Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - [Conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

- [Jupyter](https://jupyter.org/) Notebooks <img src="images/jupyter_logo.png" width="75"> 
(included in Anaconda distribution) is a web-based interactive computational environment for creating Jupyter notebook documents (quoting [wikipedia](https://en.wikipedia.org/wiki/Project_Jupyter#Jupyter_Notebook) page)

  Tips:

    - [Jupyter Notebooks cheat sheet](https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/)

- [Spyder](https://www.spyder-ide.org/) IDE <img src="images/spyder_logo.png" width="75"> 
(also shipped with Anaconda distribution) is an open source integrated development environment (IDE) for scientific programming in the Python language (quoting [wikipedia](https://en.wikipedia.org/wiki/Spyder_(software)) page)

---

# Setup <a name="setup"></a>
This section describes practical informations on how to work this class. Daily activities and once-for-all setup(s) are separately described both for in-class lessons and study from-home.

- For a step-by-step guide see [How-to-work-this-class.md](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md) file. Take a look at it if you are new to the class.

- For the checklist version of the same file see [How-to-work-this-class - checklist version.md](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class%20-%20checklist%20version.md) file. This file serves as a quick reference in case you forgot something.

Feel free to contact me at gabriele.pompa@unisi.it in case something is not clear or if you spot errors or if you have suggestions for improvement. Thanks. 
