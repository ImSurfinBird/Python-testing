import pygame as pg


def duplicate_object(object_name, obj_list):
    return obj_list[object_name].copy()


def update_display(surface, surface_color, surface_dim, object_list):
    pg.draw.rect(surface, surface_color, (0, 0, surface_dim[0], surface_dim[1]))
    for x in object_list:
        display_object(surface, x, object_list)
    pg.display.update()


def remove_object(object_name, object_list):
    del(object_list[object_name])
    return object_list


def create_object(obj_list, obj_name, obj_coords, obj_image):
    obj_list[obj_name] = {
        'x': obj_coords[0],
        'y': obj_coords[1],
        'image': pg.image.load(obj_image).convert_alpha(),
    }
    obj_list[obj_name]['width'], obj_list[obj_name]['height'] = obj_list[obj_name]['image'].get_size()
    return obj_list


def display_object(surface, obj_name, obj_list):
    surface.blit(obj_list[obj_name]['image'], (obj_list[obj_name]['x'], obj_list[obj_name]['y']))


def add_function(obj_name, obj_list, function_name):
    obj_list[obj_name][function_name] = True
