from learning_flashcards import app

@app.route('/')
def index():
    return 'Hello World!'