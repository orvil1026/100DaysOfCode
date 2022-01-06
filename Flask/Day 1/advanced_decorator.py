class User:

    def __init__(self, name):
        self.name = name
        self.logged_in = False


def is_authenticated(function):

    def wrapper(*args, **kwargs):

        if args[0].logged_in:

            function(args[0])

    return wrapper


@is_authenticated
def new_blog_post(user):
    print(f"New blog post by {user.name}")


new_user = User("orvil")
new_user.logged_in = True
new_blog_post(new_user)
