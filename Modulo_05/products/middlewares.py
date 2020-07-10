def aceleradev_middleware(get_response):

    def middleware(request):
        if request.method == 'GET':
            print('Método da requisição é GET')

        print('Acelera Fabiano')
        response = get_response(request)
        print('Online na internet')
        return response

    return middleware