import praw
from config import CLIENT_ID, SECRET, USERNAME, PASSWORD, USER_AGENT


class SimpleBot:
    """
    This is a simple class that knows how to
    perform limited actions on reddit
    """

    def __init__(self):
        """ Initialize the reddit client """
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=SECRET,
            username=USERNAME,
            password=PASSWORD,
            user_agent=USER_AGENT)
        SimpleBot.print_intro()

    @staticmethod
    def print_intro():
        print('\n██ ███    ███      █████')
        print('██ ████  ████     ██   ██')
        print('██ ██ ████ ██     ███████')
        print('██ ██  ██  ██     ██   ██')
        print('██ ██      ██     ██   ██')
        print('')
        print('██████   ██████  ████████ ██')
        print('██   ██ ██    ██    ██    ██')
        print('██████  ██    ██    ██    ██')
        print('██   ██ ██    ██    ██')
        print('██████   ██████     ██    ██\n')

    @staticmethod
    def print_output_caption(text: str) -> None:
        """ display text caption on the screen """
        print('')
        print('=' * 50)
        print(text.upper())
        print('=' * 50)

    @staticmethod
    def subreddit_prompt():
        """ prompt user to enter subreddit name """
        return input('enter subreddit name: /r/')

    def get_front_page(self, limit: int) -> None:
        """
        This method get top posts from the front page
        then displays them on the screen
        :param limit: number of posts to display
        """

        SimpleBot.print_output_caption('hottest posts right now')

        # Get hot posts from front page
        for post in self.reddit.front.hot(limit=limit):
            # display post score and title
            print(str(post.score).ljust(8), post.title)

    def get_subreddit(self, limit: int) -> None:
        """
        This method gets top posts from a specific
        subreddit and displays them on the screen
        :param limit: number of posts to display
        """

        # ask user for subreddit
        subreddit = SimpleBot.subreddit_prompt()

        SimpleBot.print_output_caption('top posts from ' + subreddit)

        # Get hot posts from a specific subreddit
        for post in self.reddit.subreddit(subreddit).hot(limit=limit):
            # display post score and title
            print(str(post.score).ljust(8), post.title)

    def post_reply(self) -> None:
        """
        This method gets a random post from a specific
        subreddit, then prompts for reply and posts
        that reply
        :return:
        """

        # ask user for subreddit
        subreddit = SimpleBot.subreddit_prompt()

        # get random from selected subreddit
        post = self.reddit.subreddit(subreddit).random()
        print(post.title)
        print(post.selftext or post.url)

        action = input('\nWould you like to reply to this post, y/n: ')
        if action == 'y':
            reply = input('Enter your reply: ')
            post.reply(reply)
            print('Reply posted!')
            print('See: ', 'https://www.reddit.com/user/' + USERNAME)
