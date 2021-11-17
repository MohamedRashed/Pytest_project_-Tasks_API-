"""Test the Task Data Type"""

from collections import namedtuple
fields = ('summary', 'owner', 'done', 'id' )
Task = namedtuple('Task', fields, defaults=(None, None, False, None))

def test_defaults():
	t1 = Task()
	t2 = Task(None, None, False, None)

	assert t1 == t2

def test_member_access():
	"""Check .field functionality of namedtuple."""
	t = Task('buy milk', 'brian')
	assert t.summary == 'buy milk'
	assert t.owner == 'brian'
	assert (t.done, t.id) == (False, None)