from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    title = "DigitalEd - 2021 Red Evenlope"
    greetings = [
        "Wishing you happiness and prosperity; and an abundance of good fortune in your future!",
        "Happy New Year! The lucky star shines bright.",
        "Good luck and great success in the coming New Year!",
        "Happy Lunar New Year 2021! May a river of gold flow into your pockets.",
        "May you have many good fortunes according to your wishes. Happy Spring Festival!",
        "Happy New Lunary Year to you! Good luck in the year ahead and may treasures fill your home.",
        "At New Year and always, may peace and love fill your heart, beauty fill your world, and contentment and joy fill your days.",
        "Best wishes for the holidays and happiness throughout the New Year.",
        "New Year time is here. May every day hold happy hours for you.",
        "Season’s greetings and sincere wishes for a bright and happy New Year! Take good care of yourself in the year ahead.",
        "Wishing you a sparkling New Year and bright happy New Year! Take your passion and make it come true.",
        "Merriest of wishes for the Lunar New Year. May happiness follow you wherever you go!"
    ]
    fireworks = [1,2]
    greeting = random.choice(greetings)
    firework = random.choice(fireworks)
    return render_template('index.html', title = title, greeting = greeting, firework = firework)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug='True', port='80')