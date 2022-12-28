import os



os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from CustomImageView import CustomImageView

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.recycleview import MDRecycleView
from kivy.uix.image import Image








KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "MDFileManager"
        left_action_items: [["menu", lambda x: None]]
        elevation: 3
    MDFloatLayout:
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.file_manager_open()
            
    
    RecyclerViewPython:
        id:rv
        viewclass: 'MyImage'  # defines the viewtype for the data items.
        
       
      
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
    
'''


class RecyclerViewPython(MDRecycleView):


    def __init__(self,  **kwargs):
        super(RecyclerViewPython, self).__init__(**kwargs)


        self.data = [{'source': str(x)} for x in []]



class MyImage(Image):
    """

    """




class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)




    def file_manager_open(self):
        from plyer import filechooser


        try:
            path = filechooser.open_file()[0]
            paisi = CustomImageView(path)
            print(paisi.img_object_li)
            # RecyclerViewPython().data.append() = [{'source': str(x)} for x in paisi.img_object_li]
            # toast(path)

            if paisi.img_object_li!=None:
                self.root.ids.rv.data = [{'source': str(x)} for x in []]
                print('data is exists')
                self.root.ids.rv.data=[{'source': str(x)} for x in paisi.img_object_li]
        except Exception as e:
            toast('No file is selected')
            print(f'{e}')


Example().run()
