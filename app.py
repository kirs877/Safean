from flask import Flask, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Sample football data
teams = [
    {"id": 1, "name": "الريال مدريد", "country": "إسبانيا", "founded": 1902, "stadium": "سانتياغو برنابيو"},
    {"id": 2, "name": "برشلونة", "country": "إسبانيا", "founded": 1899, "stadium": "كامب نو"},
    {"id": 3, "name": "مانشستر يونايتد", "country": "إنجلترا", "founded": 1878, "stadium": "أولد ترافورد"},
    {"id": 4, "name": "بايرن ميونخ", "country": "ألمانيا", "founded": 1900, "stadium": "أليانز أرينا"},
    {"id": 5, "name": "باريس سان جيرمان", "country": "فرنسا", "founded": 1970, "stadium": "حديقة الأمراء"},
    {"id": 6, "name": "يوفنتوس", "country": "إيطاليا", "founded": 1897, "stadium": "أليانز ستاديوم"}
]

matches = [
    {"id": 1, "team1": "الريال مدريد", "team2": "برشلونة", "date": "2024-01-15", "time": "20:00", "competition": "الليغا"},
    {"id": 2, "team1": "مانشستر يونايتد", "team2": "مانشستر سيتي", "date": "2024-01-16", "time": "17:30", "competition": "الدوري الإنجليزي"},
    {"id": 3, "team1": "بايرن ميونخ", "team2": "دورتموند", "date": "2024-01-17", "time": "18:30", "competition": "البوندسليغا"},
    {"id": 4, "team1": "باريس سان جيرمان", "team2": "مارسيليا", "date": "2024-01-18", "time": "21:00", "competition": "الدوري الفرنسي"}
]

news = [
    {
        "id": 1,
        "title": "انتقال نجم جديد إلى الريال مدريد",
        "summary": "الريال مدريد يضم لاعباً جديداً في صفقة قياسية",
        "date": "2024-01-10",
        "category": "انتقالات"
    },
    {
        "id": 2,
        "title": "برشلونة يفوز في الكلاسيكو",
        "summary": "فوز مثير لبرشلونة على الريال مدريد بنتيجة 3-2",
        "date": "2024-01-09",
        "category": "نتائج المباريات"
    },
    {
        "id": 3,
        "title": "تأهل مانشستر يونايتد لنصف النهائي",
        "summary": "مانشستر يونايتد يتأهل لنصف نهائي دوري أبطال أوروبا",
        "date": "2024-01-08",
        "category": "دوري أبطال أوروبا"
    }
]

@app.route('/')
def home():
    return render_template('index.html', teams=teams[:4], matches=matches[:3], news=news[:3])

@app.route('/teams')
def teams_page():
    return render_template('teams.html', teams=teams)

@app.route('/matches')
def matches_page():
    return render_template('matches.html', matches=matches)

@app.route('/news')
def news_page():
    return render_template('news.html', news=news)

@app.route('/api/teams')
def api_teams():
    return jsonify(teams)

@app.route('/api/matches')
def api_matches():
    return jsonify(matches)

@app.route('/api/news')
def api_news():
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)