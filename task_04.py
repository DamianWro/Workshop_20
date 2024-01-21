from flask import Flask, request
app = Flask(__name__)

HTML_Start = """
<!DOCTYPE HTML>
<html lang="EN">
    <head>
        <meta charset="utf-8"/>
        <meta name="description" content="" />
        <meta name="keywords" content="" />
        <title>LET'S PLAY THE GAME</title>
    </head>
        <body>
            <header>
                <h1>IMAGINE NUMBER BETWEEN 1 AND 1000</h1>
                <form action="/" method="post">
                <input type="hidden" name="min" value="{}"></input>
                <input type="hidden" name="max" value="{}"></input>
                <input type="submit" value="START"></input>
        </form>
    </body>
</html>"""


HTML_Play = """
<!DOCTYPE HTML>
<html lang="EN">
    <head>
        <meta charset="utf-8"/>
        <meta name="description" content="" />
        <meta name="keywords" content="" />
        <title>is this correct figures?</title>
    </head>
    <body>
        <header>
            <h1>It is number {guess}????</h1>
            <form action="" method="post">
            <input type="submit" name="user_answer" value="too big">
            <input type="submit" name="user_answer" value="too small">
            <input type="submit" name="user_answer" value="you won">
            <input type="hidden" name="min" value="{min}">
            <input type="hidden" name="max" value="{max}">
            <input type="hidden" name="guess" value="{guess}">
       </form>
    </body>
</html>
"""


HTML_WIN = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
            <title>Guess The Number</title>
    </head>
        <body>
            <h1>Great I guess! Your number is {guess}</h1>
        </body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def guess_computer_figures():
    if request.method == "GET":
        return HTML_Start.format(1,1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return HTML_WIN.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return HTML_Play.format(guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run()


