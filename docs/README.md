# My First Bot for Reddit

![img](https://img.shields.io/static/v1?label=python&message=3%2B&color=4B8BBE) 
![img](https://img.shields.io/static/v1?label=&message=reddit&color=FF4500)
![img](https://img.shields.io/github/v/release/mobilefirstllc/first-bot-for-reddit)

### This is an starter code + exercise for creating a simple bot for reddit. You can follow the steps below to create your own first bot for reddit!

This is a beginner-level tutorial. It assumes you have basic understanding of Python programming language. If you are interested in creating a Reddit bot but haven't created one before, you may find this tutorial helpful. 

This bot is built using Python 3 and [PRAW](https://github.com/praw-dev/praw), "Python Reddit API Wrapper" - an open source python package that allows for simple access to Reddit's API.


### Features

This bot runs on the local machine from command line. It performs actions based on user
commands, but it can be modified to perform autonomously. These are the specific actions this
bot knows how to perform:

- **Reading hot posts** — Read trending posts from your favorite subreddits  
- **Reading posts from specific subreddits** — Enter subreddit name and see what is hot in that subreddit
- **Reading random post and replying** - Choose some subreddit and reply to random post from the terminal  
- **Simple code** - easy to follow and good for beginners

**Estimated duration:** 10 - 60 minutes

* * *

## Prerequisites

Before you start check that you have all of the following:

- [ ] Python 3 ([How to install Python 3](https://realpython.com/installing-python/))
- [ ] Python IDE (for example [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download))
- [ ] Reddit User Account ([Register](https://www.reddit.com/register/))

* * * 

## Steps

### 1 - Prepare Your Project Environment

> Complete the following steps in your Python IDE

#### 1.1. Clone this repo then open it in your Python IDE

```
https://github.com/MobileFirstLLC/first-bot-for-reddit.git
```

*TIP*: If you are using PyCharm you can do step 1 from the start screen

<p align="center">
<img src="/docs/img/clone.jpg" alt="create app" width="400" />
</p>


#### 1.2. Create virtual environment 

This step is optional but highly recommended.
If you need help [see this doc](https://docs.python.org/3/tutorial/venv.html).

**On Unix or MacOS, run:**

```
python3 -m venv env
source env/bin/activate
```

**On Windows, run:**

```
python3 -m venv env
env\Scripts\activate.bat
```

#### 1.3. Install Requirements

Run this command in the terminal:

```
pip3 install -r requirements.txt
```

#### 1.4. For PyCharm users: Set project interpreter

If you are using PyCharm and created the virtual environment from a terminal, make sure the project interpreter is set
to point to that virtual environment:

- Open `PyCharm > preferences`
- Then `Project: first-bot-for-reddit > Project interpreter` 
- Click the cog icon in top right > `add`
- Choose `existing environment` and check that it points to your virtual environment `.../.../first-bot-for-reddit/env/bin/python`
- Click `OK`

* * *

### 2 - Create an app on Reddit

> For the next steps you will visit reddit.com and create your first application.


#### 2.1. Go to [Create an app...](https://ssl.reddit.com/prefs/apps/) (top left corner!) 

<p align="center">
<img src="/docs/img/create_app.jpg" alt="create app" width="400" />
</p>

#### 2.2. Enter some basic information about your app:

- enter app **name**
- choose **script** type
- enter some basic **description**
- **about URL** can be blank 
- for **redirect URI** enter any valid URL (doesn't matter - we are not using it but it is required)

Something similar to what is shown below will work

<p align="center">
<img src="/docs/img/create_app_inputs.jpg" alt="input values" width="400" />
</p>

#### 2.3. Create app

At this point you should see a page similar to the one below.
Pay attention to your `client ID` and `secret`. You will need these in the next step.

<p align="center">
<img src="/docs/img/client_id.jpg" alt="input values" width="100%" />
</p>

* * *

### 3 - Get to Coding!

> This is the last step of this tutorial. In this step you will start working with the Python code.


#### 3.1. Open `config.py`

This file is used to setup your authentication credentials for Reddit API. You will need to make changes in this file. 

Following the instructions in the comments, add your `client ID`, `secret`, `username`, and `password` to authenticate with Reddit. **Make sure you keep this file secret (!)** after entering these values. If you don't, anyone can hijack your reddit account and pretend to be you.

#### 3.2. Open `reddit_bot.py`

This is the source code for the reddit bot. It is a simple class that can execute 
specific actions on reddit. Just by reading through it you should get an idea of 
its capabilities.

#### 3.2. Open `run.py`

This it the file that creates the robot, gives you an interface to interact with the robot
and passes commands to the robot. It is not meant to be challenging you should get a good
idea of what is happening if you briefly read through the code.

#### 3.3. Execute `run.py`

Now run the `run.py` script and see what you get 

```
python run.py
```

Assuming you completed all steps correctly and nothing has changed in the Reddit API since the writing of these instructions, you should see
some interesting output in the terminal!

If you are seeing an Exception of any kind, double-check your steps. Make sure you have installed all dependencies and correctly configured your credentials in the `config.py` file.

* * *

### 4 - BONUS: Modify the code

You can now start building up the bot to do more advanced actions of your choice! [Read PRAW documentation](https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html) to understand how to interact with different Reddit features such as comments, subreddits, and messages. The rest is up to you.

Here are some suggestions of how to enhance the bot capabilities:

- [ ] Add ability to send private messages to self or a friend
- [ ] Add ability mark inbox messages read
- [ ] Add ability to see messages from specific user

* * * 

### END

Hopefully this tutorial was helpful! 

We would like to make this tutorial better over time. If you had any issues following these instructions, 
first [review existing issues](https://github.com/MobileFirstLLC/first-bot-for-reddit/issues/). If the
issue you are having is not addressed there open a [new issue](https://github.com/MobileFirstLLC/first-bot-for-reddit/issues/new/choose). 
Thank you in advance for your input.
