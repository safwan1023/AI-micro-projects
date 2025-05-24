import folium

def get_color(pollution_level):
    # Simple coloring from green (low) to red (high)
    if pollution_level < 50:
        return 'green'
    elif pollution_level < 100:
        return 'orange'
    else:
        return 'red'

def main():
    print("Pollution Hotspot Mapper\nEnter sensor data. Type 'done' to finish.\n")

    data_points = []
    while True:
        inp = input("Enter data as 'latitude,longitude,pollution_level' (or 'done'): ")
        if inp.lower() == 'done':
            break
        try:
            lat, lon, level = inp.split(',')
            lat = float(lat.strip())
            lon = float(lon.strip())
            level = float(level.strip())
            data_points.append((lat, lon, level))
        except:
            print("Invalid input. Please enter data as: latitude,longitude,pollution_level")

    if not data_points:
        print("No data entered. Exiting.")
        return

    # Create map centered at average location
    avg_lat = sum(p[0] for p in data_points) / len(data_points)
    avg_lon = sum(p[1] for p in data_points) / len(data_points)
    pollution_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)

    # Add markers
    for lat, lon, level in data_points:
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            popup=f'Pollution Level: {level}',
            color=get_color(level),
            fill=True,
            fill_color=get_color(level)
        ).add_to(pollution_map)

    # Save map
    pollution_map.save('pollution_hotspots.html')
    print("\nPollution hotspot map saved as 'pollution_hotspots.html'. Open it in a browser to view.")

if __name__ == "__main__":
    main()
