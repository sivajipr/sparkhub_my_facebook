from django import template
from generic.models import Like 
register = template.Library()
@register.filter(name='actioncounts')
def actioncounts(post,user):
	return Like.objects.filter(user=user, post=post).exists()

@register.filter(name='actioncountseve')
def actioncountseve(event,user):
	return Like.objects.filter(user=user, event=event).exists()
