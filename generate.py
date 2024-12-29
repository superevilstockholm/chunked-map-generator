from PIL import Image, ImageDraw
import random

details_json = {
    "tile_1": {
        "side": {
            "left": "grass",
            "top": "grass",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "grass",
            "right": "dirt",
            "bottom": "grass"
        }
    },
    "tile_2": {
        "side": {
            "left": "grass",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "dirt",
            "right": "dirt",
            "bottom": "grass"
        }
    },
    "tile_3": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "dirt",
            "right": "grass",
            "bottom": "dirt"
        }
    },
    "tile_4": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "dirt",
            "top": "grass",
            "right": "dirt",
            "bottom": "dirt"
        }
    },
    "tile_5": {
        "side": {
            "left": "dirt",
            "top": "grass",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "grass",
            "right": "dirt",
            "bottom": "dirt"
        }
    },
    "tile_6": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "dirt",
            "top": "grass",
            "right": "dirt",
            "bottom": "grass"
        }
    },
    "tile_7": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "grass",
            "bottom": "dirt"
        },
        "angle": {
            "left": "dirt",
            "top": "grass",
            "right": "grass",
            "bottom": "dirt"
        }
    },
    "tile_8": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "dirt",
            "top": "dirt",
            "right": "grass",
            "bottom": "dirt"
        }
    },
    "tile_9": {
        "side": {
            "left": "grass",
            "top": "dirt",
            "right": "dirt",
            "bottom": "grass"
        },
        "angle": {
            "left": "grass",
            "top": "dirt",
            "right": "grass",
            "bottom": "grass"
        }
    },
    "tile_10": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "grass",
            "bottom": "grass"
        },
        "angle": {
            "left": "dirt",
            "top": "grass",
            "right": "grass",
            "bottom": "grass"
        }
    },
    "tile_11": {
        "side": {
            "left": "grass",
            "top": "grass",
            "right": "grass",
            "bottom": "grass"
        },
        "angle": {
            "left": "grass",
            "top": "grass",
            "right": "grass",
            "bottom": "grass"
        }
    },
    "tile_12": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "grass"
        }
    },
    "tile_13": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        }
    },
    "tile_14": {
        "side": {
            "left": "dirt",
            "top": "grass",
            "right": "grass",
            "bottom": "dirt"
        },
        "angle": {
            "left": "grass",
            "top": "grass",
            "right": "grass",
            "bottom": "dirt"
        }
    },
    "tile_15": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "grass"
        },
        "angle": {
            "left": "dirt",
            "top": "dirt",
            "right": "grass",
            "bottom": "grass"
        }
    },
    "tile_16": {
        "side": {
            "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        },
        "angle": {
        "left": "dirt",
            "top": "dirt",
            "right": "dirt",
            "bottom": "dirt"
        }
    }
}

example_map = [
    [11, 11, 11, 11, 9, 15],
    [11, 11, 11, 11, 11, 11],
    [11, 11, 1, 5, 5, 5],
    [11, 11, 2, 16, 8, 12],
    [11, 11, 9, 16, 10, 9],
    [14, 11, 11, 11, 11, 11]
]

