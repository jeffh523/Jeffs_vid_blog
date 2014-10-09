from django import template
register = template.Library()


#converts a youtube video URL into iframe embed code for use in HTML
@register.filter(is_safe=True)
def convert_youtube_to_embed(url):
	if (url != '') and ("youtube.com/watch?v=" in url):
		video_id = url.split("=")[1]
		embed_code = '<iframe width="560" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % video_id
		return embed_code
	return ''
convert_youtube_to_embed.is_safe = True