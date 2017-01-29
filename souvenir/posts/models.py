from django.db import models
from address.models import District, Country, User_Address
from accounts.models import MyProfile


# # 设置 post 图片的保存路径

def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'post_images/user_{0}/{1}'.format(instance.user.id,filename)


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
	post_title = models.CharField(max_length=200,
		null =False,
		verbose_name ='发片令标题')
	post_description = models.TextField(verbose_name ='描述')

	# the quantity of postcards the sender prepared 
	post_quantity = models.PositiveIntegerField(null=False,
		verbose_name ='发片数量')

	# the number of cards left after a card is claimed
	card_left = models.IntegerField(default=0,
		verbose_name ='待领取')
	
	# picture
	post_picture = models.ImageField(null=False,
		blank = False,
		upload_to=post_directory_path,
		verbose_name ='上传一张图片'
	)

	# sent from
	post_country = models.ForeignKey(Country,
		verbose_name ='寄片的国家与地区')
	post_province = models.ForeignKey(District, 
		related_name='province',
		verbose_name ='寄片的省')
	post_city = models.ForeignKey(District,
		related_name='city',
		verbose_name ='寄片的城市')
	post_district = models.ForeignKey(District, 
		related_name='district',
		verbose_name ='寄片的区县')

	# user who creates the post 
	user = models.ForeignKey(MyProfile)

	def __str__(self):
		return self.post_title 

class CardClaim(TimeStampedModel):
	
	post = models.ForeignKey(Post)
	claimer = models.ForeignKey(MyProfile)

	# address
	claimer_address = models.ForeignKey(User_Address, 
		null = True)

	is_sent = models.BooleanField(default=False)
	is_received = models.BooleanField(default=False)


