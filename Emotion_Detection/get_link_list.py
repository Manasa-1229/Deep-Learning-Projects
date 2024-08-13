def lists(path):
    import os
    import pickle
    import warnings
    warnings.filterwarnings('ignore')
    #define the path of folder containing videos
    #path = "C:/Users/manas_nmr2rze/Desktop/Capstone/"+folder 
    #assign the object names to a list
    file_list=os.listdir(path)
    import re
    img_list = []
    for string in file_list:
        m = re.search("^.*jpg$", string)
        if m:
            img_list.append(string)
    link_list=[]
    for name in img_list:
        name = path +"/"+ name
        link_list.append(name)
    return link_list, img_list


def folders(path):
    import os
    import pickle
    import warnings
    warnings.filterwarnings('ignore')
    #define the path of folder containing videos
    #path = "C:/Users/manas_nmr2rze/Desktop/Capstone/"+folder 
    #assign the object names to a list
    file_list=os.listdir(path)
    link_list=[]
    for name in file_list:
        name = path +"/"+ name
        link_list.append(name)
    return link_list, file_list


def textlists(path):
    import os
    import pickle
    import warnings
    warnings.filterwarnings('ignore')
    #define the path of folder containing videos
    #path = "C:/Users/manas_nmr2rze/Desktop/Capstone/"+folder 
    #assign the object names to a list
    file_list=os.listdir(path)
    import re
    img_list = []
    for string in file_list:
        m = re.search("^.*txt$", string)
        if m:
            img_list.append(string)
    link_list=[]
    for name in img_list:
        name = path +"/"+ name
        link_list.append(name)
    return link_list, img_list