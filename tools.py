import re
# import os
import socket
import base64

from django.conf import settings
from django.core.paginator import Paginator
import markdown
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def get_pages(obj_list, page: int):
    paginator = Paginator(obj_list, settings.PAGE_NUMBER)
    page_obj_list = paginator.get_page(page)
    _page = paginator.page(page)
    context = {
        'page_obj_list': page_obj_list,
        'page': _page
    }
    return context


def to_markdown(text):
    md = markdown.markdown(text, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return md


def replace_static_path(*files):
    for file in files:
        _file = open(file, 'r+', encoding='utf-8')
        text = _file.read()
        static_path_list = re.findall(r'static/[^\"\']+', text)
        # print(static_path_list)
        for static_path in static_path_list:
            new = "{{% static '{path}' %}}".format(path=re.search(r'static/([^\"\']+)', static_path).group(1))
            print(static_path, new)
            text = text.replace(static_path, new)
        _file.seek(0, 0)
        _file.write(text)


def get_ip():
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)

    def get_host_ip():
        """
        查询本机ip地址
        :return: ip
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    return ip, get_host_ip()


def str_to_base64(text: str):
    _b = base64.b64encode(bytes(text, encoding='utf-8'))
    return _b


def base64_to_str(base64_text: str):
    _b = base64.b64decode(base64_text)
    return _b


if __name__ == '__main__':
    # replace_static_path('templates/base-index.html')
    print(get_ip())
    # print(type(get_ip()))
    # print(str_to_base64(
    #     'ssr://czE5Lndld2FsbC50b3A6ODA6YXV0aF9jaGFpbl9hOm5vbmU6cGxhaW46YzNWd1pYSnpjM0l1YldVLz9vYmZzcGFyYW09TmpnME1HWXhNekF3TkRJdVpXUjFMbU51JnByb3RvcGFyYW09TVRNd01EUXlPazB6U2sxNmJBJnJlbWFya3M9VTBjZ2ZGWTNmRkl3TGprNGZERTUmZ3JvdXA9Ym1WM0xuTnpjbU5tTG5SdmNB'))
#     print(base64_to_str('c3NyOi8vY3pFNUxuZGxkMkZzYkM1MGIzQTZPREE2WVhWMGFGOWphR0ZwYmw5aE9tNXZibVU2Y0d4aGFXNDZZek5XZDFwWVNucGpNMGwxWWxkVkx6OXZZbVp6Y0dGeVlXMDlUbXBuTUUxSFdYaE5la0YzVGtSSmRWcFhVakZNYlU1MUpuQnliM1J2Y0dGeVlXMDlUVlJOZDAxRVVYbFBhekI2VTJzeE5tSkJKbkpsYldGeWEzTTlWVEJqWjJaR1dUTm1Sa2wzVEdwck5HWkVSVFVtWjNKdmRYQTlZbTFXTTB4dVRucGpiVTV0VEc1U2RtTkI='
# ))
