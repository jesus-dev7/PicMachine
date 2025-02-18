from Serveur import img_get

def test_type_image():
    
    img = img_get()
    
    assert type(img) == "jpeg"