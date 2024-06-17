

class InterfazApiBodegas:
    """
    # Diccionario estático de la clase que mapea nombres de bodegas a URLs de sus APIs
    API_URLS = {
        'Bodega1': 'https://api.example.com/vinos/bodega1',
        'Bodega2': 'https://api.example.com/vinos/bodega2',
        # Se pueden añadir más bodegas y sus URLs de API aquí
    }
    """
    # Como no implementamos las APIs de las bodegas, vamos a harcodear las respuestas de las APIs en un diccionario
    
    RESPONSES = {
        'Bodega San Javier': 'actualizacionesBodega1.json',
        'Bodega Altamira': 'actualizacionesBodega2.json',
        'Bodega3': 'actualizacionesBodega3.json',
    }
    @staticmethod
    def obtenerActualizacionVinos(nombre_bodega):
        """
        # Busca la URL de la API correspondiente al nombre de la bodega
        api_url = InterfazApiBodegas.API_URLS.get(nombre_bodega)
        
        # Si no se encuentra la URL, lanza una excepción
        if not api_url:
            raise ValueError(f"No se encontró la URL de la API para la bodega: {nombre_bodega}")
        
        # Realiza una solicitud GET a la URL de la API
        response = requests.get(api_url)
        
        # Si la respuesta es exitosa, retorna los datos en formato JSON
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
        """
        # Al estar los datos harcodeados, simulamos la respuesta de la API
        return InterfazApiBodegas.RESPONSES[nombre_bodega]


class InterfazNotificacionPush:
    
    def notificarEnofilo(enofilo):
        notificado = True
        #no implementado
        return notificado

    def notificarNovedadVinoParaBodega(seguidores):

        for seguidor in seguidores:
            InterfazNotificacionPush.notificarEnofilo(seguidor)

        return ('Los seguidores de esta bodega fueron notificados de las novedades con exito!')