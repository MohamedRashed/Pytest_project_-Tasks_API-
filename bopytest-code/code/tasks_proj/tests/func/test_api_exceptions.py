import pytest
import tasks

def test_add_raises():
	"""add() should raise an exception with wrong type parameter"""
	with pytest.raises(TypeError):
		tasks.add(task='not a Task object')

def test_start_tasks_db_raises():
	"""Make sure unsupported db raises an exception"""
	with pytest.raises(ValueError) as excinfo:
		tasks.start_tasks_db('some/great/path', 'mysql')
	exception_msg = excinfo.value.args[0]
	assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

@pytest.mark.smoke
def test_list_raises():
	"""List_tasks() should raise an exception with wrong type parameter"""
	with pytest.raises(TypeError):
		tasks.list_tasks(owner=123)

@pytest.mark.smoke
@pytest.mark.get 
def test_get_raises():
	"""get() should raise an exception with wrong type parameter"""
	with pytest.raises(TypeError):
		tasks.get(task_id='123')

