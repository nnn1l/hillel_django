import logging

from django.utils.deprecation import MiddlewareMixin

from general.models import RequestStatistics

logger = logging.getLogger('middlewares')

class RequestStatisticMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        logger.debug('Called BEFORE view and get_response')
        response = self.get_response(request)
        logger.debug('Called AFTER view and get_response')
        return  response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and not request.path.startswith("/admin"):
            stats, is_created = RequestStatistics.objects.get_or_create(user=request.user)
            stats.requests += 1
            stats.save()

    def process_exception(self, request, exception):
        """
        Інкрементує поле 'exceptions' в моделі RequestStatistics
        кожного разу, коли відбувається виключення.
        """
        if request.user.is_authenticated and not request.path.startswith("/admin"):
            try:
                stats, created = RequestStatistics.objects.get_or_create(user=request.user)
                stats.exceptions += 1
                stats.save()
            except Exception as e:
                logger.error(f"Помилка при оновленні статистики виключень: {e}")
        return None  