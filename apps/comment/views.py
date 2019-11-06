from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from django.core.handlers.wsgi import WSGIRequest
from .models import LeaveWord, BlogComment
from tools import to_markdown

# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required


# Create your views here.


class leaveWordView(View):
    def post(self, request):
        next_url = request.POST.get('next_url', '/')
        c_name = request.POST.get('c_name', 'c_name')
        c_email = request.POST.get('c_email', 'c_email')
        c_message = request.POST.get('c_message', 'c_message')
        leaveword = LeaveWord()
        leaveword.c_name = c_name
        leaveword.c_email = c_email
        leaveword.c_message = c_message
        leaveword.save()
        return redirect(next_url)


class CommentView(View):

    def get(self, request, article_id):
        comments = BlogComment.objects.filter(article_id=article_id)
        for comment in comments:
            comment.context = to_markdown(comment.context)
        comment_context = {'article_comment_list': comments}

        response_str = render(request, 'comment.html', comment_context).content.decode('utf-8')
        return JsonResponse({'status': 'ok', 'data': response_str})

    def post(self, request: WSGIRequest, article_id):
        author = request.user
        result = {'status': 'ok', 'data': '', 'message': '评论成功'}
        if not author.is_authenticated:
            result['status'] = 'fail'
            result['message'] = '未登录用户，请登录后评论！'
        else:
            content = request.POST.get('content', '')
            if not content:
                print('content', content)
                result['status'] = 'fail'
                result['message'] = '垃圾评论'
            else:
                BlogComment(context=content, author=author, article_id=article_id).save()
                comments = BlogComment.objects.filter(article_id=article_id)
                for comment in comments:
                    comment.context = to_markdown(comment.context)
                comment_context = {'article_comment_list': comments}
                http_response = render(request, 'comment.html', comment_context).content
                result['data'] = http_response.decode('utf-8')

        return JsonResponse(result, safe=False)
