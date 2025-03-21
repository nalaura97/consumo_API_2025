pythonCopiarEditarclass API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'    @propertydef URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('id'), data.get('name'), data.get('species'))
        except requests.RequestException as e:
            print(f"Erro ao acessar API Rick and Morty: {e}")
            return None 
