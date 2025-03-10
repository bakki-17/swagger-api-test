import pytest
from utils.APIClient import APICLIENT
# from config import brandEndpoint, cartEndpoint
from utils.dataGenerator import DataGenerator
import json
from json import loads


dataGen = DataGenerator()
brand_id = [] # this will store the ID of the created brand then used to verify the data
orginalRecordCount = []

@pytest.fixture
def api():
    return APICLIENT()

def test_get_all_brands(api: APICLIENT):
    response = api.getRequest('brand', endpoint_path='')
    # response = api.getRequest(brandEndpoint)
    assert response.status_code == 200
    existingDataCount = len(response.json())
    # print(existingDataCount)
    # return orginalRecordCount.append(int(existingDataCount))
    return orginalRecordCount.append(existingDataCount)
    print (orginalRecordCount)
    # for i in range(existingDataCount):
    #     orginalRecordCount.append(list(i))
    #     print (orginalRecordCount)

    # return orginalRecordCount.append(existingDataCount)

# # Checking a brand by providing the ID
# def test_get_specific_brand(api: APICLIENT):
#     response = api.getRequest('brand', endpoint_path='/01jdrqaf06bhdf69bz78ecm2gf')
#     # response = api.getRequest(brandEndpoint)
#     assert response.status_code == 200
    
def test_post_new_brand(api: APICLIENT):
    generateNewBrand = dataGen.generate_new_brand()
    response = api.postRequest('brand', data=generateNewBrand)
    assert response.status_code == 201

    # ids =[]
    # resp = response.json()
    # ids.append(resp)
    # for data in resp(): # Iterate through the list of JSON objects
    #     for key, value in data.items(): # Display the key value pairs for each object
    #         print(key, ":", value)
    # print(ids)          
    resp1 = json.loads(response.text)
    assert resp1['name'], ['slug'] == generateNewBrand
    # assert resp1['slug'] == generateNewBrand

    jsonResp1 = json.dumps(resp1['id']).strip('"')
    jsonResp2 = json.dumps(resp1['name']).strip('"')
    jsonResp3 = json.dumps(resp1['slug']).strip('"')
    
    # print(resp1['id'], jsonResp1)
    assert jsonResp1 == resp1['id']
    assert jsonResp2 == resp1['name']
    assert jsonResp3 == resp1['slug'] 

    return brand_id.append(jsonResp1) #return the ID of the created brand
    
#dynamic checking of a brand record verification
def test_get_brand(api: APICLIENT):
    brandID = brand_id.pop()
    response = api.getRequest('brand', endpoint_path=f"/{brandID}")
    assert response.status_code == 200

    # resp = json.loads(response.text)
    # print(resp['id'])

def test_get_all_brands_rec(api: APICLIENT):
    count = orginalRecordCount.pop()
    response = api.getRequest('brand', endpoint_path='')
    
    assert  count <= len(response.json())
    assert  count + 1 == len(response.json())