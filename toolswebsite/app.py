import os
from flask import Flask, request, send_file, render_template, send_from_directory
from PIL import Image
import io

# app = Flask(__name__)
app = Flask(__name__, static_folder='templates')

@app.route('/templates/<path:path>')
def send_static(path):
    return send_from_directory('templates', path)

# 主页
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# JPG转PNG页面
@app.route('/jpgtopng', methods=['GET'])
def jpg_to_png():
    return render_template('jpgtopng.html')

# JPG转PNG API
@app.route("/api/jpgtopng", methods=["POST"])
def convert_jpg_to_png():
    if "image" not in request.files:
        return "No image provided", 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return "No image provided", 401

    if image_file and image_file.filename.lower().endswith(".jpg"):
        try:
            image = Image.open(image_file).convert("RGBA")
            png_image = io.BytesIO()
            image.save(png_image, "PNG")
            png_image.seek(0)
            return send_file(png_image, attachment_filename="converted_image.png", as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    return "Invalid file format", 402


@app.route('/pngtojpg', methods=['GET'])
def png_to_jpg():
    return render_template('pngtojpg.html')

@app.route("/api/pngtojpg", methods=["POST"])
def convert_png_to_jpg():
    if "image" not in request.files:
        return "No image provided", 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return "No image provided", 400

    if image_file and image_file.filename.lower().endswith(".png"):
        try:
            image = Image.open(image_file).convert("RGB")
            jpg_image = io.BytesIO()
            image.save(jpg_image, "JPEG")
            jpg_image.seek(0)
            return send_file(jpg_image, attachment_filename="converted_image.jpg", as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    return "Invalid file format", 400


@app.route('/webptopng', methods=['GET'])
def webp_to_png():
    return render_template('webptopng.html')

@app.route("/api/webptopng", methods=["POST"])
def convert_webp_to_png():
    if "image" not in request.files:
        return "No image provided", 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return "No image provided", 400

    if image_file and image_file.filename.lower().endswith(".webp"):
        try:
            with Image.open(image_file) as image:
                image = image.convert("RGBA")
                png_image = io.BytesIO()
                image.save(png_image, "PNG")
                png_image.seek(0)
                return send_file(png_image, attachment_filename="converted_image.png", as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    return "Invalid file format", 400


@app.route('/bmptopng', methods=['GET'])
def bmp_to_png():
    return render_template('bmptopng.html')

@app.route("/api/bmptopng", methods=["POST"])
def convert_bmp_to_png():
    if "image" not in request.files:
        return "No image provided", 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return "No image provided", 400

    if image_file and image_file.filename.lower().endswith(".bmp"):
        try:
            image = Image.open(image_file).convert("RGBA")
            png_image = io.BytesIO()
            image.save(png_image, "PNG")
            png_image.seek(0)
            return send_file(png_image, attachment_filename="converted_image.png", as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    return "Invalid file format", 400


@app.route('/pngtopdf', methods=['GET'])
def png_to_pdf():
    return render_template('pngtopdf.html')

@app.route("/api/pngtopdf", methods=["POST"])
def convert_png_to_pdf():
    if "image" not in request.files:
        return "No image provided", 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return "No image provided", 400

    if image_file and image_file.filename.lower().endswith(".png"):
        try:
            image = Image.open(image_file).convert("RGB")
            pdf_image = io.BytesIO()
            image.save(pdf_image, "PDF", resolution=100.0)
            pdf_image.seek(0)
            return send_file(pdf_image, attachment_filename="converted_image.pdf", as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    return "Invalid file format", 400


if __name__ == '__main__':
    app.run(debug=True)
