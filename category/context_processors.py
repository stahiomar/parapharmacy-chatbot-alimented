from category.models import Category
def categories_menu(request):
  categories = Category.objects.all()
  context = {
    'categories': categories
  }
  return context