from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    # 获取 GET 请求中的 "password" 参数
    password = request.GET.get('password', None)

    # 预期的密码值
    expected_password = 'your_expected_password'

    if password == expected_password:
        # 如果密码匹配，重定向到登录页面
        return redirect('login')
    else:
        # 如果密码不匹配，返回错误响应
        return HttpResponse('Invalid password')
