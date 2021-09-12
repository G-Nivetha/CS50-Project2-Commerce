from django.contrib import admin
from .models import User, Listing, Bid,Comment,Watchlist,Closedbid,Alllisting

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "category","price")

class BidAdmin(admin.ModelAdmin):
    list_display = ("listingid","title", "user", "bid" )

class CommentAdmin(admin.ModelAdmin):
    list_display = ("listingid", "user", "comment" )

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("listingid", "user" )

class ClosedbidAdmin(admin.ModelAdmin):
    list_display = ("listingid", "winner", "owner", "winprice" )

class AlllistingAdmin(admin.ModelAdmin):
    list_display = ("listingid", "title" )


# Register your models here.
admin.site.register(User)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Bid,BidAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Watchlist,WatchlistAdmin)
admin.site.register(Closedbid,ClosedbidAdmin)
admin.site.register(Alllisting,AlllistingAdmin)