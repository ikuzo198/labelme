import json, os, glob

data_path:str = "datasets/rc23/Table"

json_list = glob.glob(f"{data_path}/*.json")

width = 640
height = 480

labels = {'cheez-it_cracker_box': 0, 'domino_sugar_box': 1, 'jell-o_chocolate_pudding_box': 2, \
        'jell-o_strawberry_gelatin_box': 3, 'spam_potted_meat_can': 4, 'master_chef_coffee_can': 5, \
        'starkist_tuna_fish_can': 6, 'pringles_chips_can': 7, 'frenchs_mustard_bottle': 8, \
        'tomato_soup_can': 9, 'plastic_banana': 10, 'plastic_strawberry': 11, 'plastic_apple': 12, \
        'plastic_lemon': 13, 'plastic_peach': 14, 'plastic_pear': 15, 'plastic_orange': 16, \
        'plastic_plum': 17, 'windex_spray_bottle': 18, 'scrub_cleanser_bottle': 19, \
        'scotch_brite_dobie_sponge': 20, 'pitcher_base': 21, 'pitcher_lid': 22, 'plate': 23, \
        'bowl': 24, 'fork': 25, 'spoon': 26, 'spatula': 27, 'wine_glass': 28, 'mug': 29, 'large_marker': 30, \
        'key': 31, 'bolt_and_nut': 32, 'clamp': 33, 'credit_card': 34, 'soccer_ball': 35, 'soft_ball': 36, \
        'baseball': 37, 'tennis_ball': 38, 'racquetball': 39, 'golf_ball': 40, 'marbles': 41, 'cups': 42, \
        'foam_brick': 43, 'dice': 44, 'rope': 45, 'chain': 46, 'rubiks_cube': 47, 'colored_wood_blocks': 48, \
        '9-peg-hole_test': 49, 'toy_airplane': 50, 'lego_duplo': 51, 'magazine': 52, 't-shirt': 53, 'timer': 54, 'boss': 55}

# def process_json_files(folder, width, height):
#     for root, dirs, files in os.walk(folder):
#         for file in files:
#             if file.endswith('.json'):
#                 json_file = os.path.join(root, file)
#                 output_file = os.path.join(root, os.path.splitext(file)[0] + '.txt')
#                 json2yolo_seg(json_file, output_file, width, height)
#                 print(f"Processed: {json_file} -> {output_file}")



def json2yolo_seg(json_list, width, height):
    for json_data in json_list:
        with open(json_data, 'r') as f:
            print(json_data)
            raw_data = json.load(f)
            output_file = os.path.splitext(json_data)[0] + '.txt'

        with open(output_file, 'w') as o:
            for id in range(len(raw_data["shapes"])):
                label = labels[raw_data["shapes"][id]["label"]]
                class_wise_point = []
                xy = []

                for point in raw_data["shapes"][id]["points"]:
                    x, y = point
                    x = x / width
                    y = y / height
                    xy.append(x)
                    xy.append(y)

                class_wise_point = str(xy)[1:-1]
                class_wise_point = class_wise_point.replace(",","")
                o.write(f"{label} {class_wise_point}\n")



json2yolo_seg(json_list, width, height)
print("FIN")