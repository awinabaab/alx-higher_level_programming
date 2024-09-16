#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python Lists
 * @p: A pointer to a Python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	PyObject *list_item = NULL;
	PyListObject *list_object = (PyListObject *) p;
	const char *type = NULL;
	Py_ssize_t index = 0;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", list_object->allocated);

		for (index = 0; index < size; index++)
		{
			list_item = PyList_GetItem(p, index);
			type = Py_TYPE(list_item)->tp_name;
			printf("Element %zd: %s\n", index, type);
		}
	}
	else
		fprintf(stderr, "The PyObject p is not a Python List.\n");
}
