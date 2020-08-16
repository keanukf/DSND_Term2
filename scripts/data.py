import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.colors
from collections import OrderedDict
import requests
from pynytimes import NYTAPI
import datetime


def return_figures():
  """ Creates four plotly visualizations using the New York Times Archive API

    Returns:
        list (dict): list containing the four plotly visualizations
  """
  # Add New York Times API Key
  nyt = NYTAPI("AsjeHhqDYrePA2GMPpYoY1KAKAdG7P99")

  # Select Year and Month of articles
  data = nyt.archive_metadata(
    date = datetime.datetime(2020, 7, 1)
    )

  def data_to_df(data):
      # Initiate list for restructured information
      data_list = []

      # Collect Data from API dictionary
      for article in data:
          new_data = [article.get("section_name"),
                     article.get("news_desk"),
                     article.get("pub_date"),
                     article.get("headline").get("main"),
                     article.get("abstract"),
                     article.get("lead_paragraph"),
                     article.get("type_of_material"),
                     article.get("word_count")]
          # Append list of information from article to data list
          data_list.append(new_data)

      # Convert data list to DataFrame
      df = pd.DataFrame(data_list, columns=["section_name","news_desk", "pub_date", "headline", "abstract", "lead_paragraph", "type_of_material", "word_count"])

      return df

  df = data_to_df(data)

  # first chart plots section distribution
  # as a pie chart
  graph_one = []
  df_one = df.copy()

  # filter and sort values for the visualization
  # filtering plots the articles in decreasing order by their values
  labels = df_one.section_name.value_counts().index
  values = df_one.section_name.value_counts().values

  graph_one.append(
    go.Pie(
        labels=labels,
        values=values,
        hole=.6,
        textposition="inside"
    )
  )

  layout_one = dict(title = 'Distribution of sections of this months New York Times articles')

  # second chart plots section distribution
  # as a pie chart
  graph_two = []
  df_two = df.copy()

  # filter and sort values for the visualization
  # filtering plots the articles in decreasing order by their values
  labels = df_two.news_desk.value_counts().index
  values = df_two.news_desk.value_counts().values

  graph_two.append(
    go.Pie(
        labels=labels,
        values=values,
        hole=.6,
        textposition="inside"
    )
  )

  layout_two = dict(title = 'Distribution of news desk of this months articles')

  # third chart plots section distribution
  # as a pie chart
  graph_three = []
  df_three = df.copy()

  # filter and sort values for the visualization
  # filtering plots the articles in decreasing order by their values
  labels = df_three.type_of_material.value_counts().index
  values = df_three.type_of_material.value_counts().values

  graph_three.append(
    go.Pie(
        labels=labels,
        values=values,
        hole=.6,
        textposition="inside"
    )
  )

  layout_three = dict(title = 'Distribution for type of material of this months articles')

  # fourth chart plots section distribution
  # as a pie chart
  graph_four = []

  # Convert publishing date columns to datetime format
  df["pub_date"] = pd.to_datetime(df["pub_date"]).dt.date

  df_four = df.copy()
  df_four = df_four.pub_date.value_counts().to_frame().sort_index()

  # filter and sort values for the visualization
  # filtering plots the articles in decreasing order by their values
  x_val = df_four.index
  y_val = df_four.values

  graph_four.append(
        go.Scatter(
            x=df_four.index,
            y=df_four["pub_date"],
            mode="lines",
            name="Articles"
        )
  )

  layout_four = dict(title = 'Number of articles published by days')

  # fourth chart plots section distribution
  # as a pie chart
  graph_five = []

  # Calculate average number of words for this months articles
  avg_word_count = round(df.word_count.mean(),0)

  graph_five.append(
      go.Table(
          header=dict(values=['Average Word Count']),
          cells=dict(values=[avg_word_count])
      )
  )

  layout_five = dict(title = '')

  # append all charts
  figures = []
  figures.append(dict(data=graph_one, layout=layout_one))
  figures.append(dict(data=graph_two, layout=layout_two))
  figures.append(dict(data=graph_three, layout=layout_three))
  figures.append(dict(data=graph_four, layout=layout_four))
  figures.append(dict(data=graph_five, layout=layout_five))

  return figures
