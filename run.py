from reddit_bot import SimpleBot

# instantiate the bot
bot = SimpleBot()

# loop until user wants to quit
while True:

    # show instructions to user
    print("What would you like to do?\n")
    print("1 - see hot posts")
    print("2 - see posts from specific subreddit")
    print('3 - reply to a post')
    print("\nPress any other key to EXIT")
    action = input("Enter selection: ").strip()

    # handle user input
    if action == "1":
        bot.get_front_page(10)

    elif action == "2":
        bot.get_subreddit(5)

    elif action == "3":
        bot.post_reply()

    else:
        break

    print('')  # extra line break for readability

# user is exiting, say bye
print('OK bye, see you later!')
