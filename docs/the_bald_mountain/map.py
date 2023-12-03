import pandas as pd
import folium as folium


def create_marker(lat: float, long: float, name: str, img: str, color: str="green") -> folium.Marker:
    """Creates a folium.Marker object at the given location, with a custom popup contianing an image and a title."""

    html = f"""<div>
                    <h1>{name}<h1/>
                    <img src='http://localhost:5000/image/{img if img else "no_img"}' width=400 height=300>
                <div>
            """
    popup = folium.Popup(html, max_width=400, lazy=True)
    return folium.Marker(location=(lat, long), popup=popup, icon=folium.Icon(color=color, icon=("leaf" if img else "")))


def create_map(lang="hun"):
    """Parses the excel file containing the coordinates and the names of the images into a folium.Map object, 
    with a trail corresponding to each worksheet."""

    M_CENTER = (48.129591, 21.379145)
    ZOOM_START = 15
    MIN_ZOOM = 15

    m = folium.Map(location=M_CENTER, zoom_start=ZOOM_START, min_zoom=MIN_ZOOM)


    dfs = pd.read_excel("routes.xlsx", sheet_name=None)

    for route in dfs:
        df = dfs[route]
        color = route.split(" ")[0]
        df[["lat", "long"]] = df["lat_long"].str.split(",", expand=True).astype("float")
        df["img"] = df["img"].fillna("")
        df[f"name_{lang}"] = df[f"name_{lang}"].fillna("")
        folium.PolyLine(locations=df.loc[:, ["lat", "long"]], color=color).add_to(m)
        df.apply(lambda row: (create_marker(lat=row["lat"], 
                                           long=row["long"], 
                                           name=row[f"name_{lang}"], 
                                           img=row["img"], 
                                           color=color)
                                           .add_to(m)) if row[f"name_{lang}"] else None, axis=1)

    m.save("./templates/map.html")
    print("Map saved.")


if __name__ == "__main__":
    create_map()
