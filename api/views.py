from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shop.models import *
from shop.serializers import WebSiteSerializer
# Create your views here.


def get_site(request):
    return_dict = {'resCode': 1, 'resMsg': '', 'resData': []}
    base_site = request.GET.get("base_site", None)
    area = request.GET.get("area", None)
    cls = request.GET.get("siteClass", None)
    has_phone = request.GET.get("hasPhone", None)
    has_im = request.GET.get("hasIM", None)
    has_link = request.GET.get("hasLink", None)
    query_set = WebSite.objects.filter(status=0)
    if base_site:
        query_set = query_set.filter(portal_site__name=base_site)
    if area:
        query_set = query_set.filter(area__in=area)
    if cls:
        query_set = query_set.filter(site_class_id=int(cls))
    if has_im:
        query_set = query_set.filter(has_IM=True)
    if has_link:
        query_set = query_set.filter(has_link=True)
    if has_phone:
        query_set = query_set.filter(has_phone=True)

    paginator = Paginator(query_set, 12)
    page = int(request.GET.get('page', 1))
    try:
        page_content = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_content = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_content = paginator.page(paginator.num_pages)

    site_dict = WebSiteSerializer(page_content, many=True)
    return_dict["page"] = page
    return_dict["pageCount"] = paginator.num_pages
    return_dict["resData"] = site_dict.data
    return JsonResponse(return_dict)

