import os, sys, json, shutil

def convert_series(series, destination):
    if not os.path.exists(f"{destination}/series"):
        os.makedirs(f"{destination}/series")
    for serie in series:
        name = serie["name"]
        if not os.path.exists(f"{destination}/series/{name}"):
            os.makedirs(f"{destination}/series/{name}")
        for i, season in enumerate(serie["seasons"]):
            season_number = str(i + 1).zfill(3)
            if not os.path.exists(f"{destination}/series/{name}/Season {season_number}"):
                os.makedirs(f"{destination}/series/{name}/Season {season_number}")
            for j, episode in enumerate(season["episodes"]):
                episode_number = str(j + 1).zfill(3)
                file = episode["file"]
                if os.path.exists(file):
                    _, file_extension = os.path.splitext(file)
                    shutil.copy(file, f"{destination}/series/{name}/Season {season_number}/{name} S{season_number}E{episode_number}{file_extension}")

def convert_movies(movies, destination):
    if not os.path.exists(f"{destination}/movies"):
        os.makedirs(f"{destination}/movies")
    for movie in movies:
        name = movie["name"]
        file = movie["file"]
        if os.path.exists(file):
            _, file_extension = os.path.splitext(file)
            shutil.copy(file, f"{destination}/movies/{name}{file_extension}")

def convert(config, destination):
    if "series" in config:
        convert_series(config["series"], destination)
    if "movies" in config:
        convert_movies(config["movies"], destination)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert.py <config file> <destination>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    if not os.path.exists(config_file):
        print(f"File '{config_file}' not found!")
        sys.exit(1)
    destination = sys.argv[2]

    with open(config_file, "r") as file:
        convert(json.load(file), destination)