from django.contrib import admin
from .models import CustomUser, OTP, Note

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fullname', 'is_verified', 'is_premium', 'is_staff')
    list_filter = ('is_verified', 'is_premium', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'fullname')

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'otp')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')
