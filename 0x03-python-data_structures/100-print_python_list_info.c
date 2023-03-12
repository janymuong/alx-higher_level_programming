#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print some basic info:
 * about Python lists
 *
 * @p: pointer to a PyObject list object - reference count
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{

	Py_ssize_t m_alloc, size, obj_index;
	PyObject *obj;

	size = PyList_Size(p);
	m_alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", m_alloc);

	for (obj_index = 0; obj_index < size; obj_index++)
	{
		obj = PyList_GetItem(p, obj_index);
		printf("Element %ld: %s\n", obj_index, Py_TYPE(obj)->tp_name);
	}
}
