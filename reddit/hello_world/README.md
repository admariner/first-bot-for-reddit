# Hello World Bot for Reddit

### This is an starter code and exercise for creating a simple bot for reddit.
 You can follow the steps below to create your own bot for reddit!

<p align="center">
<img src="img/preview.gif" alt="preview gif" />
</p>

This is a beginner-level tutorial. It assumes you have basic understanding 
of Python programming language (basic syntax: variables, loops, conditional 
 statements, classes). If you are interested in creating a Reddit bot but 
haven't created one before, you may find this tutorial helpful. 

This bot is built using Python 3 and [PRAW](https://github.com/praw-dev/praw), 
"Python Reddit API Wrapper" - an open source python package that allows simple 
access to Reddit's API.


### Features

This bot runs on the local machine from command line. It performs actions 
based on user commands, but it can be modified to perform autonomously (to 
make a _true_ bot, modify it to work autonomously). 

These are the specific actions this bot knows how to perform:

- **Reading hot posts** — Read trending posts from your favorite subreddits  
- **Reading posts from specific subreddits** — Enter subreddit name and see 
 what is hot in that subreddit
- **Reading random post and replying** - Choose some subreddit and reply to 
random post from the terminal  

**Simple code:** easy to follow and ideal for beginners

**Estimated duration:** 10 - 60 minutes

* * *

## Prerequisites

Before you start check that you have all of the following:

- [ ] Python 3 ([Installation](https://realpython.com/installing-python/))
- [ ] Python IDE (for example [PyCharm](https://www.jetbrains.com/pycharm/download))
- [ ] Reddit user account ([Register](https://www.reddit.com/register/))

* * * 

## Steps

### 1 - Setup Environment

> Complete the following steps in your Python IDE

#### 1.1. Clone this repo then open it in your Python IDE

```
https://github.com/MobileFirstLLC/first-bot-for-reddit.git
```

*TIP*: If you are using PyCharm you can do step 1 from the start screen

<p align="center">
<img src="img/clone.jpg" alt="create app" width="400" />
</p>

If you do not have git installed locally or do not know how to use git, 
you can download this repository as a ZIP file.

#### 1.2. Install Requirements

Run this command in the terminal:

```
pip install praw
```

* * *

### 2 - Create an app on Reddit

> For the next steps you will visit reddit.com and create your first application.


#### 2.1. Go to [Create an app...](https://ssl.reddit.com/prefs/apps/) (top left corner!) 

<p align="center">
<img src="img/create_app.jpg" alt="create app" width="400" />
</p>

#### 2.2. Enter some basic information about your app:

- enter app **name**
- choose **script** type
- enter some basic **description**
- **about URL** can be blank 
- for **redirect URI** enter any valid URL (doesn't matter - we are not 
using it but it is required)

Something similar to what is shown below will work

<p align="center">
<img src="/docs/img/create_app_inputs.jpg" alt="input values" width="400" />
</p>

#### 2.3. Create app

At this point you should see a page similar to the one below.
Pay attention to your `client ID` and `secret`. You will need these in the next step.

<p align="center">
<img src="img/client_id.jpg" alt="input values" width="100%" />
</p>

* * *

### 3 - Run the Code

> In this step you will start working with the Python code and learn how to 
run the bot.


#### 3.1. Open `config.py`

This file is used to setup your authentication credentials for Reddit API. 
You will need to make changes in this file. 

Following the instructions in the comments, add your `client ID`, `secret`, 
 `username`, and `password` to authenticate with Reddit. **Make sure you 
 keep this file secret (!)** after entering these values. If you don't, anyone can hijack your reddit account and pretend to be you.

#### 3.2. Open `reddit_bot.py`

This is the source code for the reddit bot. It is a simple class that can execute specific actions on reddit. Reading through it should give you an idea of its capabilities.

#### 3.2. Open `__main__.py`

This it the file that creates the bot, gives you an interface to interact with the bot and passes commands to the bot. Read through the code briefly to get an idea of the purpose of this script.

#### 3.3. Execute `run.py`

In your terminal or command prompt, run:

```
python -m reddit.hello_world
```

Assuming you completed all steps correctly and nothing has changed in the Reddit API since the writing of these instructions, you should see some interesting output in the terminal! Go ahead and interact with the bot.

If you are seeing an Exception of any kind, double-check your steps. Make sure you have installed all dependencies and correctly configured your credentials in the `config.py` file.

* * *

### 4 - Extend the code

You can now start building up the bot to do more advanced actions of your choice! [Read PRAW documentation](https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html) to understand how to interact with different Reddit features such as comments, subreddits, and messages. The rest is up to you.

Here are some suggestions of how to enhance the bot capabilities:

- Add ability to automatically mark inbox messages read
- Add ability to see messages from specific user
- Add ability to send private messages to a friend

* * * 


We would like to make this tutorial better over time. If you had any issues 
 following these instructions, [review existing issues](https://github
 .com/MobileFirstLLC/first-bot-for-reddit/issues/). If the issue you ran into
  is not addressed, open a [new issue](https://github.com/MobileFirstLLC/first-bot-for-reddit/issues/new/choose). 
 
 Thank you for your feedback!
