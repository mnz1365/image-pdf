from PIL import Image

# add image or list of image here...
mysrc = ["car1.jpg", "car2.jpg", "house1.jpeg", "house2.jpg", "tree1.jpg", "tree2.jpg"]

def imgPdf(src):
    
    try:
        images = [
        Image.open("src/" + f)
        for f in src
        ]

        pdf_path = "mypdf.pdf"


        images[0].save(
            pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
        )

        print("pdf created!")
        
    except Exception as e:
        print("the error is: ",e)


imgPdf(mysrc)