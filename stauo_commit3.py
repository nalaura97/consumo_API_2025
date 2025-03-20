pythonCopiarEditarclass API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'    @propertydef URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('name'), data.get('films'))
        except requests.RequestException as e:
            print(f"Erro ao acessar API Star Wars: {e}")
            return None 