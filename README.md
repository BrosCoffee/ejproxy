# ejproxy
Challenge:

Create a simple Django project that can parse the table on the Methodologies page of ejproxy.com and save the results into an SQLite database.
Your code should be executable via a command line. Include instructions on how to use it.
Once you’re done, please either push your code into a repository (any will work) and share the link OR zip it up and attach it with your response.

Loom video demo: https://www.loom.com/share/99c14e06a7f044da9c83b5b580fd1147

The project is written in Python 3.9 and Django 3.2

    python -V
    Python 3.9.7
    
    python -m django --version
    3.2.6

The following steps demonstrate how we create a Post object from the shell:

    python3 manage.py shell

    >>> from methodologies.models import Post
    >>> from datetime import datetime
    >>> from pytz import timezone
    >>>
    >>> date = datetime(2021, 3, 5, 14, 30, 00, tzinfo=timezone('US/Eastern')) # 03/05/21 14:30:00 EST
    >>> title = 'Egan-Jones Proxy Services Catholic Proxy Voting Principles and Guidelines 2021'
    >>> url = 'https://ejproxy.com/media/documents/Egan-JonesProxyVotingPrinciplesandGuidelinesCATHOLIC_2021.pdf'
    >>>
    >>> post = Post(title=title, url=url, date_added=date)
    >>> post.save()

The express way will be:

    >>> Post.objects.create(...)
