
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """ 
<!doctype html>
<html lang="fa">
<head>
    <meta charset="utf-8">
    <title>محاسبه درصد آزمون تیزهوشان</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; direction: rtl; background-color: #f9f9f9;}
        .container { background: #fff; padding: 30px; border-radius: 10px; display: inline-block;}
        input[type=number] { padding: 10px; margin: 10px; width: 80px; }
        input[type=submit] { padding: 10px 20px; margin-top: 20px; }
        .result { margin-top: 20px; font-size: 20px; color: green; }
        .footer { margin-top: 30px; font-size: 14px; }
        .footer a { text-decoration: none; color: #007bff; }
    </style>
</head>
<body>
    <div class="container">
        <h2>محاسبه درصد آزمون تیزهوشان ششم به هفتم</h2>
        <form method="POST">
            <h4>دفترچه اول:</h4>
            <label>تعداد پاسخ درست:</label><br>
            <input type="number" name="correct1" min="0" required><br>
            <label>تعداد پاسخ غلط:</label><br>
            <input type="number" name="wrong1" min="0" required><br>

            <h4>دفترچه دوم:</h4>
            <label>تعداد پاسخ درست:</label><br>
            <input type="number" name="correct2" min="0" required><br>
            <label>تعداد پاسخ غلط:</label><br>
            <input type="number" name="wrong2" min="0" required><br>

            <input type="submit" value="محاسبه درصد">
        </form>
        {% if result is not none %}
            <div class="result">درصد نهایی شما: {{ result }}٪</div>
        {% endif %}
        <div class="footer">
            <p>ما را در شبکه‌های اجتماعی دنبال کنید:</p>
            <p>
                <a href="https://instagram.com/mohamadiriazi">اینستاگرام</a> |
                <a href="https://t.me/mohamadiriazi">تلگرام</a>
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            correct1 = int(request.form["correct1"])
            wrong1 = int(request.form["wrong1"])
            correct2 = int(request.form["correct2"])
            wrong2 = int(request.form["wrong2"])

            score1 = ((correct1 * 3) - wrong1) / (60 * 3) * 100
            score2 = ((correct2 * 3) - wrong2) / (60 * 3) * 100
            total_score = ((score1 * 3) + score2) / 4
            result = round(total_score, 2)
        except:
            result = "خطا در محاسبات"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
