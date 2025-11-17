from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import random


app = Flask(__name__)

                    # Configuration 
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

# Initialize Flask-Session
Session(app)

@app.route("/")
def index():
    # If no username in session, redirect to login
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Record the user name in session
        session["name"] = request.form.get("mail")[1:]
        session["mail"]= request.form.get("mail")
        session["password"] = request.form.get("password")
        session["mails"] = []


        nutzerDatenbank = ["doswalt"]
        passwortDatenbank = ["ganzGeheimesPasswort"]

        for i in range(10):
            session["mails"] += [[[betreffzeilen[i]],[email_inhalte[i]], [Absender[i]]]]

        if session["mail"] not in nutzerDatenbank:
            
            return "<script> document.getElementById('loginForm').reset(); ;alert('Nutzer gibt es nicht du Hund');</script>"
        else:
            if session["password"] not in passwortDatenbank:
                session["password"] = ""
                session["mail"]= ""
                return "<script> document.getElementById('loginForm').reset(); alert('Passwort ist falsch');</script>"
                return redirect("/login")

            else:
                return redirect("/")

        
        
        print(session["mails"])

        
        
    return render_template("login.html")


abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
Absender = [
    "max.mustermann@example.com",
    "anna.schmidt@example.com",
    "peter.müller@example.com",
    "lisa.meier@example.com",
    "jan.klein@example.com",
    "sara.schneider@example.com",
    "tom.hoffmann@example.com",
    "julia.braun@example.com",
    "michael.wagner@example.com",
    "laura.fischer@example.com"
]

email_inhalte = [
    "Hallo Max,\n\nIch hoffe, es geht dir gut! Ich wollte dich fragen, ob du am Freitag Zeit hast, um uns zu treffen.\n\nViele Grüße,\nAnna",
    "Liebe Anna,\n\nVielen Dank für deine Nachricht! Freitag passt mir gut. Lass uns um 15 Uhr im Café treffen.\n\nHerzliche Grüße,\nMax",
    "Hallo Peter,\n\nIch wollte dir nur kurz Bescheid geben, dass das Meeting auf nächste Woche verschoben wurde.\n\nBeste Grüße,\nLisa",
    "Hi Lisa,\n\nDanke für die Info! Ich werde die Änderungen im Kalender aktualisieren.\n\nViele Grüße,\nPeter",
    "Hallo Jan,\n\nIch habe die Unterlagen für das Projekt fertiggestellt. Lass mich wissen, wenn du sie durchsehen möchtest.\n\nGrüße,\nTom",
    "Liebe Sara,\n\nIch freue mich auf unser Treffen nächste Woche! Hast du schon einen Termin im Kopf?\n\nAlles Gute,\nJulia",
    "Hallo Tom,\n\nIch wollte dir nur sagen, dass ich die Präsentation für das Meeting vorbereitet habe. Ich hoffe, sie gefällt dir!\n\nBeste Grüße,\nMichael",
    "Hi Julia,\n\nDie Präsentation sieht großartig aus! Ich habe ein paar kleine Anmerkungen, die wir besprechen sollten.\n\nHerzliche Grüße,\nTom",
    "Hallo Michael,\n\nIch habe die neuen Daten für das Projekt erhalten. Lass uns darüber sprechen, wenn du Zeit hast.\n\nViele Grüße,\nLaura",
    "Liebe Laura,\n\nDanke für die Info! Ich bin am Donnerstag verfügbar, um die Daten zu besprechen.\n\nBeste Grüße,\nMichael"
]

betreffzeilen = [
    "Treffen am Freitag",
    "Bestätigung des Meetings",
    "Änderung des Projektzeitplans",
    "Unterlagen für das Projekt",
    "Vorbereitung der Präsentation",
    "Fragen zum nächsten Treffen",
    "Neue Daten für das Projekt",
    "Feedback zur Präsentation",
    "Einladung zum Team-Meeting",
    "Wichtige Informationen zur Deadline"
]



@app.route("/inbox")
def inbox():
    if session["name"] != None:
        


        
        return render_template("inbox.html")


    else:
        return render_template("login.html") # + pls login to access


@app.route("/logout")
def logout():
    # Clear the username from session
    session["name"] = None
    session["mail"]= None
    session["password"] = None
    return redirect("/")

    

if __name__ == "__main__":
    app.run(debug=True)
