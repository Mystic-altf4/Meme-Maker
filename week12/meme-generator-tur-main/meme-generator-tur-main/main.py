# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        ust_metin = request.form.get("textTop")
        alt_metin = request.form.get("textBottom")
        # Görev #3. Metnin konumunu almak
        ust_metin_y_konum = request.form.get("textTop_y")
        alt_metin_y_konum = request.form.get("textBottom_y")
        ust_metin_x_konum = request.form.get("textTop_x")
        alt_metin_x_konum = request.form.get("textBottom_x")
        # Görev #3. Metnin rengini almak
        renk = request.form.get("color-selector")

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               ust_metin=ust_metin,
                               alt_metin=alt_metin,

                               # Görev #3. Rengi görüntüleme
                               renk=renk,
                               
                               # Görev #3. Metnin konumunu görüntüleme
                                ust_metin_y_konum=ust_metin_y_konum,
                                alt_metin_y_konum=alt_metin_y_konum,
                                ust_metin_x_konum=ust_metin_x_konum,
                                alt_metin_x_konum=alt_metin_x_konum
                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
