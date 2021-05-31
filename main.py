from app import app, db
from app.models import User, Post, Tea

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User':User, 'Post':Post, 'Tea':Tea}

if __name__ == "__main__":
    app.run(debug=False)