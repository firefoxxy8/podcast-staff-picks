import json
from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL
from sheet import get_google_sheet

@app.route('/')
def index():
    sheets = get_google_sheet()
    staff_picks = []

    for index, pick in enumerate(sheets):
	    staff_pick = {}
	    staff_pick['recommender'] = json.dumps(pick['Recommender'])
	    staff_pick['title'] = json.dumps(pick['Title'])
	    staff_pick['twitter'] = json.dumps(pick['Twitter'])
	    staff_pick['episode'] = json.dumps(pick['Episode'])
	    staff_pick['podcast'] = json.dumps(pick['Podcast'])
	    staff_pick['link'] = json.dumps(pick['Link'])
	    staff_pick['description'] = json.dumps(pick['Description'])
	    staff_picks.append(staff_pick)

    return render_template('staff_picks.json',
        staff_picks=staff_picks,
        )
