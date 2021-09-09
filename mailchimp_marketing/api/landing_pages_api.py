# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.62
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class LandingPagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def delete_page(self, page_id, **kwargs):  # noqa: E501
        """Delete landing page  # noqa: E501

        Delete a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_page(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_page_with_http_info(page_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_page_with_http_info(page_id, **kwargs)  # noqa: E501
            return data

    def delete_page_with_http_info(self, page_id, **kwargs):  # noqa: E501
        """Delete landing page  # noqa: E501

        Delete a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_page_with_http_info(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all(self, **kwargs):  # noqa: E501
        """List landing pages  # noqa: E501

        Get all landing pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_dir: Determines the order direction for sorted results.
        :param str sort_field: Returns files sorted by the specified field.
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. Default value is 10. Maximum value is 1000
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_with_http_info(self, **kwargs):  # noqa: E501
        """List landing pages  # noqa: E501

        Get all landing pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_dir: Determines the order direction for sorted results.
        :param str sort_field: Returns files sorted by the specified field.
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. Default value is 10. Maximum value is 1000
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort_dir', 'sort_field', 'fields', 'exclude_fields', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all" % key
                )
            params[key] = val
        del params['kwargs']

        if 'count' in params and params['count'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling ``, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_dir' in params:
            query_params.append(('sort_dir', params['sort_dir']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_page(self, page_id, **kwargs):  # noqa: E501
        """Get landing page info  # noqa: E501

        Get information about a specific page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_page_with_http_info(page_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_page_with_http_info(page_id, **kwargs)  # noqa: E501
            return data

    def get_page_with_http_info(self, page_id, **kwargs):  # noqa: E501
        """Get landing page info  # noqa: E501

        Get information about a specific page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_page_content(self, page_id, **kwargs):  # noqa: E501
        """Get landing page content  # noqa: E501

        Get the the HTML for your landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_content(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPageContent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_page_content_with_http_info(page_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_page_content_with_http_info(page_id, **kwargs)  # noqa: E501
            return data

    def get_page_content_with_http_info(self, page_id, **kwargs):  # noqa: E501
        """Get landing page content  # noqa: E501

        Get the the HTML for your landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_content_with_http_info(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPageContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}/content', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPageContent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_page(self, page_id, body, **kwargs):  # noqa: E501
        """Update landing page  # noqa: E501

        Update a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_page(page_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param LandingPage2 body:  (required)
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_page_with_http_info(page_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_page_with_http_info(page_id, body, **kwargs)  # noqa: E501
            return data

    def update_page_with_http_info(self, page_id, body, **kwargs):  # noqa: E501
        """Update landing page  # noqa: E501

        Update a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_page_with_http_info(page_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :param LandingPage2 body:  (required)
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, body, **kwargs):  # noqa: E501
        """Add landing page  # noqa: E501

        Create a new Mailchimp landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LandingPage1 body:  (required)
        :param bool use_default_list: Will create the Landing Page using the account's Default List instead of requiring a list_id.
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add landing page  # noqa: E501

        Create a new Mailchimp landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LandingPage1 body:  (required)
        :param bool use_default_list: Will create the Landing Page using the account's Default List instead of requiring a list_id.
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'use_default_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'use_default_list' in params:
            query_params.append(('use_default_list', params['use_default_list']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def publish_page(self, page_id, **kwargs):  # noqa: E501
        """Publish landing page  # noqa: E501

        Publish a landing page that is in draft, unpublished, or has been previously published and edited.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_page(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.publish_page_with_http_info(page_id, **kwargs)  # noqa: E501
        else:
            (data) = self.publish_page_with_http_info(page_id, **kwargs)  # noqa: E501
            return data

    def publish_page_with_http_info(self, page_id, **kwargs):  # noqa: E501
        """Publish landing page  # noqa: E501

        Publish a landing page that is in draft, unpublished, or has been previously published and edited.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_page_with_http_info(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: LandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}/actions/publish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unpublish_page(self, page_id, **kwargs):  # noqa: E501
        """Unpublish landing page  # noqa: E501

        Unpublish a landing page that is in draft or has been published.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_page(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unpublish_page_with_http_info(page_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unpublish_page_with_http_info(page_id, **kwargs)  # noqa: E501
            return data

    def unpublish_page_with_http_info(self, page_id, **kwargs):  # noqa: E501
        """Unpublish landing page  # noqa: E501

        Unpublish a landing page that is in draft or has been published.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_page_with_http_info(page_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_id: The unique id for the page. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unpublish_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if ('page_id' not in params or
                params['page_id'] is None):
            raise ValueError("Missing the required parameter `page_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in params:
            path_params['page_id'] = params['page_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/landing-pages/{page_id}/actions/unpublish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
