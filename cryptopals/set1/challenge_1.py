import base64

def hex_to_base64(hex_string):
    return base64.b64encode(base64.b16decode(hex_string, True))

def main(hex_string):
    return hex_to_base64(hex_string)
