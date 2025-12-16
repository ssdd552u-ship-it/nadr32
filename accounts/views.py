from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # التحقق من كلمات المرور
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("accounts:register")

        # التحقق من وجود اسم المستخدم
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا")
            return redirect("accounts:register")

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            is_customer=True
        )

        # تسجيل الدخول مباشرة بعد التسجيل
        login(request, user)
        messages.success(request, "تم إنشاء الحساب بنجاح")
        return redirect("/")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect("/")
        else:
            messages.error(request, "بيانات الدخول غير صحيحة")
            return redirect("accounts:login")

    return render(request, "accounts/login.html")


@require_POST
def logout_view(request):
    """
    تسجيل خروج آمن (POST فقط)
    """
    logout(request)
    messages.success(request, "تم تسجيل الخروج بنجاح")
    return redirect("/")
