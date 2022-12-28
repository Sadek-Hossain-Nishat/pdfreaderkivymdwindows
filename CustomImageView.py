import os


import fitz
import shutil


class CustomImageView:
    img_object_li = []


    def __init__(self, pdf_location=''):
        self.img_object_li.clear()
        open_pdf = fitz.Document(pdf_location)
        f= open('G:/pythonprojects/kivyandkivymdprojects/PdfReaderApplicationinKivymd/cach_file.txt','r')

        cach_path = f.read()
        f.close()
        if cach_path!='':
            shutil.rmtree(cach_path)

        count = 0
        print(f'page count {open_pdf.page_count}\n'
              f'type {type(open_pdf.page_count)}')


        pdf_location_list = pdf_location.split('\\')
        pdf_file_name = pdf_location_list[len(pdf_location_list)-1]
        print(pdf_file_name)
        pdf_file_name_list = pdf_file_name.split('.')
        print(pdf_file_name_list)
        pdf_file_images_folder_name = pdf_file_name_list[0]+"_images"
        print(pdf_file_images_folder_name)
        # os.remove(cach_folder_path)

        image_folder_path='G:/pythonprojects/kivyandkivymdprojects/PdfReaderApplicationinKivymd/'+pdf_file_images_folder_name
        f= open('G:/pythonprojects/kivyandkivymdprojects/PdfReaderApplicationinKivymd/cach_file.txt','w')
        f.write(image_folder_path)
        f.close()

        # cach_folder_path = image_folder_path

        is_exists_dir=os.path.exists(image_folder_path)
        if is_exists_dir==False:


            os.mkdir(image_folder_path)

        for page in range(open_pdf.page_count):
            page = open_pdf.load_page(page)
            pix = page.get_pixmap()
            pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix

            # p=pix1.tobytes('png')




            pix1.save(image_folder_path+"/page-%i.png" % page.number)



            # self.img_object_li.append(p)

            # pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
            # img = pix1.tobytes()
            # timg = PhotoImage(data=img)

            # img = '{}.png'.format(pix)
            # count += 1
            # self.img_object_li.append(img)
            # print(f'{img}\n type {type(img)}')
        entirs = os.listdir(image_folder_path)
        for entry in entirs:
            imageUrl =f'{image_folder_path}/{entry}'
            self.img_object_li.append(imageUrl)


        print(entirs)
        print(type(entirs))