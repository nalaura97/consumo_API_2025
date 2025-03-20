pythonCopiarEditarclass API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'    @propertydef URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('name'), data.get('tvSeries'))
        except requests.RequestException as e:
            print(f"Erro ao acessar API Crônicas do Gelo e do Fogo: {e}")
            return None 