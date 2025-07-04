# coding: utf-8

"""
    DoorLoop API Reference

    It does some pretty cool stuff and gives you complete access to DoorLoop's data  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@doorloop.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_task(self, **kwargs):  # noqa: E501
        """Deletes a Task  # noqa: E501

        Deletes a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_task(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_task_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_task_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_task_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes a Task  # noqa: E501

        Deletes a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_task_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_task" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{taskId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task(self, **kwargs):  # noqa: E501
        """Retrieve a Task  # noqa: E501

        Retrieves a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_task_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_task_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_task_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a Task  # noqa: E501

        Retrieves a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{taskId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tasks(self, **kwargs):  # noqa: E501
        """Retrieve all Tasks  # noqa: E501

        Retrieves all Tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object filter_property_group: Filter by Portfolio Id
        :param object filter_property: Filter by Property Id
        :param object filter_unit: Filter by Unit Id
        :param object filter_type: Filter by Task Type
        :param object filter_status: Filter by Task Status
        :param object filter_created_at_from: Format: YYYY-MM-DD
        :param object filter_created_at_to: Format: YYYY-MM-DD
        :param object filter_due_date_from: Format: YYYY-MM-DD
        :param object filter_due_date_to: Format: YYYY-MM-DD
        :param object filter_completed_at_from: Format: YYYY-MM-DD
        :param object filter_completed_at_to: Format: YYYY-MM-DD
        :param object filter_assigned_to_user: Filter by User Id or \"unassigned\"
        :param object filter_text: Filter by Subject, Description or Reference
        :param object filter_requested_by_id: Filter by Requested by User, Tenant or Owner Id
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all Tasks  # noqa: E501

        Retrieves all Tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object filter_property_group: Filter by Portfolio Id
        :param object filter_property: Filter by Property Id
        :param object filter_unit: Filter by Unit Id
        :param object filter_type: Filter by Task Type
        :param object filter_status: Filter by Task Status
        :param object filter_created_at_from: Format: YYYY-MM-DD
        :param object filter_created_at_to: Format: YYYY-MM-DD
        :param object filter_due_date_from: Format: YYYY-MM-DD
        :param object filter_due_date_to: Format: YYYY-MM-DD
        :param object filter_completed_at_from: Format: YYYY-MM-DD
        :param object filter_completed_at_to: Format: YYYY-MM-DD
        :param object filter_assigned_to_user: Filter by User Id or \"unassigned\"
        :param object filter_text: Filter by Subject, Description or Reference
        :param object filter_requested_by_id: Filter by Requested by User, Tenant or Owner Id
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_property_group', 'filter_property', 'filter_unit', 'filter_type', 'filter_status', 'filter_created_at_from', 'filter_created_at_to', 'filter_due_date_from', 'filter_due_date_to', 'filter_completed_at_from', 'filter_completed_at_to', 'filter_assigned_to_user', 'filter_text', 'filter_requested_by_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_property_group' in params:
            query_params.append(('filter_propertyGroup', params['filter_property_group']))  # noqa: E501
        if 'filter_property' in params:
            query_params.append(('filter_property', params['filter_property']))  # noqa: E501
        if 'filter_unit' in params:
            query_params.append(('filter_unit', params['filter_unit']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'filter_status' in params:
            query_params.append(('filter_status', params['filter_status']))  # noqa: E501
        if 'filter_created_at_from' in params:
            query_params.append(('filter_createdAt_from', params['filter_created_at_from']))  # noqa: E501
        if 'filter_created_at_to' in params:
            query_params.append(('filter_createdAt_to', params['filter_created_at_to']))  # noqa: E501
        if 'filter_due_date_from' in params:
            query_params.append(('filter_dueDate_from', params['filter_due_date_from']))  # noqa: E501
        if 'filter_due_date_to' in params:
            query_params.append(('filter_dueDate_to', params['filter_due_date_to']))  # noqa: E501
        if 'filter_completed_at_from' in params:
            query_params.append(('filter_completedAt_from', params['filter_completed_at_from']))  # noqa: E501
        if 'filter_completed_at_to' in params:
            query_params.append(('filter_completedAt_to', params['filter_completed_at_to']))  # noqa: E501
        if 'filter_assigned_to_user' in params:
            query_params.append(('filter_assignedToUser', params['filter_assigned_to_user']))  # noqa: E501
        if 'filter_text' in params:
            query_params.append(('filter_text', params['filter_text']))  # noqa: E501
        if 'filter_requested_by_id' in params:
            query_params.append(('filter_requestedById', params['filter_requested_by_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task(self, **kwargs):  # noqa: E501
        """Create a Task  # noqa: E501

        Creates a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_task(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_task_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_task_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_task_with_http_info(self, **kwargs):  # noqa: E501
        """Create a Task  # noqa: E501

        Creates a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_task_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task_update(self, **kwargs):  # noqa: E501
        """Post an Update on a Task  # noqa: E501

        Posts an update on a task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_task_update(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TasksUpdateBody body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_task_update_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_task_update_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_task_update_with_http_info(self, **kwargs):  # noqa: E501
        """Post an Update on a Task  # noqa: E501

        Posts an update on a task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_task_update_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TasksUpdateBody body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task_update" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/update', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_task(self, **kwargs):  # noqa: E501
        """Update a Task  # noqa: E501

        Updates a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_task(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_task_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_task_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_task_with_http_info(self, **kwargs):  # noqa: E501
        """Update a Task  # noqa: E501

        Updates a Task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_task_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_task" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Key']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{taskId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
