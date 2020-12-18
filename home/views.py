from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("helo")


def vessel(request):
    return JsonResponse([
        {
            "id": "uuid2",
            "name": "Vessel 2",
            "isApproved": True,
            "psaNumber": "psanumber12"
        }, {
            "id": "uuid1",
            "name": "Vessel 1",
            "isApproved": True,
            "psaNumber": "psanumber1"
        }
    ], safe=False)


def mor(request):
    return JsonResponse([
        {
            "id": "uuid123123213",
            "name": "MOR One"
        }, {
            "id": "duauuid123123",
            "name": "MOR Two"
        }
    ], safe=False)


def terminal(request):
    return JsonResponse([
        {
            "id": "UUID123",
            "name": "TERMINAL One",
            "restStartTime": "19:00:00",
            "restEndTime": "22:00:00",
            "bbmQuantity": 30,
            "morId": "duauuid123123"
        },
        {
            "id": "UUID1234",
            "name": "TERMINAL Two",
            "restStartTime": "01:00:00",
            "restEndTime": "05:00:00",
            "bbmQuantity": 40,
            "morId": "duauuid123123"
        },
        {
            "id": "UUID12345",
            "name": "TERMINAL Three",
            "restStartTime": "10:00:00",
            "restEndTime": "12:00:00",
            "bbmQuantity": 600,
            "morId": "uuid123123213"
        },
        {
            "id": "UUID123457",
            "name": "TERMINAL Four",
            "restStartTime": "13:00:00",
            "restEndTime": "16:00:00",
            "bbmQuantity": 700,
            "morId": "uuid123123213"
        }

    ], safe=False)


def profile(request):
    return JsonResponse(
        {
            "terminalId": "uuid1",
            "email": "email@mail.com",
            "isApproved": True,
            "companyName": "companyName1",
            "companyAddress": "address1",
            "companyPhone": "081234567891",
            "type": "customer"
        },
        safe=False)


def schedule(request):
    if request.GET.get('date', '') != '' and request.GET.get('slot', '') != '':
        return JsonResponse([
            "00:00:00",
            "01:00:00",
            "02:00:00",
            "03:00:00",
            "04:00:00",
            "05:00:00",
            "06:00:00",
            "11:00:00",
            "12:00:00",
            "13:00:00",
            "14:00:00",
            "15:00:00",
            "16:00:00",
            "17:00:00",
            "18:00:00",
            "23:00:00"
        ],
            safe=False)

    elif request.GET.get('date', '') != '' and request.GET.get('slot', '') == '':
        print(request.GET)
        return JsonResponse([
            {
                "id": "a3acff4c-b461-4e3c-9431-8c324d569c8e",
                "status": "Approved",
                "date": "2020-12-16",
                "startTime": "15:00:00",
                "endTime": "17:00:00",
                "quantity": 200,
                "loNumber": "string"
            }, {
                "id": "a3acff4c-abc-4e3c-9431-8c324d569c8e",
                "status": "Processed",
                "date": "2020-12-16",
                "startTime": "05:00:00",
                "endTime": "11:00:00",
                "quantity": 400,
                "loNumber": "string"
            },
            {
                "id": "a3acff4c-def-4e3c-9431-8c324d569c8e",
                "status": "Approved",
                "date": "2020-12-16",
                "startTime": "20:00:00",
                "endTime": "22:00:00",
                "quantity": 300,
                "loNumber": "string"
            }
        ],
            safe=False)
    else:
        return JsonResponse({'message': 'invalid'})


def jetty(request):
    return JsonResponse(
        [{
            "id": "7b385f64-5717-4562-b3fc-2c963f66afa6",
            "name": "jettyName",
            "busyStartTime": "00:00:00",
            "busyEndTime": "02:00:00",
            "terminalId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }, {
            "id": "7b385f64-5717-4562-b3fc-aaaaaacobaaa",
            "name": "jettyName TWO",
            "busyStartTime": "10:00:00",
            "busyEndTime": "13:00:00",
            "terminalId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }],
        safe=False)


def product(request):
    return JsonResponse(
        [{
            "id": "uuid1",
            "name": "Bensin",
            "quantity": 100,
            "flowrate": 20
        },
            {
                "id": "uuid12",
                "name": "Solar",
                "quantity": 300,
                "flowrate": 30
            }
        ],
        safe=False)
