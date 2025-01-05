import geopandas as gpd
import matplotlib.pyplot as plt

# Load a GeoJSON dataset for the map of France
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson"
france_map = gpd.read_file(url)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_facecolor("none")  # Set background color to transparent

france_map.boundary.plot(ax=ax, edgecolor="#FF8C00", linewidth=1.5)  # Orange border (hex: #FF8C00)

# Remove axes and frame for a clean look
ax.axis("off")

# Save the map as an image
plt.savefig("france_map_theme.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()
