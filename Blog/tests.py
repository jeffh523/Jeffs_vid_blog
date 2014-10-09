from django.test import TestCase
from Blog.models import Post
from django.utils import timezone
from Blog.templatetags.Blog_extras import convert_youtube_to_embed

class BlogTests(TestCase):

	def setup(self):
		self.post1 = Post(title="post1 title") 

	def test_creating_posts(self):
		self.assertEqual("post1 title", self.post1.title)
		self.assertEqual('', self.post1.content)
		self.assertEqual('', self.post1.videoURL)
		#no time argument was given for post1 so dateCreated=None
		self.assertEqual(None, self.post1.dateCreated)
		
		post2_creation_time = timezone.now()
		post2 = Post(title="post2 title", content="blah", 
			videoURL="http://www.youtube.com/watch?v=vTIsuCSFuj8",
				dateCreated=post2_creation_time)
		self.assertEqual("post2 title", post2.title)
		self.assertEqual("blah", post2.content)
		self.assertEqual("http://www.youtube.com/watch?v=vTIsuCSFuj8", post2.videoURL)
		self.assertEqual(post2_creation_time, post2.dateCreated)

	def test_convert_youtube_to_embed_validURL(self):
		post3 = Post(title="post3 title", content="somecontent", 
			videoURL="http://www.youtube.com/watch?v=0EEfjUGc1Io")
		post3_embed = convert_youtube_to_embed(post3.videoURL)
		self.assertEqual('<iframe width="560" height="315" src="//www.youtube.com/embed/0EEfjUGc1Io" frameborder="0" allowfullscreen></iframe>',
			post3_embed)
			
	def test_convert_youtube_to_embed_noURL(self):
		self.assertEqual('', convert_youtube_to_embed(self.post1.videoURL))
		
	def test_convert_youtube_to_embed_invalidURL(self):
		invalid_URL1 = "dsfwtj"
		invalid_URL2 = "www.facebook.com"
		invalid_URL3 = "www.youtube.com"
		
		post4 = Post(title="post4 title", videoURL=invalid_URL1)
		self.assertEqual('', convert_youtube_to_embed(post4.videoURL))
		
		post5 = Post(title="post5 title", videoURL=invalid_URL2)
		self.assertEqual('', convert_youtube_to_embed(post5.videoURL))
		
		post6 = Post(title="post6 title", videoURL=invalid_URL3)
		self.assertEqual('', convert_youtube_to_embed(post6.videoURL))
		
		