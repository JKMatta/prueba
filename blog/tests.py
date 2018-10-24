from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):
  def test_postPublish1( self ):
	#Arrange
	expected=2
	result=1
	#act
	result=2
	#assert
	self.assertAreEqual(expected,result)

  def test_postPublish2( self ):
	#Arrange
	expected=2
	result=1
	#act
	result=2
	#assert
	self.assertAreEqual(expected,result)

  def test_postPublish3( TestCase ):
	#Arrange
	expected=2
	result=1
	#act
	result=2
	#assert
	self.assertAreEqual(expected,result)
