from digitalhealthapp import app

import json, plotly
from flask import render_template, request, Response, jsonify
from scripts.data import return_figures


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

	# Parse the POST request countries list
	if (request.method == 'POST') and request.form:
		figures = return_figures(request.form)

	# GET request returns all countries for initial page load
	else:
		figures = return_figures()

	# plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON)
