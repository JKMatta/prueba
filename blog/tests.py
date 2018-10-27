from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):

  def test_equal( self ):
	#Arrange
	expected=2
	result=2
	#act

	#assert
	self.assertAreEqual(expected,result)
