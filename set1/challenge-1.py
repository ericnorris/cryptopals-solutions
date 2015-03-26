import base64

def hex_to_base64(hex_string):
    return base64.b64encode(base64.b16decode(hex_string, True))

if __name__ == '__main__':
    hex_string = raw_input("> ")
    print hex_to_base64(hex_string)
