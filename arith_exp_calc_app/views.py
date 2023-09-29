from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'arith_exp_calc.html')

@csrf_exempt
def calculate_expression(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
            response = str(result)
        except Exception as e:
            response = f"Error: {str(e)}"
        return render(request, 'arith_exp_calc.html', {'result': response, 'expression': expression})
    return render(request, 'arith_exp_calc.html')
