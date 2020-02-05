from app import create_app, db
# from app.models import UploadInfo, FileInfo # tables
from flask_migrate import Migrate

app = create_app('remote')
migrate = Migrate(app,db)

@app.shell_context_processor #what is this
def make_shell_context():
    return dict(db=db)
