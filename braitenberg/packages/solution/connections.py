from typing import Tuple

import numpy as np

from solution.preprocessing import preprocess

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    height, width = shape
    half_width = width // 2
    road_mask = np.zeros((height, width))

    # Define the number of tiles
    num_tiles = 20

    # Define the initial and final widths of the road
    initial_width = width * 0.05
    final_width = width * 0.8

    # Define the height range for the road (2/3 of the total height)
    road_height = int(height * 2 / 3)

    # Calculate the width increase per tile
    width_increase = (final_width - initial_width) / num_tiles

    # Fill the image with tiles representing the road
    for i in range(num_tiles):
        # Calculate the current tile width
        current_width = initial_width + i * width_increase
        # Calculate the x-coordinates for the left and right edges of the tile
        left_edge = int((width - current_width) / 2)
        right_edge = int((width + current_width) / 2)
        # Calculate the y-coordinates for the top and bottom edges of the tile
        top_edge = height - road_height + int(i * road_height / num_tiles)
        bottom_edge = height - road_height + int((i + 1) * road_height / num_tiles)
        # Set the pixels in the tile region to 1
        road_mask[top_edge:bottom_edge, left_edge:right_edge] = -1.0
    # ---
    road_mask[:, half_width:] = 0.0
    return road_mask


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    height, width = shape
    half_width = width // 2
    road_mask = np.zeros((height, width))

    # Define the number of tiles
    num_tiles = 20

    # Define the initial and final widths of the road
    initial_width = width * 0.05
    final_width = width * 0.8

    # Define the height range for the road (2/3 of the total height)
    road_height = int(height * 2 / 3)

    # Calculate the width increase per tile
    width_increase = (final_width - initial_width) / num_tiles

    # Fill the image with tiles representing the road
    for i in range(num_tiles):
        # Calculate the current tile width
        current_width = initial_width + i * width_increase
        # Calculate the x-coordinates for the left and right edges of the tile
        left_edge = int((width - current_width) / 2)
        right_edge = int((width + current_width) / 2)
        # Calculate the y-coordinates for the top and bottom edges of the tile
        top_edge = height - road_height + int(i * road_height / num_tiles)
        bottom_edge = height - road_height + int((i + 1) * road_height / num_tiles)
        # Set the pixels in the tile region to 1
        road_mask[top_edge:bottom_edge, left_edge:right_edge] = -1.0
    # ---
    road_mask[:, :half_width] = 0.0
    return road_mask