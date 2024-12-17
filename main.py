# 

from flask import Flask, request, jsonify
import pandas as pd
import random

# Initialize Flask app
app = Flask(__name__)

# Read the tea recommendation data
tea_rec_df = pd.read_csv('/home/tj/development/Gami/Tea_simple/tea_rec.csv', on_bad_lines='skip')
# Read the tea facts data with low_memory=False
tea_facts_df = pd.read_csv('/home/tj/development/Gami/Tea_simple/tea_facts.csv', sep=";")

@app.route("/")
def get_home_page():
    with open("index.html", "r") as file:
        return file.read()

@app.route("/recommend_tea", methods=["GET"])
def recommend_tea():
    mood = request.args.get('mood')
    time_of_day = request.args.get('time_of_day')
# @app.route("/get_tea_options", methods=["GET"])
# def get_tea_options():
#     moods = tea_rec_df['Mood'].unique().tolist()
#     times_of_day = tea_rec_df['Time of Day'].unique().tolist()
#     return jsonify({
#         "moods": moods,
#         "times_of_day": times_of_day
#     })

  
    # Logic for tea recommendation based on mood and time of day
    recommended_tea = tea_rec_df[(tea_rec_df['Mood'] == mood) & (tea_rec_df['Time of Day'] == time_of_day)]
    
    if not recommended_tea.empty:
        tea = recommended_tea.sample(1).iloc[0]
        tea_name = tea['Tea Name']
        tea_image_url = tea['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIyVBZ60B1v77cZXE6GDhg7HSML_Do4XpM1A&s']  # Assuming the URL is stored in the 'Image_url' column
        fun_fact = tea_facts_df.sample(1)['Fact'].iloc[0]  # Random fun fact
        return jsonify({
            "tea_name": tea_name,
            "tea_image_url": tea_image_url,
            "fun_fact": fun_fact
        })
    else:
        return jsonify({"error": "No matching tea found for the given mood and time."})

@app.route("/get_tea_options", methods=["GET"])
def get_tea_options():
    moods = tea_rec_df['Mood'].unique().tolist()
    times_of_day = tea_rec_df['Time of Day'].unique().tolist()
    return jsonify({
        "moods": moods,
        "times_of_day": times_of_day
    })

if __name__ == "__main__":
    app.run(debug=True)