def generate_random_map_chunk(grid_width, grid_height, details_json):
    """Menghasilkan peta acak dengan aturan tertentu, dengan kontrol proporsi dirt dan grass."""
    
    map_chunk = [[None for _ in range(grid_width)] for _ in range(grid_height)]
    
    def valid_tile(x, y, tile_index):
        tile = details_json[f"tile_{tile_index}"]
        if x > 0:
            left_tile = map_chunk[y][x-1]
            if left_tile and details_json[f"tile_{left_tile}"]["side"]["right"] != tile["side"]["left"]:
                return False
        if y > 0:
            top_tile = map_chunk[y-1][x]
            if top_tile and details_json[f"tile_{top_tile}"]["side"]["bottom"] != tile["side"]["top"]:
                return False
        if x < grid_width - 1:
            right_tile = map_chunk[y][x+1]
            if right_tile and details_json[f"tile_{right_tile}"]["side"]["left"] != tile["side"]["right"]:
                return False
        if y < grid_height - 1:
            bottom_tile = map_chunk[y+1][x]
            if bottom_tile and details_json[f"tile_{bottom_tile}"]["side"]["top"] != tile["side"]["bottom"]:
                return False
        return True
    
    def is_surrounded_by_dirt(x, y):
        """Memeriksa apakah tile dikelilingi oleh dirt sepenuhnya atau sebagian besar."""
        dirt_count = 0
        if x > 0:
            left_tile = map_chunk[y][x-1]
            if left_tile and "dirt" in details_json[f"tile_{left_tile}"]["side"].values():
                dirt_count += 1
        if y > 0:
            top_tile = map_chunk[y-1][x]
            if top_tile and "dirt" in details_json[f"tile_{top_tile}"]["side"].values():
                dirt_count += 1
        if x < grid_width - 1:
            right_tile = map_chunk[y][x+1]
            if right_tile and "dirt" in details_json[f"tile_{right_tile}"]["side"].values():
                dirt_count += 1
        if y < grid_height - 1:
            bottom_tile = map_chunk[y+1][x]
            if bottom_tile and "dirt" in details_json[f"tile_{bottom_tile}"]["side"].values():
                dirt_count += 1
        return dirt_count >= 2

    def is_tile_heavy_dirt(tile_index):
        """Memeriksa apakah tile sebagian besar berisi dirt daripada grass."""
        tile = details_json[f"tile_{tile_index}"]
        
        dirt_count = sum(1 for side in tile["side"].values() if side == "dirt")
        grass_count = sum(1 for side in tile["side"].values() if side == "grass")
        
        if dirt_count > 2 or grass_count == 0:
            return True
        
        return False

    for y in range(grid_height):
        for x in range(grid_width):
            placed_tile = False
            
            possible_tiles = list(details_json.keys())
            random.shuffle(possible_tiles)
            
            for tile_key in possible_tiles:
                tile_index = int(tile_key.split('_')[1])

                if is_surrounded_by_dirt(x, y):
                    tile_index = 16
                elif is_tile_heavy_dirt(tile_index):
                    tile_index = 16

                if valid_tile(x, y, tile_index):
                    map_chunk[y][x] = tile_index
                    placed_tile = True
                    break
            
            if not placed_tile:
                map_chunk[y][x] = 11

    return map_chunk

