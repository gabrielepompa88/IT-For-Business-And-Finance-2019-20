# Table of contents
- [How to work IN CLASS](#class)
  - [Before the lessons starts](#before_class)
  - [How to follow the lesson](#during_class)
- [How to work AT HOME](#home)
  - [First-time SETUP](#home_setup)
  - [How to work at home](#wfh)

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
- **any file that you create _ex-novo_ must be saved into /Personal_Notes folder**.

