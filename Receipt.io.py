from flask import Flask, request, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
configure_uploads(app, photos)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'photos' in request.files:
        print("HELLO")
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
