""" Context processors needed for the top navbar"""


def add_user(request):
    """Adds user to every template """
    return {'user': request.user}
