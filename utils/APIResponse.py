from rest_framework.response import Response
from http.client import responses as HTTPStatus



def APIResponse(data=None, notification=None, *args, **kwargs):
    response = {
        'notification': {}
    }
    if (notification is not None) and len(notification) == 2:
        response['notification'] = {
            'type': notification[0],
            'message': notification[1]
        }
    if data is None:
        response['data'] = []
    else:
        response['data'] = data
    resp = Response(response, *args, **kwargs)
    resp.data['status'] = resp.status_code
    resp.data['status_type'] = HTTPStatus[resp.status_code]
    return resp


def DepartmentAPIResponse(department_list=None, notification=None, *args, **kwargs):
    response = {
        'notification': {}
    }
    if (notification is not None) and len(notification) == 2:
        response['notification'] = {
            'type': notification[0],
            'message': notification[1]
        }
    if department_list is None:
        response['department_list'] = []
    else:
        response['department_list'] = department_list
    resp = Response(response, *args, **kwargs)
    resp.data['status'] = resp.status_code
    resp.data['status_type'] = HTTPStatus[resp.status_code]
    return resp


def UnitAPIResponse(unit_list=None, notification=None, *args, **kwargs):
    response = {
        'notification': {}
    }
    if (notification is not None) and len(notification) == 2:
        response['notification'] = {
            'type': notification[0],
            'message': notification[1]
        }
    if unit_list is None:
        response['unit_list'] = []
    else:
        response['unit_list'] = unit_list
    resp = Response(response, *args, **kwargs)
    resp.data['status'] = resp.status_code
    resp.data['status_type'] = HTTPStatus[resp.status_code]
    return resp


def AssigneAPIResponse(assign_list=None, notification=None, *args, **kwargs):
    response = {
        'notification': {}
    }
    if (notification is not None) and len(notification) == 2:
        response['notification'] = {
            'type': notification[0],
            'message': notification[1]
        }
    if assign_list is None:
        response['assign_list'] = []
    else:
        response['assign_list'] = assign_list
    resp = Response(response, *args, **kwargs)
    resp.data['status'] = resp.status_code
    resp.data['status_type'] = HTTPStatus[resp.status_code]
    return resp
