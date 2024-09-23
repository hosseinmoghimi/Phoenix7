from rest_framework.views import APIView
from .constants import FAILED,SUCCEED
from .forms import *
class ReadExcelFileApi(APIView):
    def post(self,request,*args, **kwargs):
        log = 1
        context = {}
        result = FAILED
        message = ""
        if request.method == 'POST':
            log += 1
            ReadExcelFileForm_ = ReadExcelFileForm(request.POST, request.FILES)
            if ReadExcelFileForm_.is_valid():
                log += 1
                cd=ReadExcelFileForm_.cleaned_data
                origin_file = request.FILES['file1']
                print(origin_file)
                from .excel2 import Excel
                excell=Excel(origin_file=origin_file)
                 
                if page_download is not None:
                    context['page_download'] = PageDownloadSerializer(page_download).data
                    context['result'] = SUCCEED
        context['result'] = result
        context['message'] = message
        context['log'] = log
        return JsonResponse(context)
    