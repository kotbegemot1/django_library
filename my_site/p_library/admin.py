from django.contrib import admin
from p_library.models import Book, Author, Redaction, Friend, Rent, Publisher, UserProfile

# Register your models here.
@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

	@staticmethod
	def author_full_name(obj):
		return obj.author.full_name

	list_display = ('title', 'author_full_name')
	fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'cover', 'redact', 'publisher' )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass    

@admin.register(Redaction)
class RedactorAdmin(admin.ModelAdmin):
	pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	pass

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
	pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	pass