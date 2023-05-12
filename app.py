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
    <div style ="position : fixed; left:50px;top:30 px;width:800px;height:100px;background-color:white;z-index:500">
    <br>  </br>
    
    <form>
    <select name="YourLocation">
    <option value="Taipei">台北</option>
    <option value="Taoyuan">桃園</option>
    <option value="Hsinchu">新竹</option>
    <option value="Miaoli">苗栗</option>
        </select>
    </form>
        <button style="font-size:20px;">  確定 </button>

    </div>
   
    """))

    map.save("output.html")

    folium.Marker(
        location=[25.030797164609954, 121.55874457225863],
        tooltip ="好玩嘗試xddd"

    ).add_to(map)

 
    return map._repr_html_()


       


if __name__ == '__main__':
    app.run(debug=True)