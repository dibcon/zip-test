from io import BytesIO, StringIO
import zipfile
import json


def generate_zip_stream(input_string):
    # bin_stream = content.encode(encoding="utf-8")
    mem_zip = BytesIO()
    a_bytes = bytes(input_string, "utf-8")

    binary_stream =  BytesIO(a_bytes)
    # binary_stream =  BytesIO(b'I am a byte string \x01')

    # print(binary_stream.getValue())

    with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("xyz", input_string)


    return mem_zip.getvalue()

def generate_json():
    with open('vehicle.json', 'r', encoding='utf-8') as f:
        # data = (line.strip() for line in f) #Erzeugt Generator Objekt
        content = f.read()
    return (content)
	
def main():
    json_struct=generate_json()
    print(json_struct)

    xbinary_stream =  BytesIO(bytes(json_struct, "utf-8"))   ##(b'I am a byte string \x01')
    print(xbinary_stream.getvalue()) # Prints b'I am a byte string \x01'

    bin_stream=generate_zip_stream(json_struct)
    print(bin_stream)

    file = open("sample.zip", "wb")

    file.write(bin_stream)

    file.close()

if __name__ == "__main__":
    main()
