from app import create_app
fd, db = tempfile.mkstemp()
os.environ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db
app = create_app()
app.run(host='0.0.0.0')