import requests
import io
from PIL import Image
from requests.exceptions import HTTPError
from reportlab.pdfgen import canvas

# Creating empty PDF
c = canvas.Canvas("comic_pdf.pdf")
c.save()

n = 3000
url_path = 'https://xkcd.com/'
pdf_path = "/Users/akhileshvarmabhupathiraju/Documents/oh_project/week_1/comic_pdf.pdf"
resolution=100.0


def get_image_urls(n, url_path):
    img_list = []
    for i in range(1,n):
        try:
            if (i%500==0):
                print("Extracting comic no: ",i)
            x = requests.get(url_path + str(i), stream = True)
            image_url_split = x.text.split('Image URL ')[1]
            image_url_first_index = image_url_split.find("<a href= ")
            image_url_last_index = image_url_split.find(">")
            

        except HTTPError:
            print("Unable to get comic no: ", i,"due to HTTP error")

        except Exception as e:
            print("Unable to get comic no: ", i, "due to",e)

        else:
        
            image_url = image_url_split[image_url_first_index:image_url_last_index+1].replace('<a href= "','').replace('">','')
            img_list.append(image_url)

    return img_list
    



image_list = get_image_urls(n, url_path)
        
print("Total no of image urls extracted and to be present in the pdf: ",len(image_list))


def save_images_to_pdf(img_list, pdf_path, resolution=100.0):
    try:
        with Image.open(requests.get(img_list[0], stream=True).raw) as first_image:
            pdf_images = [first_image.convert('RGB')]

            for idx, f in enumerate(img_list[1:]):
                try:
                    img = Image.open(requests.get(f, stream=True).raw).convert('RGB')
                    pdf_images.append(img)
                except Exception as e:
                    print(f"Error downloading image '{f}' at index {idx}: {e}")

            if pdf_images:
                pdf_images[0].save(pdf_path, save_all=True, append_images=pdf_images[1:], dpi=(resolution, resolution))
                print("Done saving images to PDF")
            else:
                print("No images found to save to PDF")

    except Exception as e:
        print(f"An error occurred while saving images: {e}")


save_images_to_pdf(image_list, pdf_path, resolution)


