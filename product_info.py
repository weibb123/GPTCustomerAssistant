import json
from product import *

# these are the allowed category in the product dot py file
category = """[{'category': 'Smartphones and Accessories'},
                {'category': 'Computers and Laptops'},
                {'category': 'Cameras and Camcorders'},
                {'category': 'Audio Equipment'}]
            """

category_list = read_string_to_list(category)
output_string = generate_output_string(category_list)