def generate_random_map_chunk(grid_width, grid_height, details_json):
    """Menghasilkan peta acak dengan aturan tertentu, dengan preferensi untuk grass atau dirt penuh."""
    
    map_chunk = [[None for _ in range(grid_width)] for _ in range(grid_height)]
    
    def valid_tile(x, y, tile_index):
        tile = details_json[f"tile_{tile_index}"]
        if x > 0:
            left_tile = map_chunk[y][x-1]
            if left_tile and details_json[f"tile_{left_tile}"]["side"]["right"] != tile["side"]["left"]:
                return False
        if y > 0:
            top_tile = map_chunk[y-1][x]
            if top_tile and details_json[f"tile_{top_tile}"]["side"]["bottom"] != tile["side"]["top"]:
                return False
        if x < grid_width - 1:
            right_tile = map_chunk[y][x+1]
            if right_tile and details_json[f"tile_{right_tile}"]["side"]["left"] != tile["side"]["right"]:
                return False
        if y < grid_height - 1:
            bottom_tile = map_chunk[y+1][x]
            if bottom_tile and details_json[f"tile_{bottom_tile}"]["side"]["top"] != tile["side"]["bottom"]:
                return False
        return True
    
    def is_surrounded_by_dirt(x, y):
        """Memeriksa apakah tile dikelilingi oleh dirt sepenuhnya atau sebagian besar."""
        dirt_count = 0
        if x > 0:
            left_tile = map_chunk[y][x-1]
            if left_tile and "dirt" in details_json[f"tile_{left_tile}"]["side"].values():
                dirt_count += 1
        if y > 0:
            top_tile = map_chunk[y-1][x]
            if top_tile and "dirt" in details_json[f"tile_{top_tile}"]["side"].values():
                dirt_count += 1
        if x < grid_width - 1:
            right_tile = map_chunk[y][x+1]
            if right_tile and "dirt" in details_json[f"tile_{right_tile}"]["side"].values():
                dirt_count += 1
        if y < grid_height - 1:
            bottom_tile = map_chunk[y+1][x]
            if bottom_tile and "dirt" in details_json[f"tile_{bottom_tile}"]["side"].values():
                dirt_count += 1
        
        return dirt_count >= 3

    def get_tile_weight(tile_index):
        tile = details_json[f"tile_{tile_index}"]
        if all(v == "grass" for v in tile["side"].values()) or all(v == "grass" for v in tile["angle"].values()):
            return 5
        if all(v == "dirt" for v in tile["side"].values()) or all(v == "dirt" for v in tile["angle"].values()):
            return 5
        return 1
    
    for y in range(grid_height):
        for x in range(grid_width):
            placed_tile = False
            
            possible_tiles = list(details_json.keys())
            tile_weights = [get_tile_weight(int(tile.split('_')[1])) for tile in possible_tiles]
            
            weighted_tiles = random.choices(possible_tiles, weights=tile_weights, k=len(possible_tiles))
            
            for tile_key in weighted_tiles:
                tile_index = int(tile_key.split('_')[1])

                if is_surrounded_by_dirt(x, y):
                    tile_index = 16

                if valid_tile(x, y, tile_index):
                    map_chunk[y][x] = tile_index
                    placed_tile = True
                    break
            
            if not placed_tile:
                map_chunk[y][x] = 11

    for y in range(grid_height):
        for x in range(grid_width):
            tile_index = map_chunk[y][x]
            tile = details_json[f"tile_{tile_index}"]
            
            if all(v == "dirt" for v in tile["side"].values()) and any(v == "grass" for v in tile["side"].values()):
                map_chunk[y][x] = 11

    return map_chunk

random_map = generate_random_map_chunk(20, 20, details_json)
# random_map = generate_custom_map_chunk(12, 12, details_json)

for row in random_map:
    print(row)

def draw_tile_grid(tile_grid, tile_width, tile_height, output_file):
    """Render grid ke dalam sebuah gambar dengan tile berbentuk belah ketupat dan offset diagonal ke kanan atas."""
    grid_width = len(tile_grid[0])
    grid_height = len(tile_grid)

    img_width = (grid_width + grid_height) * (tile_width // 2)
    img_height = (grid_width + grid_height) * (tile_height // 2)

    img = Image.new("RGBA", (img_width, img_height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    points = [
        (tile_width / 2, 0),
        (tile_width, tile_height / 2),
        (tile_width / 2, tile_height),
        (0, tile_height / 2)
    ]

    for y, row in enumerate(tile_grid):
        for x, tile_name in enumerate(row):
            if tile_name:
                try:
                    tile_image = Image.open(f"map_tile/tile_{tile_name}.png").convert("RGBA")
                except FileNotFoundError:
                    tile_image = Image.new("RGBA", (tile_width, tile_height), (200, 200, 200, 255))
                    draw_tile = ImageDraw.Draw(tile_image)
                    draw_tile.polygon(points, fill="gray")

                tile_image = tile_image.resize((tile_width, tile_height))

                x_offset = (x + y) * (tile_width // 2)
                y_offset = (y - x) * (tile_height // 2) + ((img_height // 2) - (tile_height // 2))

                img.paste(tile_image, (int(x_offset), int(y_offset)), tile_image)

    img.save(output_file)
    print(f"Tile grid saved to {output_file}")

draw_tile_grid(random_map, tile_width=100, tile_height=50, output_file="tile_grid_diamond_limited.png")