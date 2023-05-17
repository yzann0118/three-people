from flask import Flask,request, render_template
import folium

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])


def base():
    map = folium.Map(
        location=[25.030797164609954, 121.55874457225863],
        zoom_start=12
        
    )
    map.get_root().html.add_child(folium.Element("""
    <html>

    <head>
        <title>三人組道安平台</title>
    </head>
    <body>
        <div style ="position : fixed; left:1200px;top:30 px;width:400px;height:2000px;background-color:white;z-index:500">
        
        <form>
            
            <br>區域選擇  <select name="Location">
            <option value="Taipei">台北</option>
            <option value="Taoyuan">桃園</option>
            <option value="Hsinchu">新竹</option>
            <option value="Miaoli">苗栗</option>
            </select>
        <br></br>
        </form>
        <button style="font-size:20px;" type="summit">  確定 </button>
        <input type="submit" value="確定" />
        <br></br>

        <form action="" method='post' style="">
            
            <input type=file name=file>
            <br>請輸入搜尋位置<input type=summit value="位置" name="搜尋位置按鈕">
            
        </form>
        </div>

    </body>
    </html>
   
    """))

    map.save("output.html")

    folium.Marker(
        location=[25.030797164609954, 121.55874457225863],
        tooltip ="好玩嘗試xddd"

    ).add_to(map)

 
    return map._repr_html_()

@app.route('/page1')
def page():
    return render_template('111年臺北市無號誌交叉口原始點資料_縮放人數_new.html')


if __name__ == '__main__':
    app.run(debug=True)