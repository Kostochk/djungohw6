from django.shortcuts import render

def greeting_view(request):
    message = ""
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        message = f"Доброго дня, {first_name} {last_name}!"
    return render(request, 'greeting.html', {'message': message})

def prime_numbers_view(request):
    primes = []
    if request.method == "POST":
        start = int(request.POST.get("start", 0))
        end = int(request.POST.get("end", 0))
        
        for num in range(max(2, start), end + 1):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
                
    return render(request, 'primes.html', {'primes': primes})

def prime_numbers_view(request):
    primes = []
    if request.method == "POST":
        start = int(request.POST.get("start", 0))
        end = int(request.POST.get("end", 0))
        
        for num in range(max(2, start), end + 1):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
                
    return render(request, 'primes.html', {'primes': primes})

def mult_table_range_view(request):
    results = None
    if request.method == "POST":
        start = int(request.POST.get("start", 1))
        end = int(request.POST.get("end", 10))
        results = {
            'range': range(start, end + 1),
            'nums': range(1, 11)
        }
    return render(request, 'mult_table.html', results)

def subscribe_view(request):
    user_data = None
    if request.method == "POST":
        user_data = {
            'first_name': request.POST.get("first_name"),
            'last_name': request.POST.get("last_name"),
            'age': request.POST.get("age"),
            'gender': request.POST.get("gender"),
            'email': request.POST.get("email"),
        }
    return render(request, 'subscribe.html', {'user': user_data})