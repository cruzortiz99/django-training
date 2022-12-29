from django.contrib import admin
import domain.models as models

# Register your models here.
admin.site.register([
    models.AdoptionCenter,
    models.AdoptionOrder,
    models.PostComment,
    models.Pet,
    models.PetStore,
    models.PetStorePurchaseOrder,
    models.Post,
    models.PostReaction,
    models.User
])
