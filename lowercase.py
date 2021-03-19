import os

'''This function lower cases any text based files it will not traverse multiple file paths or other file types!'''


def lower_cased():
    print('YOU ARE NOW CONVERTING EVERYTHING COLLECTED TO LOWERCASE')
    path = r'./collected'
    for file in os.listdir(path):
        print(file)
        x = (os.path.join(path, file))
        with open(x, 'r+b') as f:
            reading = f.read()
            f.seek(0)
            f.write(reading.lower())

if __name__ == "__main__":
    lower_cased()
