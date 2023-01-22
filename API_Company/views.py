#from django.shortcuts import render

from django.views import View
# Create your views here.

from .models import company

from django.http import JsonResponse

#from django.forms import model_to_dict

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

class companyListView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        #get
        # if('name' in request.GET):
        #     companylist = list(company.objects.filter(name__contains=request.GET['name']).values())
        #     datos = {'message': "Success", 'companies': companylist}
        #     return JsonResponse(datos, safe=False)
        # else:
           # companylist = company.objects.all()
           # return JsonResponse(list(companylist.values()), safe=False)
        if (id > 0):
            company2 = list(company.objects.filter(id=id).values())
            if len(company2) > 0:
                datos = {'message': "Success", 'company': company2[0]}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else:
            companylist = list(company.objects.all().values())
            if len(companylist) > 0 :
                datos = {'message': "Success", 'companies': companylist}
            else:
                datos = {'message': "Companies not found..."}    
            return JsonResponse(datos, safe=False)

    def post(self, request):
    #     #post
        #print(request.body)
        jd = json.loads(request.body)
        print(jd)
        company.objects.create(name=jd['name'], phone=jd['phone'], email=jd['email'], website=jd['website'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
    #     #put    
        jd = json.loads(request.body)
        print(jd)
        company2 = list(company.objects.filter(id=id).values())
        if len(company2) > 0:
            company3 = company.objects.get(id=id)
            company3.name = jd['name']
            company3.phone = jd['phone']
            company3.email = jd['email']
            company3.website = jd['website']
            company3.save()
            datos = {'message': "Success"}
        else:
             datos = {'message': "Company not found..."}

        return JsonResponse(datos)



    def delete(self, request, id):
    #     #delete
        company2 = list(company.objects.filter(id=id).values())
        if len(company2) > 0:
            company.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
             datos = {'message': "Company not found..."}

        return JsonResponse(datos)

