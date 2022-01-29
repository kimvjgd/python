files1 = ['1-asdas12d.JPG',         # 중간중간 대문자도 있다.
         '1-asdas214d.jpeg',
         '1-asda745sd.jpg',
         '1-asdas5434d.jpeg',
         '1-asda31232sd.mp3',
         '1-asdas12d.jpg',
         '1-asdas214d.jpeg',
         '1-asda745sd.JPG',
         '1-asdas5434d.MP3',
         '1-asda31232sd.png',
         '1-asdas12d.jpg',
         '1-asdas214d.jpeg',
         '1-asda745sd.jpg',
         '1-asdas5434d.jpeg',
         '1-asda31232sd.png',]
files2 = ['2-asdas12d.jpg',
         '2-asdas214d.jpeg',
         '2-asda745sd.jpg',
         '2-asdas5434d.jpeg',
         '2-asda31232sd.mp3',
         '2-asdas12d.jpg',
         '2-asdas214d.jpeg',
         '2-asda745sd.jpg',
         '2-asdas5434d.MP3',
         '2-asda31232sd.png',
         '2-asdas12d.jpg',
         '2-asdas214d.jpeg',
         '2-asda745sd.jpg',
         '2-asdas5434d.jpeg',
         '2-asda31232sd.png',]

def printByExt(file_list, ext):
    for file in file_list:
        if file.lower().endswith(ext):
            print(file)
    
    print('-'*50)


def main():
    printByExt(files1, 'jpg')
    printByExt(files2, 'jpeg')
    printByExt(files1, 'mp3')

main()