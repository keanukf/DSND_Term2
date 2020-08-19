### Link to the [New York Times Dashboard](https://udacity-nyt-dashboard.herokuapp.com/)

## New York Times Dashboard

This is a web app was built with python and flask and was deployed with [Heroku](https://dashboard.heroku.com/apps). It visualizes a set of data including all articles by New York Times (NYT) published this month. Data is visualized using Plotly.
This is a project in development for the Udacity Data Scientist Nanodegree.

## Agenda

1. The flood of information
2. Perspectives on a solution
3. Development of a New York Times dashboard
4. Limitations and possible improvements
5. How to install it yourself


### Preview of the developed Dashboard
![Project Preview](/images/preview.png)

## Repository structure
* "nytdashboardapp" - Folder containing web app files
  * "static" - HTML web pages
    * "img" - Folder containing images for the web app
  * "templates" - HTML web pages
    * "index.html" - Page that shows NYT Dashboard
  * "routes.py" - File that defines web app page connections
* "scripts" - Folder containing data sources and processing script
  * "data.py" - Datasource including New York Times data and chart creation
  * "data.ipynb" - Jupyter Notebook used for data modeling testing purposes
* "Images" - Folder containing images used for README.md
* "nltk.txt" - Text file with nltk corporas for Heroku
* "nytdashboard.py" - Script that starts the web app (Heroku and locally)
* "Procfile" - File specifying web app type for Heroku
* "requirements.txt" - File specifying imported python packages for Heroku


# 1. The flood of information

In today's world, access to information is increasingly easy. Whether on Facebook, LinkedIn and Instagram, all information is from official and private sources. In addition, many recommendation machine learning algorithms are now learning to interpret user behavior, making what is presented to us even more pre-selected.

Therefore, it might be useful to have a tool for a general overview of the distributed contents of certain serious and reliable news institutions.

In a first step, it would be useful to have a dashboard that could answer the following questions:
- In which areas and topics are most articles published?
- On which days of the month are the most and least articles published?
- Is it possible to show a mood for the current articles?


# 2. Perspectives on a solution

To give a first solution to this problem, I created a dashboard for the (digital) articles of the New York Times of the current month, whose development I will explain in the following.

I chose the [New York Times](https://www.nytimes.com/) because it has a high reputation, professionalism and a well documented [API](https://developer.nytimes.com/).


# 3. Development of a New York Times dashboard
The following will explain the approach I chose to develop the Dashboard and deploy it as a web app. For full code see GitHub repository. Also find a [Jupyter Notebook](https://github.com/keanukf/udacity_nyt_dashboard/blob/extended_version/scripts/data.ipynb) in the repository, where I double checked some of the code of the web app.

## 3.1 Data extraction of the NYT API
The data extraction and modeling of charts was fully done in the `scripts/data.py`file. I used the `pynytimes` package for easier connection. I extracted all the articles of July, which in the end included 6553 articles. After inspecting the dataset and extracting the relevant columns, no data was missing, so no further data cleaning was necessary.

## 3.2 Data modeling and analysis to answer  

Then the first three charts were developed with `plotly` and its `go` functions, in order to answer the first question (see Figure 1). There the distribution of 1) sections, 2) news desks and 3) type of material is shown. Here we can easily see that in July the most articles were published within the U.S. section (20.6%), on the Business news desk (8.53%) and by far the most published articles were news (72.6%). That's already a good overview of the distributions of topics and types of articles. Here as well the data was already clean and had no double values oder missing values.

To answer the second question, again a `plotly` chart was created by aggregating the publishing dates and counting the number of articles published per day. On this chart (see Figure 1) we can see that there's a wide range of number of published articles (range between 57 and 382). That there are frequent lows, occuring at the Saturday 4th, Sunday 12th, Saturday 18th and Sunday 26th, which might be an indicator that the New York Times might has several low production days during the weekend.

### Figure 1
![Project Preview](/images/preview.png)

Regarding the last question, a Natural Language Processing (NLP) sentiment analysis approach was chosen. Specifically the pretrained Vader text corpus and the `SentimentIntensityAnalyzer()` sentiment analysis function was used. It can easily be used on new english language data to score positive, neutral and negative words.

### Advantages of using VADER
"VADER has a lot of advantages over traditional methods of Sentiment Analysis, including:
- It works exceedingly well on social media type text, yet readily generalizes to multiple domains
- It doesn’t require any training data but is constructed from a generalizable, valence-based, human-curated gold standard sentiment lexicon
- It is fast enough to be used online with streaming data, and
- It does not severely suffer from a speed-performance tradeoff."

Within the first implementation of the Vader sentiment analysis the dataset was too large to analyze, causing an error at the heroku deployment. That's why I decided to only filter for one section, the `politics` section in this case. The resulting chart (see Figure 2) shows us, that Julies politics articles were mostly positive (45.8%) and only a third (34.6%) of the words used were negative, with the rest being neutral. This gives any user a quick overview about the overall sentiment of a specific section.

### Figure 2
![Sentiment Analysis](/images/sentiment.png)

## 3.3 Deployment of the web app
For the deployment of the web app I chose Heroku and took a template of Udacity, for a basic web application. A lot of problems and debugging was caused by the implementation of NLP algorithms and packages, e.g. the `nltk` package, because therefore some extra files like the `nltk.txt` including nltk corpora download specifications, was necessary. Afterall the web app was finally deployed on Heroku with the user of python and flask.


# 4. Limitations and possible improvements
## Limitations

The performance of the NLP implementation is limited, so it was only possible to give an overview over one section. Also the user is not able to manipulate and interact with the data.

## Possible improvements

One possible and probably useful additional feature would be some filters, so users can actively choose what data of which time period is most relevant to them. This can easily be implement within the web part of the application, since the easy NYT API allows free choice of dates - information about filtering just need to be put at the query part of the API connection.
Another interesting filter might be filtering out specific topics and news types for the sentiment analysis, so they can get a quick overview of overall sentiment tendencies of the topic of their interest.

Also further NLP algorithms can be implemented (like the one that I didn't manage to implement to the web app) and already existing ones can be fined tuned and improved.

Finally it might be a relevant extension to also implement other newspaper APIs and give the user a chance to select between different newspapers for analysis.


# 5. How to install it yourself

## Prerequisites

To install the flask app, you need:
- python3
- python packages in the requirements.txt file

 Install the packages with
```
 pip install -r requirements.txt
```

## Installing

Add `app.run(host='0.0.0.0', port=3001, debug=True)` as a new line to the `nytdashboard.py`file.

On a MacOS/linux system, installation is easy. Open a terminal, and go into
the directory with the flask app files. Run `python nytdashboard.py` in the terminal.

Then open `http://0.0.0.0:3001/` in the browser of your choice.
