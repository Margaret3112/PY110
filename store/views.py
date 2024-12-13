from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_view(request):
    if request.method == "GET":
        id_num = request.GET.get("id")
        if id_num:
            data = DATABASE.get(id_num)
            if data:
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})
            else:
                return HttpResponseNotFound("Данного продукта нет в базе данных")
        else:
            return JsonResponse([DATABASE[key]['name'] for key in DATABASE], safe=False, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})

def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{page}.html', 'r', encoding="utf-8") as f:
                        return HttpResponse(f.readlines())
        elif isinstance(page, int):
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:
                with  open(f'store/products/{data["html"]}.html', 'r', encoding="utf-8") as f:
                    return HttpResponse(f.readlines())
        return HttpResponse(status=404)