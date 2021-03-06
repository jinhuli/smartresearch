# coding: utf-8
from django.views.generic.base import TemplateView
from django.contrib.auth import logout


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class LoginView(TemplateView):
    template_name = 'pages/login.html'


class LogoutView(TemplateView):
    template_name = 'pages/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class StockSearchView(TemplateView):
    '''
    智能检索
    '''
    template_name = 'pages/search.html'

    def get_context_data(self, **kwargs):
        context_data = super(StockSearchView, self).get_context_data()
        q = self.request.GET.get('q')
        stock_name = self.request.GET.get('stock_name')
        ct = self.request.GET.get('ct')
        context_data.update({'q': q, 'stock_name': stock_name, 'ct': ct})
        return context_data


class StockForecastView(TemplateView):
    '''
    股票指标明细列表页
    '''
    template_name = 'pages/forecast.html'

    def get_context_data(self, **kwargs):
        context_data = super(StockForecastView, self).get_context_data()
        stock_code = kwargs.get('code')
        stock_name = self.request.GET.get('stock_name')
        context_data.update(
            {'stock_code': stock_code, 'stock_name': stock_name})
        return context_data


class StockForecastMoreView(TemplateView):
    '''
    指标明细相关言报、公告、社交页面
    '''
    template_name = 'pages/forecast_more.html'

    def get_context_data(self, **kwargs):
        context_data = super(StockForecastMoreView, self).get_context_data()
        q = self.request.GET.get('q')
        stock_name = self.request.GET.get('stock_name')
        ct = self.request.GET.get('ct')
        context_data.update({'q': q, 'stock_name': stock_name, 'ct': ct})
        return context_data


class StockForecastDiffView(TemplateView):
    '''
    股票对比页面
    '''
    template_name = 'pages/forecast_diff.html'

    def get_context_data(self, **kwargs):
        context_data = super(StockForecastDiffView, self).get_context_data()
        code = self.request.GET.get('stock_code')
        name = self.request.GET.get('stock_name')
        context_data.update({'stock_code': code, 'stock_name': name})
        return context_data


class StockIndustryRankView(TemplateView):
    '''
    股票行业排名页面
    '''
    template_name = 'pages/industry_rank.html'


class StockArticleDetailView(TemplateView):
    '''
    文章详情页面
    '''
    template_name = 'pages/detail.html'

    def get_context_data(self, **kwargs):
        context_data = super(StockArticleDetailView, self).get_context_data()
        pk = self.request.GET.get('pk')
        ct = self.request.GET.get('ct')
        context_data.update({'pk': pk, 'ct': ct})
        return context_data
