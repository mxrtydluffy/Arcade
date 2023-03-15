from blog import create_app

if __name__ == "__main__":
    app = create_app()
    # automatically reruns flask web server without manually stopping it.
    app.run(debug=True)