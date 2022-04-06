import requests as rq # take files from urls
import json # read Json files

# url_velo = "http://opendata.nicecotedazur.org/data/storage/f/2014-05-13T08%3A22%3A17.827Z/velobleu.json"
  
def find_coord(url : str) -> list[list[float]]:
    """
    Returns the list of the coordinate pair from an url.
    The data must be in a json format.
    The coordinate pair must be stocked under the "coordinates" key.
    """
    
    response = rq.get(url)    
    jsonresponse = response.json()
    
    coord_list = []
    
    for part in jsonresponse["docs"]:
        for key, value in part.items():
            if type(value) == dict:
                coord_list.append(value["coordinates"])
    
    return coord_list