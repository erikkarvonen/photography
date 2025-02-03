import json
import os

# Load album data
with open("data.json") as f:
    albums = json.load(f)

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Read template files
with open("templates/index.html") as f:
    index_template = f.read()
with open("templates/album.html") as f:
    album_template = f.read()

# Generate index.html
index_html = index_template.replace("{{ albums }}", "\n".join(
    f'<li><a href="{name.replace(" ", "_")}.html">{name}</a></li>' for name in albums
))
with open("output/index.html", "w") as f:
    f.write(index_html)

# Generate album pages
for album_name, images in albums.items():
    image_tags = "\n".join(f'<img src="{image}" alt="Photo">' for image in images)
    album_html = album_template.replace("{{ album_name }}", album_name).replace("{{ images }}", image_tags)

    album_filename = f"output/{album_name.replace(' ', '_')}.html"
    with open(album_filename, "w") as f:
        f.write(album_html)

print("Static site generated in /output")
