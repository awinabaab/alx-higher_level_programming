#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_list - Prints some basic info about Python Lists
 * @p: A pointer to a Python list
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	PyObject *list_item = NULL;
	PyListObject *list_object = (PyListObject *) p;
	const char *type = NULL;
	Py_ssize_t index = 0;

	if (PyList_Check(p))
	{
		size = list_object->ob_base.ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", list_object->allocated);

		for (index = 0; index < size; index++)
		{
			list_item = list_object->ob_item[index];
			type = list_item->ob_type->tp_name;
			printf("Element %zd: %s\n", index, type);
			if (PyBytes_Check(list_item))
				print_python_bytes(list_item);
		}
	}
}

/**
 * print_python_bytes - Prints the the bytes of a Python bytes object
 * @p: A pointer to a Python object
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_object = (PyBytesObject *) p;
	Py_ssize_t size = bytes_object->ob_base.ob_size;
	Py_ssize_t max_bytes_size = (size > 10 ? 10 : size + 1);
	Py_ssize_t index = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", bytes_object->ob_sval);
		printf("  first %zd bytes: ", max_bytes_size);

		for (index = 0; index < max_bytes_size; index++)
			printf("%02x ", bytes_object->ob_sval[index]);
		printf("\n");
	}
	else
		printf(" [ERROR] Invalid Bytes Object\n");
}
