from flask import Flask

import folium

app = Flask(__name__)


@app.route('/')
def base():
    map = folium.Map(
        location=[25.030797164609954, 121.55874457225863],
        zoom_start=12,
        popup='Skytree'
    )

    folium.Marker(
        location=[25.030797164609954, 121.55874457225863],
        
        tooltip="好玩的嘗試XDD"

    ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)