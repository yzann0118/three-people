from flask import Flask, request, render_template, Response
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
            results = model.predict(frame)
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
    return render_template('cameratest.html', camera_id=camera_id)

@app.route('/CCTVmap')
def CCTVmap():
    return render_template('臺北市CCTV設施地圖.html')


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




# @app.route('/', methods=['POST', 'GET'])


# def base():
#     map = folium.Map(
#         location=[25.030797164609954, 121.55874457225863],
#         zoom_start=12
        
#     )
#     map.get_root().html.add_child(folium.Element("""
#     <html>

#     <head>
#         <title>三人組道安平台</title>
#     </head>
#     <body>
#         <div style ="position : fixed; left:1200px;top:30 px;width:400px;height:2000px;background-color:white;z-index:500">
        
#         <form>
            
#             <br>區域選擇  <select name="Location">
#             <option value="Taipei">台北</option>
#             <option value="Taoyuan">桃園</option>
#             <option value="Hsinchu">新竹</option>
#             <option value="Miaoli">苗栗</option>
#             </select>
#         <br></br>
#         </form>

#         <form action="/page1">


#             <button style="font-size:20px;" type="summit">  無號誌交叉口 </button>
#         </form>

        
#         <form action="/page1">
#             <input type="submit" value="無號誌交叉口" />
#         </form>
#         <br></br>

#         <form action="" method='post' style="">
            
#             <input type=file name=file>
#             <br>請輸入搜尋位置<input type=summit value="位置" name="搜尋位置按鈕">
            
#         </form>
#         </div>

#     </body>
#     </html>
   
#     """))

#     map.save("output.html")

#     folium.Marker(
#         location=[25.030797164609954, 121.55874457225863],
#         tooltip ="好玩嘗試xddd"

#     ).add_to(map)

 
#     return map._repr_html_()

# @app.route('/page1')
# def page():
#     return render_template('111年臺北市無號誌交叉口原始點資料_縮放人數_new.html')



if __name__ == '__main__':
    app.run(debug=True)