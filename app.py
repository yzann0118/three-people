from flask import Flask, request, render_template, Response, json
import folium
from ultralytics import YOLO
import cv2

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')
            
def gen_result_frames(camera_id):
    model = YOLO("./yolov8n.pt")
    # model = YOLO("./yolov8m.pt")
    video_path = f"https://cctv.bote.gov.taipei:8501/mjpeg/{camera_id}" 
    cap = cv2.VideoCapture(video_path)
    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
        if success:
            # Run YOLOv8 inference on the frame
            # results = model.track(frame)
            results = model.predict(frame, device='cpu')
            result = results[0].plot()
            ret, buffer = cv2.imencode('.jpg', result)
            result = buffer.tobytes()
            yield (b'--result\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + result + b'\r\n')

@app.route('/video_feed/<camera_id>')
def video_feed(camera_id):
    #   return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=result')
    return Response(gen_result_frames(camera_id),
                    mimetype='multipart/x-mixed-replace; boundary=result')

@app.route('/detect/<camera_id>')
def detect(camera_id):
    if (int(camera_id)>400):
        return 'Wrong Camera ID !!'
    return render_template('camera_predict.html', camera_id=camera_id)

@app.route('/CCTVmap')
def CCTVmap():
    return render_template('臺北市CCTV設施地圖.html')

@app.route('/accident/30days/<year>')
def Days30(year):
    path = '30日_'+year+'.html'
    return render_template(path, year=year)

@app.route('/accident/unsignalized/<year>')
def Unsignal(year):
    path = '無號誌_'+year+'.html'
    return render_template(path, year=year)

@app.route('/accident/pendestrian/<year>')
def Pendestrian(year):
    path = '行人涉入_'+year+'.html'
    return render_template(path, year=year)

@app.route('/accident/total/<year>')
def Total(year):
    path = '交通事故_'+year+'.html'
    return render_template(path, year=year)

@app.route('/service')
def service_page():
    return render_template('111年臺北市無號誌交叉口原始點資料_縮放人數_new.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/map')
def map_page():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)