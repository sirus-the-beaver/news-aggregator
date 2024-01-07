# news-aggregator

This project is a news aggregator that aggregates an article from 2 different news sources (CNN and NPR).

The project features a GUI where users can search any term or phrase they wish. After they submit their search request, the user will be returned the most recent article from CNN and NPR that pops up for that search term or phrase.

The articles are displayed as a headline, with a timestamp, the source, and the actual body of the article.

In some cases, an article doesn't have any text (such as articles that have a video as the content). In these cases, the aggregator will return some text stating that the article doesn't have any text, but will still return the link to the article so that the user can visit the article if they wish to do so.

In the event that an article can't load due to a timeout error, or an article simply doesn't exist for the search term or phrase, then the aggregator will return some text stating that either an article couldn't be found or couldn't be loaded.

In order to run this program:

- Clone this repository onto your local machine
- From the command line, enter: ```python gui.py```

Upon launching the program, the GUI will pop up and you'll be able to use the software as intended.
