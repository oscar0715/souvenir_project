from django.db import models
from address.models import District, Country
from accounts.models import MyProfile


# 设置 post 图片的保存路径
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'post_image/user_{0}/{1}'.format(instance.user.id,filename)


# Create your models here.
class TimeStampedModel(models.Model):
	"""
	abstract base class, 提供创建时间和修改时间两个通用的field
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Post(TimeStampedModel):
	# basic
	post_title = models.CharField(max_length=200,null =False)
	post_description = models.TextField()

	# the quantity of postcards the sender prepared 
	post_quantity = models.PositiveIntegerField(null=False)

	# the number of cards left after a card is claimed
	card_left = models.IntegerField(default=0)
	
	# picture
	post_picture = models.ImageField(null=True,blank = True,upload_to=user_directory_path);

	# sent from
	post_country = models.ForeignKey(Country)
	post_province = models.ForeignKey(District, related_name='province')
	post_city = models.ForeignKey(District, related_name='city')
	post_district = models.ForeignKey(District, related_name='district')

	# user who creates the post 
	user = models.ForeignKey(MyProfile)

	def __str__(self):
		return self.post_title 
