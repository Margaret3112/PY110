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
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        else:

            products = [product.get("name") for product in DATABASE]
            return JsonResponse(products, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})

