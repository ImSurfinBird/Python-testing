import pygame as pg
import ObjectHandling as obj


def drag_and_drop(mouse_button1, mouse_coords, object_data):
    if mouse_button1[0] == 1 and mouse_coords[0] in range(object_data['x'], object_data['x'] + object_data['width']) and mouse_coords[1] in range(object_data['y'], object_data['y'] + object_data['height']):
        object_data['drag'] = True
    if mouse_button1[0] == 0 and object_data['drag']:
        object_data['drag'] = False
        object_data['x'] = mouse_coords[0] - int(object_data['width'] / 2)
        object_data['y'] = mouse_coords[1] - int(object_data['height'] / 2)
    return object_data


def move_path(object_data):
    for s in range(object_data['speed']):
        if(object_data['x'], object_data['y']) in object_data['path'].keys():
            object_data['direction'] = object_data['path'][(object_data['x'], object_data['y'])]
        if object_data['direction'] == 'UP':
            object_data['y'] -= 1
        if object_data['direction'] == 'DOWN':
            object_data['y'] += 1
        if object_data['direction'] == 'LEFT':
            object_data['x'] -= 1
        if object_data['direction'] == 'RIGHT':
            object_data['x'] += 1
    return object_data


def move(object_data):
    if object_data['direction'] == 'UP':
        object_data['y'] -= object_data['speed']
    if object_data['direction'] == 'DOWN':
        object_data['y'] += object_data['speed']
    if object_data['direction'] == 'LEFT':
        object_data['x'] -= object_data['speed']
    if object_data['direction'] == 'RIGHT':
        object_data['x'] += object_data['speed']
    return object_data
