# IT For Business and Finance 2019/20

This repository (https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20) provides course informations and material supporting the first year master course of _IT For Business and Finance_ held at University of Siena in 2019/20.

**WARNING**: the course and this repository is under ongoing update.

**Symbols conventions**: updated sections/material in this README.md file will be highlited with &#x1F534; (a big red circle) displayed next to it.

# Table of contents
- [IMPORTANT COMMUNICATIONS](#bakeka)
- [Class Schedule](#class_schedule)
- [Contacts](#contacts)
- [Class Diary](#class_diary)
- [Resources](#resources)
  - [Reading](#reading_material)
  - [Programming](#programming_material)
- [Setup](#setup)
  - [How to work IN CLASS](#class)
    - [Before the lessons starts](#before_class)
    - [How to follow the lesson](#during_class)
  - [How to work AT HOME](#home)
    - [First-time SETUP](#home_setup)
    - [How to work at home](#wfh)

# &#x1F534; IMPORTANT COMMUNICATIONS &#x1F534; <a name="bakeka"></a> 
- Soon will be active the e-learning for IT for Business and Finance course at [http://elearning.unisi.it/moodle/](http://elearning.unisi.it/moodle/) (more info to come). You will be able to access with your unisiPass credentials and the key-world: **ITForBusAndFin2020_elearning**. Stay tuned.

# &#x1F534; Class Schedule <a name="class_schedule"></a> 
Classes start on Monday, February 24 2020 at 14:00 in _Aula informatica 1_. The timetable is:

Monday: 14:00-16:00\
Tuesday: 18:00-19:30 **this lesson starts sharply at 18:00**\
Wednesday: 14:00-16:00

Currently known amendements to this schedule are the following:

Monday 16/3: _Aula 1_\
&#x1F534; Wednesday 4/3 and 18/3: _Aula 12_ 

# Contacts <a name="contacts"></a>
&#x1F534 [Gabriele Pompa](https://www.linkedin.com/in/gabrielepompa/) (gabriele.pompa@unisi.it)

# Class Diary <a name="class_diary"></a>
This is the diary of the class. Here the topics covered during the lessons are listed, as well as the corresponding [Python for Finance (2nd ed.)](http://shop.oreilly.com/product/0636920117728.do) textbook chapters and other learning material (e.g. Jupyter Notebooks).

- **Lesson 1 (24/02)**: class presentation. introduction to: programming in Python, Anaconda platform, Jupyter Notebooks and interactive programming, Spyder IDE and programmatic programming, Python modules and `import` expressions.
  - Sections 1._The Python Programming Language_, 1._Technology in Finance_
  - [Introduction I.ipynb](Notebooks/Introduction_I.ipynb)
  
- **Lesson 2 (25/02)**:  motivations for adopting Python in Finance.
  - Sec. 1._Python for Finance_, 1._Data-Driven Finance_, 2._Basic operations with conda_, 2._Conda as a Virtual Environment Manager_
  
- **Lesson 3 (26/02)**:  random number generation. Histogram. Empirical distribution (normalized histogram). Template for `.py` files (scripts) in Spyder.
  - &#x1F534; Spyder Template file [template_example.py](Scripts/template_example.py): use this file as a template example. Any script (`.py` file) that you write in Spyder IDE has to follow the structure of this template.
  - [Introduction II.ipynb](Notebooks/Introduction_II.ipynb): Sec. 1, 2, 3, 4.
  
- **Lesson 4 (2/03)**:  `int` data type, `.bit_length()` method for `int`, binary representation of integers (examples). `float` data type, issues of finite precision of internal binary representation of decimal numbers, arbitrary precision in Python ([`Decimal` module](https://docs.python.org/2/library/decimal.html)). Normal random variables in Python (Scipy [`norm` class](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)),`.pdf()` method of `norm` class, Normal fit to empirical distribution, `.fit()` method of `norm` class.
  - Sec. 3._Integers_, 3._Floats_
  - [Introduction II.ipynb](Notebooks/Introduction_II.ipynb): Sec. 5
  
- **&mu;&epsilon;&tau;&alpha;-Lesson 5 (3/03)**: gentle introduction to [github](https://github.com/). Teacher-Student(s) workflow (push-pull flow). Edit - Stage (`git add`) - Commit (`git commit`) pattern. Setup of a local development clone of a repository already established (hands-on example: `git clone` of the class repository into computers of _Aula Informatica 1_). Syncing local clone with updated class repository (the _hard_ way) with `git fetch` and `git reset`.   

# Resources <a name="resources"></a>

## Reading <a name="reading_material"></a>
- Textbook: [_Python for Finance -- Mastering Data-Driven Finance_ (2nd edition)](http://shop.oreilly.com/product/0636920117728.do) by Yves Hilpisch (O'Reilly). 
<img src="http://hilpisch.com/images/py4fi_2nd_shadow.png" width="75">

- Python tutorial: [Python 3.7 online tutorial](https://docs.python.org/3.7/tutorial/).

- Numpy tutorial(s): 
    - [Numpy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
    - [Numpy User Guide](https://docs.scipy.org/doc/numpy/user/index.html)

- Scipy tutorial: [Scipy Tutorial](https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/index.html)

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

# Setup <a name="setup"></a>
This section describes practical informations on how to work this class. Daily activities and once-for-all setup(s) are separately described both for in-class lessons and study from-home.

**NOTICE**: the same contents of this section have been replicate - adding step-by-step details and pictures - in [How-to-work-this-class.md](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md) file. Take a look at it if you are new to the class or if something in this section is not clear to you (if [How-to-work-this-class.md](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md) is not enough, feel free to ask!)

## How to work IN CLASS <a name="class"></a>

### Before the lessons starts <a name="before_class"></a>
These are the steps you need to be done **before** the lesson starts to effectively follow any in-class lesson:

0. go to the class webpage at [github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20). 

1. Open Anaconda Navigator and switch to the class conda environment `ITForBusAndFin2020_env`

2. Sync your local copy of the class repository to have the latest updated material of the class. To do this:

  - In the Anaconda Navigator, open the _console_shortcut_ app. 
  - In the terminal window open, type (for an explanation of this commands see [this answer](https://stackoverflow.com/a/8888015/2533366) in [Stack Overflow](https://stackoverflow.com/):
  
  ```
  cd C:\Users\it-bf\Desktop\IT-For-Business-And-Finance-2019-20
  git fetch --all
  git reset --hard origin/master
  ```
  
  **WARNING**: `git reset` command will overwrite all changes to files in the class repository that are not in the dedicated `IT-For-Business-And-Finance-2019-20/Personal_Notes` folder. That is, for example, if these changes were notes that you took while on a Jupyter Notebook while reading it, these notes will be lost!!! See section [How to follow the lesson](#during_class) to effectively take notes during the lesson and section [How to work at home](#wfh) to know how to retrieve those notes at home and how to take new ones at home while studying on Notebooks. 
    
3. Launch the Jupyer Notebook App

4. In the newly opened Google Chrome's panel, navigate to folder `/Desktop/IT-For-Business-And-Finance-2019-20/Notebooks` and open the Notebook that you want.
  
### How to follow the lesson <a name="during_class"></a>
Let's suppose that you modify `Introduction_II.ipynb` (these instructions apply to any Notebook and any file in `/IT-For-Business-And-Finance-2019-20` folder

When the lesson ends you want to keep studying on the modified notebook at home. Then you can: 

0. Rename your Notebook as _Introduction_II___WITH_MY_NOTES_ 

1. Download the Notebook _as a Notebook (.ipynb)_.

2. E-mail the renamed Notebook `Introduction_II___WITH_MY_NOTES.ipynb` to yourself. 

**WARNING**: remember to log-off from gmail before you leave the IT class.
  
## How to work AT HOME <a name="home"></a>

### First-time SETUP (things to do once and for all) <a name="home_setup"></a>
These are preliminary tasks to be done the first time that you work on this class from your personal computer. There are many more details in the corresponding section [First-time SETUP](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md#first-time-setup-things-to-do-once-and-for-all-) of the [How-to-work-this-class.md](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20/blob/master/How-to-work-this-class.md) file. 

0. [Download Anaconda](https://www.anaconda.com/distribution/#download-section)
 
1. Download Git: [Windows](https://git-scm.com/download/win) | [Max OS](https://git-scm.com/download/mac) 
| [Linux/Unix](https://git-scm.com/download/linux) 

2. clone the [IT-For-Business-And-Finance-2019-20](https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20) class repository into your `/Desktop` folder. Type:

  ```
  cd C:\Users\[$YOUR_USER_NAME]\Desktop
  git clone https://github.com/gabrielepompa88/IT-For-Business-And-Finance-2019-20.git
  ```
  
  where `[$YOUR_USER_NAME]` has to be substituted with your appropriate user name in your computer. You will see that a newly created `/IT-For-Business-And-Finance-2019-20` is created in your `/Desktop` folder.
  
3. Create the _ITForBusAndFin2020_env_ Conda environment importing the `ITForBusAndFin2020_env_setup.yml` file that you find in the newly created `/IT-For-Business-And-Finance-2019-20` folder. Switch to this environment.

## How to work at home (things to do everytime) <a name="wfh"></a>
When you are at home and want to study for this class, you can do the following:

0. Follow all the steps (0., 1., 2., 3. and 4.) explained in section [Before the lessons starts](#before_class) on your computer. 

1. Put `/IT-For-Business-And-Finance-2019-20/Personal_Notes` the files with notes taken in class that you sent to yourself via e-mail.

2. Work on any file of the class folder `/IT-For-Business-And-Finance-2019-20` using the Jupyter Notebook App or the Spyder App of the Anaconda Navigator, and:

- **any file that you change must be copied-n-pasted into /Personal_Notes folder**
- **any file that you newly create must be saved into /Personal_Notes folder**.

