import requests
class Cep:
    def __init__(self, address_type, address_name, address, state, district, lat, lng):
        self.address_type = address_type
        self.address_name = address_name
        self.address = address
        self.state = state
        self.district = district
        self.lat = lat
        self.lng = lng


link = requests.get('https://cep.awesomeapi.com.br/json/89066340')
pessoa = Cep(['adress'])
print(link.text)