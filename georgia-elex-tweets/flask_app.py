from flask import Flask, render_template, request, send_from_directory
import requests
import json
from datetime import datetime

ap_format_str = '%B %d, %Y %H:%M'
input_time_str = '%Y-%m-%d %H:%M'

app = Flask(__name__)
app.config["DEBUG"] = False


def get_json(query_string=''):
    json_data = 'https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets.json'
    url = json_data + query_string
    r = requests.get(url)
    json_obj = json.loads(r.content)
    return json_obj

@app.route('/')
def index():
    template = 'index.html'
    timestamp_json = get_json('?_sort_desc=created_at_est&_size=1')
    timestamp = timestamp_json['rows'][0][1][:-10]
    datetime_obj = datetime.strptime(timestamp, input_time_str)
    formatted_timestamp = datetime_obj.strftime(ap_format_str)
    latest = get_json('?_size=100&_sort_desc=created_at_est&_shape=objects')
    return render_template(template,
                           formatted_timestamp=formatted_timestamp,
                           latest=latest,
                           )

@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")


@app.route('/<topic>/')
def detail(topic):
    template = 'detail.html'
    if topic == "senate_regular":
        query_string = '?display_name__contains=Senate,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="U.S. Senate Regular Election",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=Senate%2C&_sort_desc=created_at_est"
        )
    elif topic == "senate_special":
        query_string = '?display_name__contains=Special&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="U.S. Senate Special Election",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=Special&_sort_desc=created_at_est"
        )
    elif topic == "hd1":
        query_string = '?display_name__contains=District+1,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 1",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+1%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd2":
        query_string = '?display_name__contains=District+2,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 2",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+2%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd3":
        query_string = '?display_name__contains=District+3,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 3",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+3%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd4":
        query_string = '?display_name__contains=District+4,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 4",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+4%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd5":
        query_string = '?display_name__contains=District+5,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 5",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+5%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd6":
        query_string = '?display_name__contains=District+6,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 6",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+6%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd7":
        query_string = '?display_name__contains=District+7,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 7",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+7%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd8":
        query_string = '?display_name__contains=District+8,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 8",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+8%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd9":
        query_string = '?display_name__contains=District+9,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 9",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+9%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd10":
        query_string = '?display_name__contains=District+10,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 10",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+10%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd11":
        query_string = '?display_name__contains=District+11,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 11",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+11%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd12":
        query_string = '?display_name__contains=District+12,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 12",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+12%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd13":
        query_string = '?display_name__contains=District+13,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 13",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+13%2C&_sort_desc=created_at_est"
        )
    elif topic == "hd14":
        query_string = '?display_name__contains=District+14,&_sort_desc=created_at_est&_shape=objects&_size=300'
        query_result = get_json(query_string=query_string)
        return render_template(
            template,
            topic="Georgia House District 14",
            object=query_result,
            see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets?display_name__contains=District+14%2C&_sort_desc=created_at_est"
        )
    elif topic == 'about':
        template = 'about.html'
        return render_template(template, object=None)
    else:
        not_found = "There's no page for this topic :("
        return render_template(template, object=not_found, see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets")


@app.route('/search/search', methods=['POST'])
def search():
    template = 'detail.html'
    user_input = request.form['search']
    json_query = "?_search=" + user_input + "&_sort_desc=created_at_est&_shape=objects&_size=max"
    search_results = get_json(json_query)
    if len(search_results['rows']) > 0:
        return render_template(template, topic=user_input, object=search_results, see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app//simplified_output/elex_tweets?_search=" + user_input + "&_sort_desc=created_at_est")
    else:
        not_found = "No results found"
        return render_template(template, topic=not_found, object=search_results, see_all="https://ga-elex-twitter-sx7bcyrkda-ue.a.run.app/simplified_output/elex_tweets")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)