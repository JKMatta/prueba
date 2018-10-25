from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):

  def test_postPublish1( self ):
	#Arrange
	expected=2
	result=1
	x = Post.objects.get(title="test")
	Post.objects.create(author="javier",title="test")
	#act
	if x == "test":
		result=2
	
	#assert
	self.assertAreEqual(expected,result)
