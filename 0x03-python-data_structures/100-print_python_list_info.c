#include "pylist.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		const char *elementType = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, elementType);
	}
}
